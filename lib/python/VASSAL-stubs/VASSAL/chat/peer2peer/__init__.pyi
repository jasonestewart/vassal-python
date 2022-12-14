import VASSAL.chat
import VASSAL.chat.ui
import VASSAL.command
import java.beans
import java.io
import java.lang
import java.net
import java.util
import org.litesoft.p2pchat
import typing



class AcceptPeerThread(java.lang.Thread):
    @typing.overload
    def __init__(self, int: int, pendingPeerManager: org.litesoft.p2pchat.PendingPeerManager): ...
    @typing.overload
    def __init__(self, serverSocket: java.net.ServerSocket, pendingPeerManager: org.litesoft.p2pchat.PendingPeerManager): ...
    def getPort(self) -> int: ...
    def halt(self) -> None: ...
    def run(self) -> None: ...
    def start(self) -> None: ...

class EchoClient(java.lang.Runnable, java.beans.PropertyChangeListener):
    NAME: typing.ClassVar[str] = ...
    def __init__(self, chatServerConnection: VASSAL.chat.ChatServerConnection, int: int, int2: int, fileWriter: java.io.FileWriter): ...
    def propertyChange(self, propertyChangeEvent: java.beans.PropertyChangeEvent) -> None: ...
    @staticmethod
    def report(roomArray: typing.List[VASSAL.chat.Room]) -> str: ...
    def run(self) -> None: ...
    def showCHAT(self, peerInfo: org.litesoft.p2pchat.PeerInfo, string: str) -> None: ...

class IpWatch(java.lang.Runnable):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, long: int): ...
    def addPropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def getCurrentIp(self) -> str: ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    def run(self) -> None: ...

