from ..base import SchemaEnum


class DigitalDocumentPermissionType(SchemaEnum):
    COMMENT_PERMISSION = "https://schema.org/CommentPermission"
    READ_PERMISSION = "https://schema.org/ReadPermission"
    WRITE_PERMISSION = "https://schema.org/WritePermission"
