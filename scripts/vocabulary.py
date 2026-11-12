BASIC = {
    "Text": "Text",
    "URL": "Url",
    "Number": "Number",
    "Integer": "Integer",
    "Float": "Number",
    "Boolean": "Boolean",
    "Date": "Date",
    "DateTime": "DateTime",
    "Time": "Time",
}
TEXT_LIKE_ROOTS = {"schema:Text", "schema:Quantity"}


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def ids(value):
    return [item["@id"] for item in as_list(value)]


def plain(value):
    return value["@value"] if isinstance(value, dict) else value


class Vocabulary:
    def __init__(self, graph):
        self.nodes = {node["@id"]: node for node in graph}
        self.classes = {
            name: node
            for name, node in self.nodes.items()
            if "rdfs:Class" in as_list(node["@type"]) and name.startswith("schema:")
        }
        self.properties = {
            name: node
            for name, node in self.nodes.items()
            if "rdf:Property" in as_list(node["@type"]) and name.startswith("schema:")
        }
        self.parents = {
            name: [p for p in ids(node.get("rdfs:subClassOf")) if p in self.classes]
            for name, node in self.classes.items()
        }
        self.ancestor_cache = {}
        self.members = self.collect_members()
        self.own_properties = self.collect_own_properties()

    def collect_members(self):
        members = {}
        for name, node in self.nodes.items():
            kinds = set(as_list(node["@type"]))
            if name.startswith("schema:") and not {"rdfs:Class", "rdf:Property"} & kinds:
                for kind in kinds & self.classes.keys():
                    members.setdefault(kind, []).append(node)
        return members

    def collect_own_properties(self):
        own = {}
        for name, node in self.properties.items():
            if self.is_superseded(node):
                continue
            for domain in ids(node.get("schema:domainIncludes")):
                if domain in self.classes:
                    own.setdefault(domain, []).append(name)
        return own

    def is_superseded(self, node):
        return "schema:supersededBy" in node

    def ancestors(self, name):
        if name not in self.ancestor_cache:
            found = set()
            for parent in self.parents.get(name, []):
                found |= {parent} | self.ancestors(parent)
            self.ancestor_cache[name] = found
        return self.ancestor_cache[name]

    def short(self, name):
        return name.split(":", 1)[1]

    def kind(self, name):
        if self.short(name) in BASIC:
            return "basic"
        node = self.classes[name]
        if (
            "schema:DataType" in as_list(node["@type"])
            or name in TEXT_LIKE_ROOTS
            or self.ancestors(name) & TEXT_LIKE_ROOTS
        ):
            return "text"
        if "schema:Number" in self.ancestors(name):
            return "basic"
        return "class"

    def is_enumeration_class(self, name):
        return "schema:Enumeration" in self.ancestors(name) and self.kind(name) == "class"

    def is_enum(self, name):
        return (
            self.is_enumeration_class(name)
            and bool(self.members.get(name))
            and not self.own_properties.get(name)
            and not self.is_superseded(self.classes[name])
        )

    def enum_family(self, name):
        return [
            other
            for other in self.classes
            if self.is_enum(other) and (other == name or name in self.ancestors(other))
        ]

    def inherited_properties(self, name):
        found = set()
        for ancestor in self.ancestors(name):
            found |= set(self.own_properties.get(ancestor, []))
        return found

    def description(self, name):
        text = plain(self.classes[name].get("rdfs:comment", ""))
        return text.replace("\\n", "\n").split("\n\n")[0].strip().replace('"""', "'''")