class P2PClient(VASSAL.chat.ChatServerConnection, VASSAL.chat.ui.ChatControlsInitializer, org.litesoft.p2pchat.UserDialog, VASSAL.chat.PlayerEncoder):
    @typing.overload
    def __init__(self, commandEncoder: VASSAL.command.CommandEncoder, welcomeMessageServer: typing.Union[VASSAL.chat.WelcomeMessageServer, typing.Callable], peerPool: 'PeerPool'): ...
    @typing.overload
    def __init__(self, commandEncoder: VASSAL.command.CommandEncoder, welcomeMessageServer: typing.Union[VASSAL.chat.WelcomeMessageServer, typing.Callable], peerPool: 'PeerPool', properties: java.util.Properties): ...
    @typing.overload
    def addPropertyChangeListener(self, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    @typing.overload
    def addPropertyChangeListener(self, string: str, propertyChangeListener: java.beans.PropertyChangeListener) -> None: ...
    def getAvailableRooms(self) -> typing.List[VASSAL.chat.Room]: ...
    def getRoom(self) -> VASSAL.chat.Room: ...
    def getRoomMgr(self) -> 'RoomManager': ...
    def getStatusServer(self) -> VASSAL.chat.ServerStatus: ...
    def getUserInfo(self) -> VASSAL.chat.Player: ...
    def initializeControls(self, chatServerControls: VASSAL.chat.ui.ChatServerControls) -> None: ...
    def isConnected(self) -> bool: ...
    def playerToString(self, player: VASSAL.chat.Player) -> str: ...
    def sendTo(self, player: VASSAL.chat.Player, command: VASSAL.command.Command) -> None: ...
    def sendToAll(self, string: str) -> None: ...
    @typing.overload
    def sendToOthers(self, command: VASSAL.command.Command) -> None: ...
    @typing.overload
    def sendToOthers(self, string: str) -> None: ...
    def setActivePeerManager(self, activePeerManager: org.litesoft.p2pchat.ActivePeerManager) -> None: ...
    def setConnected(self, boolean: bool) -> None: ...
    def setPendingPeerManager(self, pendingPeerManager: org.litesoft.p2pchat.PendingPeerManager) -> None: ...
    def setRoom(self, room: VASSAL.chat.Room) -> None: ...
    def setUserInfo(self, player: VASSAL.chat.Player) -> None: ...
    def showCHAT(self, peerInfo: org.litesoft.p2pchat.PeerInfo, string: str) -> None: ...
    def showConnect(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showConnectFailed(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showDisconnect(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showHELO(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showNAME(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showPMSG(self, peerInfo: org.litesoft.p2pchat.PeerInfo, string: str) -> None: ...
    def showStreamsFailed(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showUnrecognized(self, peerInfo: org.litesoft.p2pchat.PeerInfo, string: str) -> None: ...
    def stringToPlayer(self, string: str) -> VASSAL.chat.Player: ...
    def uninitializeControls(self, chatServerControls: VASSAL.chat.ui.ChatServerControls) -> None: ...

class P2PClientFactory(VASSAL.chat.ChatServerFactory):
    P2P_TYPE: typing.ClassVar[str] = ...
    P2P_LISTEN_PORT: typing.ClassVar[str] = ...
    P2P_SERVER_IP: typing.ClassVar[str] = ...
    P2P_SERVER_PORT: typing.ClassVar[str] = ...
    P2P_SERVER_NAME: typing.ClassVar[str] = ...
    P2P_SERVER_PW: typing.ClassVar[str] = ...
    def __init__(self): ...
    def buildServer(self, properties: java.util.Properties) -> VASSAL.chat.ChatServerConnection: ...

class P2PPlayer(VASSAL.chat.SimplePlayer):
    def __init__(self, peerInfo: org.litesoft.p2pchat.PeerInfo): ...
    def equals(self, object: typing.Any) -> bool: ...
    def getId(self) -> str: ...
    def getInfo(self) -> org.litesoft.p2pchat.PeerInfo: ...
    def getRoom(self) -> str: ...
    def hashCode(self) -> int: ...
    def setId(self, string: str) -> None: ...
    def setProperty(self, string: str, string2: str) -> None: ...
    def setRoom(self, string: str) -> None: ...
    def setStats(self, player: VASSAL.chat.Player) -> None: ...
    def summary(self) -> str: ...

class PeerPool:
    def connectFailed(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def disconnect(self) -> None: ...
    def initialize(self, p2PPlayer: P2PPlayer, pendingPeerManager: org.litesoft.p2pchat.PendingPeerManager) -> None: ...

class PeerPoolInfo:
    def getModuleName(self) -> str: ...
    def getUserName(self) -> str: ...

class RoomManager:
    def __init__(self): ...
    def clear(self) -> None: ...
    def getDefaultRoom(self) -> VASSAL.chat.Room: ...
    def getPlayerById(self, string: str) -> P2PPlayer: ...
    def getRoomContaining(self, player: VASSAL.chat.Player) -> VASSAL.chat.SimpleRoom: ...
    def getRooms(self) -> typing.List[VASSAL.chat.Room]: ...
    def remove(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> typing.List[VASSAL.chat.Room]: ...
    def setDefaultRoomName(self, string: str) -> None: ...
    def update(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> typing.List[VASSAL.chat.Room]: ...

class RoomTracker:
    def __init__(self): ...
    def finalizeRoom(self, room: VASSAL.chat.Room) -> None: ...
    def getJoinedPlayers(self) -> java.util.Enumeration[VASSAL.chat.Player]: ...
    def getLeftPlayers(self) -> java.util.Enumeration[VASSAL.chat.Player]: ...
    def init(self, room: VASSAL.chat.Room) -> None: ...

class TextClient:
    def __init__(self, chatServerConnection: VASSAL.chat.ChatServerConnection): ...
    def getClient(self) -> VASSAL.chat.ChatServerConnection: ...
    @staticmethod
    def report(roomArray: typing.List[VASSAL.chat.Room]) -> str: ...
    class Encoder(VASSAL.command.CommandEncoder):
        def __init__(self): ...
        def decode(self, string: str) -> VASSAL.command.Command: ...
        def encode(self, command: VASSAL.command.Command) -> str: ...
    class ShowText(VASSAL.command.Command):
        def __init__(self, string: str): ...
        def getMessage(self) -> str: ...

class UnitTest(org.litesoft.p2pchat.UserDialog):
    def __init__(self, string: str): ...
    @staticmethod
    def main(stringArray: typing.List[str]) -> None: ...
    def setActivePeerManager(self, activePeerManager: org.litesoft.p2pchat.ActivePeerManager) -> None: ...
    def setPendingPeerManager(self, pendingPeerManager: org.litesoft.p2pchat.PendingPeerManager) -> None: ...
    def showCHAT(self, peerInfo: org.litesoft.p2pchat.PeerInfo, string: str) -> None: ...
    def showConnect(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showConnectFailed(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showDisconnect(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showHELO(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showNAME(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showPMSG(self, peerInfo: org.litesoft.p2pchat.PeerInfo, string: str) -> None: ...
    def showStreamsFailed(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def showUnrecognized(self, peerInfo: org.litesoft.p2pchat.PeerInfo, string: str) -> None: ...
    def toString(self) -> str: ...

class ClientTest(P2PClient, java.lang.Runnable, java.beans.PropertyChangeListener):
    def __init__(self, peerPool: PeerPool, welcomeMessageServer: typing.Union[VASSAL.chat.WelcomeMessageServer, typing.Callable], int: int, int2: int, fileWriter: java.io.FileWriter): ...
    def propertyChange(self, propertyChangeEvent: java.beans.PropertyChangeEvent) -> None: ...
    @staticmethod
    def report(roomArray: typing.List[VASSAL.chat.Room]) -> str: ...
    def run(self) -> None: ...

class DirectPeerPool(PeerPool, VASSAL.chat.ui.ChatControlsInitializer):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, properties: java.util.Properties): ...
    def connectFailed(self, peerInfo: org.litesoft.p2pchat.PeerInfo) -> None: ...
    def disconnect(self) -> None: ...
    def initComponents(self, p2PPlayer: P2PPlayer, pendingPeerManager: org.litesoft.p2pchat.PendingPeerManager) -> None: ...
    def initialize(self, p2PPlayer: P2PPlayer, pendingPeerManager: org.litesoft.p2pchat.PendingPeerManager) -> None: ...
    def initializeControls(self, chatServerControls: VASSAL.chat.ui.ChatServerControls) -> None: ...
    def uninitializeControls(self, chatServerControls: VASSAL.chat.ui.ChatServerControls) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("VASSAL.chat.peer2peer")``.

    AcceptPeerThread: typing.Type[AcceptPeerThread]
    ClientTest: typing.Type[ClientTest]
    DirectPeerPool: typing.Type[DirectPeerPool]
    EchoClient: typing.Type[EchoClient]
    IpWatch: typing.Type[IpWatch]
    P2PClient: typing.Type[P2PClient]
    P2PClientFactory: typing.Type[P2PClientFactory]
    P2PPlayer: typing.Type[P2PPlayer]
    PeerPool: typing.Type[PeerPool]
    PeerPoolInfo: typing.Type[PeerPoolInfo]
    RoomManager: typing.Type[RoomManager]
    RoomTracker: typing.Type[RoomTracker]
    TextClient: typing.Type[TextClient]
    UnitTest: typing.Type[UnitTest]
