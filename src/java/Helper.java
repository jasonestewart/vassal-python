package VASSAL.tools.python;

import VASSAL.Info;
import VASSAL.counters.Decorator;
import VASSAL.counters.GamePiece;
import VASSAL.counters.UsePrototype;
import VASSAL.launch.StandardConfig;
import VASSAL.build.GameModule;
import VASSAL.build.module.GameState;
import VASSAL.build.module.metadata.SaveMetaData;
import VASSAL.command.Command;
import VASSAL.tools.ArchiveWriter;
import VASSAL.tools.io.FileArchive;
import VASSAL.tools.io.ObfuscatingOutputStream;
import VASSAL.tools.io.ZipArchive;

import javax.swing.SwingUtilities;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;
import java.nio.charset.StandardCharsets;

public final class Helper {
  private final String pythonVersion;
  private final String javaVersion;
  private final Command[] myCommand = new Command[1];
  private final boolean inited;
  public void shutdown(){System.exit(0);}

  public Helper(String version) {
    pythonVersion = version;
    javaVersion = "0.1";
    inited = false;
  }

  public String getVASSALVersion() {
    return Info.getVersion();
  }

  public String getPythonVersion() {
    return pythonVersion;
  }

  public String getJavaVersion() {
    return javaVersion;
  }

  public Command getCommand() {
    return myCommand[0];
  }

  public GamePiece getPrototype(GamePiece p) {
    return Decorator.getDecorator(p, UsePrototype.class);
  }

  public String getBuildString(GameModule module) {
    String buildString = null;
    try {
      Method method = GameModule.class.getDeclaredMethod("buildString", null);
      method.setAccessible(true);
      buildString = (String) method.invoke(module, null);
    }
    catch (NoSuchMethodException | InvocationTargetException | IllegalAccessException e) {
      e.printStackTrace();
    }
    return buildString;
  }

  public void saveGameModule(GameModule module) {
    try {
      // run save() in the GUI thread
      SwingUtilities.invokeAndWait(() -> doSaveGameModule(module));
    }
    catch (InterruptedException | InvocationTargetException e) {
      e.printStackTrace();
    }
  }

  private void doSaveGameModule(GameModule module) {
    try {
      module.save();
    }
    catch (NullPointerException npe) {
      npe.printStackTrace();
      // ignore until we fix GameModule.save()
    }
  }

  /*
  public void writeBuildFile(ArrayList<Buildable> buildables) {
    org.w3c.dom.Document doc = Builder.createNewDocument();

    Element el = doc.createElement(getClass().getName());
    GameModule module = GameModule.getGameModule();
    String[] names = module.getAttributeNames();
    for (String name : names) {
      String val = module.getAttributeValueString(name);
      if (val != null) {
        el.setAttribute(name, val);
      }
    }

    for (Buildable b : buildables) {
      el.appendChild(b.getBuildElement(doc));
    }
    final String buildString = Builder.toString(doc);
  }
*/
  public GameModule initGameModule(String moduleFilename) {
    System.err.println("VASSAL: initGameModule: start");
    try {
      // run doReadSavedGame() in the GUI thread
      SwingUtilities.invokeAndWait(() -> doInitGameModule(moduleFilename));
    }
    catch (InterruptedException | InvocationTargetException e) {
      e.printStackTrace();
      System.exit(1);
    }
    System.err.println("VASSAL: initGameModule: end");
    return GameModule.getGameModule();
  }

  public void resaveSavedGame(String moduleFilename, String saveGameFilename, Command c) {
    // we've already initialized the GameModule, so we just use it to encode
    final String newSave = GameModule.getGameModule().encode(c);
    try (FileArchive archive = new ZipArchive(new File(saveGameFilename))) {
      try (OutputStream zout = archive.getOutputStream(GameState.SAVEFILE_ZIP_ENTRY);
           BufferedOutputStream bout = new BufferedOutputStream(zout);
           OutputStream out = new ObfuscatingOutputStream(bout)) {
        out.write(newSave.getBytes(StandardCharsets.UTF_8));
      }
      catch (IOException e) {
        e.printStackTrace();
      }
      (new SaveMetaData()).save(archive);
    }
    catch (IOException e) {
      e.printStackTrace();
    }
  }

  public Command readSavedGame(String moduleFilename, String saveGameFilename) {
    // we have to run code in the GUI thread, so pretend we have a GUI
    System.setProperty("java.awt.headless", "false");

    try {
      // run doReadSavedGame() in the GUI thread
      SwingUtilities.invokeAndWait(() -> doReadSavedGame(moduleFilename, saveGameFilename));
    }
    catch (InterruptedException | InvocationTargetException e) {
      e.printStackTrace();
    }
    return myCommand[0];
  }

  private void doReadSavedGame(String moduleFilename, String saveGameFilename) {
    try {
      doInitGameModule(moduleFilename);
      myCommand[0] = GameModule.getGameModule().getGameState().decodeSavedGame(new File(saveGameFilename));
    }
    catch (IOException e) {
      e.printStackTrace();
    }
  }

  private void doInitGameModule(String moduleFilename) {
    System.err.println("VASSAL: doInit: start");
    try {
      // we need to do a bit of reflection to ensure the needed classes exist
      init();

      System.err.println("VASSAL: doInit: init finished");

      // now we can actually decode the savedGame
      System.err.println("VASSAL: doInit: using moduleFilename: " + moduleFilename);
      ArchiveWriter aw = new ArchiveWriter(moduleFilename);
        System.err.println("VASSAL: doInit: creating GameModule");
        GameModule gm = new GameModule(aw);
        System.err.println("VASSAL: doInit: finished creating GameModule");
      GameModule.init(gm);
      System.err.println("VASSAL: doInit: GameModule.init finished");
    }
    catch (IOException e) {
      e.printStackTrace();
      System.exit(1);
    }
    System.err.println("VASSAL: doInit: end");
  }

  // We need to make an instance of PlayerMenuManager available in order to decode the savedGame
  private static void init() {
    System.err.println("VASSAL: init: start");
    try {
      Info.setConfig(new StandardConfig());
    }
    catch (IOException e) {
      System.err.println("VASSAL: " + e.getMessage()); //NON-NLS
      e.printStackTrace();
      System.exit(1);
    }
    try {
      final Class<?> clazz = Class.forName("VASSAL.launch.Player$PlayerMenuManager");
      final Constructor<?> declaredConstructor = clazz.getDeclaredConstructor();
      declaredConstructor.setAccessible(true);
      declaredConstructor.newInstance();
    }
    catch (InstantiationException | InvocationTargetException | NoSuchMethodException | IllegalAccessException | ClassNotFoundException e) {
      e.printStackTrace();
    }
    System.err.println("VASSAL: init: end");
  }
}
