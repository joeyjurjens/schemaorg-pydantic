from ..base import SchemaEnum


class MusicAlbumReleaseType(SchemaEnum):
    ALBUM_RELEASE = "https://schema.org/AlbumRelease"
    BROADCAST_RELEASE = "https://schema.org/BroadcastRelease"
    EP_RELEASE = "https://schema.org/EPRelease"
    SINGLE_RELEASE = "https://schema.org/SingleRelease"
