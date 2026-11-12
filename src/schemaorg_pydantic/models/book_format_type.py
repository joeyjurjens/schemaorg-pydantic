from ..base import SchemaEnum


class BookFormatType(SchemaEnum):
    AUDIOBOOK_FORMAT = "https://schema.org/AudiobookFormat"
    E_BOOK = "https://schema.org/EBook"
    GRAPHIC_NOVEL = "https://schema.org/GraphicNovel"
    HARDCOVER = "https://schema.org/Hardcover"
    PAMPHLET = "https://schema.org/Pamphlet"
    PAPERBACK = "https://schema.org/Paperback"
