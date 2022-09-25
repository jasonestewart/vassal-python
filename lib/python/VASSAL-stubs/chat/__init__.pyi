import VASSAL.build.module
import VASSAL.chat.messageboard
import VASSAL.chat.node
import VASSAL.chat.peer2peer
import VASSAL.chat.ui
import VASSAL.command
import VASSAL.configure
import java.awt
import java.beans
import java.util
import javax.swing
import typing



class AddressBookServerConfigurer(VASSAL.configure.Configurer):
    def __init__(self, string: str, string2: str, hybridClient: 'HybridClient'): ...
    def getControls(self) -> java.awt.Component: ...
    def getValueString(self) -> str: ...
    @typing.overload
    def setValue(self, object: typing.Any) -> None: ...
    @typing.overload
    def setValue(self, string: str) -> None: ...

class ChatServerConnection(VASSAL.build.module.ServerConnection):
    ROOM: typing.ClassVar[str] = ...
    AVAILABLE_ROOMS: typing.ClassVar[str] = ...
    STATUS: typing.ClassVar[str] = ...
    PLAYER_INFO: typing.ClassVar[str] = ...
    INCOMING_MSG: typing.ClassVar[str] = ...
    STATUS_SERVER: typing.ClassVar[str] = ...
    DEFAULT_ROOM_NAME: typing.ClassVar[str] = ...
    def getAvailableRooms(self) -> typing.List['Room']: ...
    def getRoom(self) -> 'Room': ...
    def getUserInfo(self) -> 'Player': ...
    def sendTo(self, player: 'Player', command: VASSAL.command.Command) -> None: ...
    def setRoom(self, room: 'Room') -> None: ...
    def setUserInfo(self, player: 'Player') -> None: ...

class ChatServerFactory:
    TYPE_KEY: typing.ClassVar[str] = ...
    def __init__(self): ...
    @staticmethod
    def build(properties: java.util.Properties) -> ChatServerConnection: ...
    def buildServer(self, properties: java.util.Properties) -> ChatServerConnection: ...
    @staticmethod
    def register(string: str, chatServerFactory: 'ChatServerFactory') -> None: ...

class CommandDecoder(java.beans.PropertyChangeListener):
    def __init__(self): ...
    def propertyChange(self, propertyChangeEvent: java.beans.PropertyChangeEvent) -> None: ...

class Compressor:
    @staticmethod
    def compress(byteArray: typing.List[int]) -> typing.List[int]: ...
    @staticmethod
    def decompress(byteArray: typing.List[int]) -> typing.List[int]: ...

class HttpRequestWrapper:
    def __init__(self, string: str): ...
    @typing.overload
    def doGet(self, string: str, properties: java.util.Properties) -> java.util.List[str]: ...
    @typing.overload
    def doGet(self, properties: java.util.Properties) -> java.util.List[str]: ...
    @typing.overload
    def doPost(self, string: str, properties: java.util.Properties) -> java.util.List[str]: ...
    @typing.overload
    def doPost(self, properties: java.util.Properties) -> java.util.List[str]: ...

class InviteCommand(VASSAL.command.Command):
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, chatServerConnection: ChatServerConnection): ...
    def getPlayer(self) -> str: ...
    def getPlayerId(self) -> str: ...
    def getRoom(self) -> str: ...
    def isLoggable(self) -> bool: ...

class InviteEncoder(VASSAL.command.CommandEncoder):
    COMMAND_PREFIX: typing.ClassVar[str] = ...
    def __init__(self, chatServerConnection: ChatServerConnection): ...
    def decode(self, string: str) -> VASSAL.command.Command: ...
    def encode(self, command: VASSAL.command.Command) -> str: ...

class LockableRoom:
    def getName(self) -> str: ...
    def getOwningPlayer(self) -> 'Player': ...
    def isLocked(self) -> bool: ...
    def isOwner(self, string: str) -> bool: ...

class MainRoomChecker:
    def __init__(self): ...
    def filter(self, string: str, string2: str, string3: str) -> str: ...

class MainRoomFilter(VASSAL.command.CommandFilter):
    def __init__(self): ...

class MessageServer: ...

class Player:
    def getId(self) -> str: ...
    def getName(self) -> str: ...
    def getStatus(self) -> 'PlayerStatus': ...

class PlayerEncoder:
    def playerToString(self, player: Player) -> str: ...
    def stringToPlayer(self, string: str) -> Player: ...

class PlayerInfoWindow(javax.swing.JDialog):
    def __init__(self, frame: java.awt.Frame, simplePlayer: 'SimplePlayer'): ...

class PlayerStatus: ...

