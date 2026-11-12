from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .offer import Offer


class OfferForLease(Offer):
    """An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something, i.e. an [[Offer]] whose\n  [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for\n  background on the underlying concepts."""
    schema_type: ClassVar[str] = "OfferForLease"
