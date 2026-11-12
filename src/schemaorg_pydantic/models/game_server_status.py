from ..base import SchemaEnum


class GameServerStatus(SchemaEnum):
    OFFLINE_PERMANENTLY = "https://schema.org/OfflinePermanently"
    OFFLINE_TEMPORARILY = "https://schema.org/OfflineTemporarily"
    ONLINE = "https://schema.org/Online"
    ONLINE_FULL = "https://schema.org/OnlineFull"