class PrivMsgCommand(VASSAL.command.Command):
    def __init__(self, privateChatManager: 'PrivateChatManager', player: Player, string: str): ...
    def executeCommand(self) -> None: ...
    def getMessage(self) -> str: ...
    def getSender(self) -> Player: ...
    def isLoggable(self) -> bool: ...
    def myUndoCommand(self) -> VASSAL.command.Command: ...

class PrivateChatEncoder(VASSAL.command.CommandEncoder):
    COMMAND_PREFIX: typing.ClassVar[str] = ...
    def __init__(self, playerEncoder: PlayerEncoder, privateChatManager: 'PrivateChatManager'): ...
    def decode(self, string: str) -> VASSAL.command.Command: ...
    def encode(self, command: VASSAL.command.Command) -> str: ...

class PrivateChatManager:
    def __init__(self, chatServerConnection: ChatServerConnection): ...
    def getChatterFor(self, player: Player) -> 'PrivateChatter': ...

class PrivateChatter(VASSAL.build.module.Chatter):
    def __init__(self, player: Player, chatServerConnection: ChatServerConnection): ...
    def getClient(self) -> VASSAL.build.module.ServerConnection: ...
    def getPlayer(self) -> Player: ...
    @typing.overload
    def send(self, string: str, string2: str) -> None: ...
    @typing.overload
    def send(self, string: str) -> None: ...

class Room:
    def addPlayer(self, player: Player) -> None: ...
    def getName(self) -> str: ...
    def getPlayerList(self) -> java.util.List[Player]: ...
    def removePlayer(self, player: Player) -> None: ...

class ServerAddressBook:
    CURRENT_SERVER: typing.ClassVar[str] = ...
    def __init__(self): ...
    def addPropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    @staticmethod
    def changeServerPopup(jComponent: javax.swing.JComponent) -> None: ...
    @staticmethod
    def editCurrentServer(boolean: bool) -> None: ...
    def getControls(self) -> javax.swing.JComponent: ...
    def getCurrentDescription(self) -> str: ...
    def getCurrentIcon(self) -> javax.swing.Icon: ...
    def getDefaultServerProperties(self) -> java.util.Properties: ...
    @typing.overload
    @staticmethod
    def getExternalAddress() -> str: ...
    @typing.overload
    @staticmethod
    def getExternalAddress(string: str) -> str: ...
    @staticmethod
    def getInstance() -> 'ServerAddressBook': ...
    @staticmethod
    def getLocalAddress() -> str: ...
    def isEnabled(self) -> bool: ...
    def removePropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def setCurrentServer(self, properties: java.util.Properties) -> None: ...
    def setEnabled(self, boolean: bool) -> None: ...
    def setFrozen(self, boolean: bool) -> None: ...
    def showPopup(self, jComponent: javax.swing.JComponent) -> None: ...

class ServerConfigurer(VASSAL.configure.Configurer):
    def __init__(self, string: str, string2: str, hybridClient: 'HybridClient'): ...
    def getControls(self) -> java.awt.Component: ...
    def getValueString(self) -> str: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    @typing.overload
    def setValue(self, object: typing.Any) -> None: ...
    @typing.overload
    def setValue(self, string: str) -> None: ...

class ServerStatus:
    def getHistory(self, string: str) -> typing.List['ServerStatus.ModuleSummary']: ...
    def getStatus(self) -> typing.List['ServerStatus.ModuleSummary']: ...
    def getSupportedTimeRanges(self) -> typing.List[str]: ...
    class ModuleSummary:
        @typing.overload
        def __init__(self, string: str): ...
        @typing.overload
        def __init__(self, string: str, roomArray: typing.List[Room]): ...
        def addRoom(self, room: Room) -> None: ...
        def getModuleName(self) -> str: ...
        def getRoom(self, string: str) -> 'SimpleRoom': ...
        def getRooms(self) -> typing.List[Room]: ...
        def numPlayers(self) -> int: ...
        def setModuleName(self, string: str) -> None: ...
        def toString(self) -> str: ...

class SoundEncoder(VASSAL.command.CommandEncoder):
    COMMAND_PREFIX: typing.ClassVar[str] = ...
    def __init__(self, playerEncoder: PlayerEncoder): ...
    def decode(self, string: str) -> VASSAL.command.Command: ...
    def encode(self, command: VASSAL.command.Command) -> str: ...
    class Cmd(VASSAL.command.Command):
        TOO_SOON: typing.ClassVar[int] = ...
        def __init__(self, string: str, player: Player): ...
        def getSender(self) -> Player: ...

class SynchCommand(VASSAL.command.Command):
    def __init__(self, player: Player, chatServerConnection: ChatServerConnection): ...
    def getPlayer(self) -> Player: ...
    def isLoggable(self) -> bool: ...

