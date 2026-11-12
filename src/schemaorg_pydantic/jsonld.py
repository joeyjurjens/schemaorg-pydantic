from __future__ import annotations

import datetime as dt
import json
from decimal import Decimal
from typing import Any

from pydantic.fields import FieldInfo

from .base import Node, Ref, SchemaEnum

CONTEXT = "https://schema.org"
FIRST = ["name", "url", "headline", "description", "image", "logo"]


class GraphConflict(ValueError):
    pass


class JsonLd:
    @classmethod
    def encode(cls, node: Node) -> dict[str, Any]:
        return {"@context": CONTEXT, **cls.encode_node(node)}

    @classmethod
    def dumps(cls, node: Node, **options: Any) -> str:
        return json.dumps(cls.encode(node), **options)

    @classmethod
    def script(cls, document: dict[str, Any]) -> str:
        text = json.dumps(document, ensure_ascii=False, indent=2)
        text = text.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
        return f'<script type="application/ld+json">{text}</script>'

    @classmethod
    def encode_node(
        cls, node: Node, graph: Graph | None = None, root: bool = True
    ) -> dict[str, Any]:
        if graph is not None and node.id and not root:
            graph.register(node)
            return {"@id": node.id}
        out: dict[str, Any] = {"@type": node.schema_type}
        if node.id:
            out["@id"] = node.id
        for name, field in cls.ordered_fields(node):
            if name == "id":
                continue
            value = cls.encode_value(getattr(node, name), graph)
            if not cls.is_empty(value):
                out[field.serialization_alias or name] = value
        return out

    @classmethod
    def encode_value(cls, value: Any, graph: Graph | None = None) -> Any:
        if isinstance(value, Node):
            return cls.encode_node(value, graph, root=False)
        if isinstance(value, Ref):
            return {"@id": value.id}
        if isinstance(value, SchemaEnum):
            return value.value
        if isinstance(value, Decimal):
            as_float = float(value)
            return as_float if Decimal(repr(as_float)) == value else str(value)
        if isinstance(value, (dt.datetime, dt.date, dt.time)):
            return value.isoformat()
        if isinstance(value, list):
            items = [cls.encode_value(item, graph) for item in value]
            return [item for item in items if not cls.is_empty(item)]
        return value

    @classmethod
    def ordered_fields(cls, node: Node) -> list[tuple[str, FieldInfo]]:
        def position(item: tuple[str, FieldInfo]) -> int:
            return FIRST.index(item[0]) if item[0] in FIRST else len(FIRST)

        return sorted(type(node).model_fields.items(), key=position)

    @staticmethod
    def is_empty(value: Any) -> bool:
        return value is None or value == "" or value == [] or value == {}


class Graph:
    def __init__(self, *nodes: Node) -> None:
        self.nodes: dict[str, dict[str, Any]] = {}
        self.anonymous: list[dict[str, Any]] = []
        for node in nodes:
            self.add(node)

    def add(self, node: Node) -> None:
        if node.id and node.id not in self.nodes:
            self.nodes[node.id] = {}
        data = JsonLd.encode_node(node, self)
        if not node.id:
            self.anonymous.append(data)
        elif self.nodes[node.id]:
            self.nodes[node.id] = self.merge(self.nodes[node.id], data)
        else:
            self.nodes[node.id] = data

    def register(self, node: Node) -> None:
        if node.id and node.id not in self.nodes:
            self.add(node)

    def merge(self, first: dict[str, Any], second: dict[str, Any]) -> dict[str, Any]:
        merged = dict(first)
        for key, value in second.items():
            if key in merged and merged[key] != value:
                raise GraphConflict(
                    f"{first.get('@id')}: {key} differs: {merged[key]!r} vs {value!r}"
                )
            merged[key] = value
        return merged

    def encode(self) -> dict[str, Any]:
        return {"@context": CONTEXT, "@graph": list(self.nodes.values()) + self.anonymous}

    def dumps(self, **options: Any) -> str:
        return json.dumps(self.encode(), **options)

    def script(self) -> str:
        return JsonLd.script(self.encode())
