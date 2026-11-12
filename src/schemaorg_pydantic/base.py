import datetime as dt
from decimal import Decimal
from enum import Enum
from typing import Annotated, Any, ClassVar
from urllib.parse import urlparse

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, PlainValidator


def check_url(value: str) -> str:
    parts = urlparse(value)
    if parts.scheme in ("http", "https") and parts.netloc:
        return value
    if parts.scheme in ("mailto", "tel") and parts.path:
        return value
    raise ValueError(f"not an absolute URL: {value!r}")


def check_date(value: str) -> str:
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"not an ISO 8601 date: {value!r}") from None
    return value


def check_datetime(value: str) -> str:
    try:
        dt.datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        raise ValueError(f"not an ISO 8601 date and time: {value!r}") from None
    return value


def check_time(value: str) -> str:
    try:
        dt.time.fromisoformat(value)
    except ValueError:
        raise ValueError(f"not an ISO 8601 time: {value!r}") from None
    return value


Text = str
Url = Annotated[str, AfterValidator(check_url)]
Number = int | float | Decimal
Integer = int
Boolean = bool
Date = dt.date | Annotated[str, AfterValidator(check_date)]
DateTime = dt.datetime | Annotated[str, AfterValidator(check_datetime)]
Time = dt.time | Annotated[str, AfterValidator(check_time)]


class Is:
    def __class_getitem__(cls, name: str) -> Any:
        prefix = f"{__package__}.models."

        def check(value: Any) -> Any:
            for klass in type(value).__mro__:
                if klass.__name__ == name and klass.__module__.startswith(prefix):
                    return value
            raise ValueError(f"expected an instance of {name}, got {type(value).__name__}")

        return Annotated[Any, PlainValidator(check)]


class SchemaEnum(str, Enum):
    pass


class Ref(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", populate_by_name=True)
    id: str = Field(validation_alias="@id", serialization_alias="@id")


class Node(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        populate_by_name=True,
        validate_assignment=True,
        defer_build=True,
    )
    schema_type: ClassVar[str] = "Thing"
    id: str | None = Field(default=None, validation_alias="@id", serialization_alias="@id")

    def ref(self) -> Ref:
        if not self.id:
            raise ValueError(f"{type(self).__name__} has no @id to reference")
        return Ref(id=self.id)

    def to_jsonld(self) -> dict[str, Any]:
        from .jsonld import JsonLd

        return JsonLd.encode(self)

    def to_script(self) -> str:
        from .jsonld import JsonLd

        return JsonLd.script(JsonLd.encode(self))