class SynchEncoder(VASSAL.command.CommandEncoder):
    COMMAND_PREFIX: typing.ClassVar[str] = ...
    def __init__(self, playerEncoder: PlayerEncoder, chatServerConnection: ChatServerConnection): ...
    def decode(self, string: str) -> VASSAL.command.Command: ...
    def encode(self, command: VASSAL.command.Command) -> str: ...

class WelcomeMessageServer:
    def getWelcomeMessage(self) -> VASSAL.command.Command: ...

class CgiServerStatus(ServerStatus):
    LAST_DAY: typing.ClassVar[str] = ...
    LAST_WEEK: typing.ClassVar[str] = ...
    LAST_MONTH: typing.ClassVar[str] = ...
    def __init__(self): ...
    def getHistory(self, string: str) -> typing.List[ServerStatus.ModuleSummary]: ...
    def getStatus(self) -> typing.List[ServerStatus.ModuleSummary]: ...
    def getSupportedTimeRanges(self) -> typing.List[str]: ...

class DummyClient(ChatServerConnection, VASSAL.chat.ui.ChatControlsInitializer):
    def __init__(self): ...
    def addPropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def getAvailableRooms(self) -> typing.List[Room]: ...
    def getRoom(self) -> Room: ...
    def getStatusServer(self) -> ServerStatus: ...
    def getUserInfo(self) -> Player: ...
    def initializeControls(self, chatServerControls: VASSAL.chat.ui.ChatServerControls) -> None: ...
    def isConnected(self) -> bool: ...
    def sendTo(self, player: Player, command: VASSAL.command.Command) -> None: ...
    def sendToOthers(self, command: VASSAL.command.Command) -> None: ...
    def setConnected(self, boolean: bool) -> None: ...
    def setRoom(self, room: Room) -> None: ...
    def setUserInfo(self, player: Player) -> None: ...
    def uninitializeControls(self, chatServerControls: VASSAL.chat.ui.ChatServerControls) -> None: ...

class DummyMessageServer(VASSAL.chat.messageboard.MessageBoard, WelcomeMessageServer):
    def __init__(self): ...
    def getMessages(self) -> typing.List[VASSAL.chat.messageboard.Message]: ...
    def getWelcomeMessage(self) -> VASSAL.command.Command: ...
    def postMessage(self, string: str) -> None: ...

class HttpMessageServer(VASSAL.chat.messageboard.MessageBoard, WelcomeMessageServer):
    @typing.overload
    def __init__(self, peerPoolInfo: VASSAL.chat.peer2peer.PeerPoolInfo): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, peerPoolInfo: VASSAL.chat.peer2peer.PeerPoolInfo): ...
    def getMessages(self) -> typing.List[VASSAL.chat.messageboard.Message]: ...
    def getWelcomeMessage(self) -> VASSAL.command.Command: ...
    def postMessage(self, string: str) -> None: ...

class HybridClient(ChatServerConnection, PlayerEncoder, VASSAL.chat.ui.ChatControlsInitializer):
    def __init__(self): ...
    def addPropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def getAvailableRooms(self) -> typing.List[Room]: ...
    def getDelegate(self) -> ChatServerConnection: ...
    def getRoom(self) -> Room: ...
    def getUserInfo(self) -> Player: ...
    def initializeControls(self, chatServerControls: VASSAL.chat.ui.ChatServerControls) -> None: ...
    def isConnected(self) -> bool: ...
    def playerToString(self, player: Player) -> str: ...
    def sendTo(self, player: Player, command: VASSAL.command.Command) -> None: ...
    def sendToOthers(self, command: VASSAL.command.Command) -> None: ...
    def setConnected(self, boolean: bool) -> None: ...
    def setDelegate(self, chatServerConnection: ChatServerConnection) -> None: ...
    def setRoom(self, room: Room) -> None: ...
    def setUserInfo(self, player: Player) -> None: ...
    def stringToPlayer(self, string: str) -> Player: ...
    def uninitializeControls(self, chatServerControls: VASSAL.chat.ui.ChatServerControls) -> None: ...
    def updateDisplayControls(self, icon: javax.swing.Icon, string: str) -> None: ...

class LockableChatServerConnection(ChatServerConnection):
    def doInvite(self, string: str, string2: str) -> None: ...
    def doKick(self, player: Player) -> None: ...
    def getDefaultRoomName(self) -> str: ...
    def isDefaultRoom(self, room: Room) -> bool: ...
    def isInvitable(self, player: Player) -> bool: ...
    def isKickable(self, player: Player) -> bool: ...
    def lockRoom(self, lockableRoom: LockableRoom) -> None: ...
    def sendInvite(self, player: Player) -> None: ...

class SimplePlayer(Player):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, playerStatus: PlayerStatus): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getId(self) -> str: ...
    def getName(self) -> str: ...
    def getStatus(self) -> PlayerStatus: ...
    def hashCode(self) -> int: ...
    def setId(self, string: str) -> None: ...
    def setName(self, string: str) -> None: ...
    def setStatus(self, playerStatus: PlayerStatus) -> None: ...
    def toString(self) -> str: ...
    def updateStatus(self) -> None: ...

class SimpleRoom(Room):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, room: Room): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, playerArray: typing.List[Player]): ...
    def addPlayer(self, player: Player) -> None: ...
    def contains(self, player: Player) -> bool: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getName(self) -> str: ...
    def getPlayer(self, string: str) -> Player: ...
    def getPlayerList(self) -> java.util.List[Player]: ...
    def hashCode(self) -> int: ...
    def numPlayers(self) -> int: ...
    def removePlayer(self, player: Player) -> None: ...
    def setName(self, string: str) -> None: ...
    def setPlayers(self, playerArray: typing.List[Player]) -> None: ...
    def toString(self) -> str: ...

class SimpleStatus(PlayerStatus):
    CRC: typing.ClassVar[str] = ...
    MODULE_VERSION: typing.ClassVar[str] = ...
    IP: typing.ClassVar[str] = ...
    CLIENT: typing.ClassVar[str] = ...
    PROFILE: typing.ClassVar[str] = ...
    AWAY: typing.ClassVar[str] = ...
    LOOKING: typing.ClassVar[str] = ...
    NAME: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool, boolean2: bool): ...
    @typing.overload
    def __init__(self, boolean: bool, boolean2: bool, string: str): ...
    @typing.overload
    def __init__(self, boolean: bool, boolean2: bool, string: str, string2: str, string3: str, string4: str, string5: str): ...
    @staticmethod
    def decode(string: str) -> 'SimpleStatus': ...
    @staticmethod
    def encode(simpleStatus: 'SimpleStatus') -> str: ...
    def getClient(self) -> str: ...
    def getCrc(self) -> str: ...
    def getIp(self) -> str: ...
    def getModuleVersion(self) -> str: ...
    def getProfile(self) -> str: ...
    def isAway(self) -> bool: ...
    def isLooking(self) -> bool: ...
    def updateStatus(self) -> None: ...

class DynamicClient(HybridClient):
    def __init__(self): ...
    def setConnected(self, boolean: bool) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.chat")``.

    AddressBookServerConfigurer: typing.Type[AddressBookServerConfigurer]
    CgiServerStatus: typing.Type[CgiServerStatus]
    ChatServerConnection: typing.Type[ChatServerConnection]
    ChatServerFactory: typing.Type[ChatServerFactory]
    CommandDecoder: typing.Type[CommandDecoder]
    Compressor: typing.Type[Compressor]
    DummyClient: typing.Type[DummyClient]
    DummyMessageServer: typing.Type[DummyMessageServer]
    DynamicClient: typing.Type[DynamicClient]
    HttpMessageServer: typing.Type[HttpMessageServer]
    HttpRequestWrapper: typing.Type[HttpRequestWrapper]
    HybridClient: typing.Type[HybridClient]
    InviteCommand: typing.Type[InviteCommand]
    InviteEncoder: typing.Type[InviteEncoder]
    LockableChatServerConnection: typing.Type[LockableChatServerConnection]
    LockableRoom: typing.Type[LockableRoom]
    MainRoomChecker: typing.Type[MainRoomChecker]
    MainRoomFilter: typing.Type[MainRoomFilter]
    MessageServer: typing.Type[MessageServer]
    Player: typing.Type[Player]
    PlayerEncoder: typing.Type[PlayerEncoder]
    PlayerInfoWindow: typing.Type[PlayerInfoWindow]
    PlayerStatus: typing.Type[PlayerStatus]
    PrivMsgCommand: typing.Type[PrivMsgCommand]
    PrivateChatEncoder: typing.Type[PrivateChatEncoder]
    PrivateChatManager: typing.Type[PrivateChatManager]
    PrivateChatter: typing.Type[PrivateChatter]
    Room: typing.Type[Room]
    ServerAddressBook: typing.Type[ServerAddressBook]
    ServerConfigurer: typing.Type[ServerConfigurer]
    ServerStatus: typing.Type[ServerStatus]
    SimplePlayer: typing.Type[SimplePlayer]
    SimpleRoom: typing.Type[SimpleRoom]
    SimpleStatus: typing.Type[SimpleStatus]
    SoundEncoder: typing.Type[SoundEncoder]
    SynchCommand: typing.Type[SynchCommand]
    SynchEncoder: typing.Type[SynchEncoder]
    WelcomeMessageServer: typing.Type[WelcomeMessageServer]
    messageboard: VASSAL.chat.messageboard.__module_protocol__
    node: VASSAL.chat.node.__module_protocol__
    peer2peer: VASSAL.chat.peer2peer.__module_protocol__
    ui: VASSAL.chat.ui.__module_protocol__