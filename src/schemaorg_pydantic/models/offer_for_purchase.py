from __future__ import annotations

from typing import ClassVar

from pydantic import Field

from .offer import Offer


class OfferForPurchase(Offer):
    """An [[OfferForPurchase]] in Schema.org represents an [[Offer]] to sell something, i.e. an [[Offer]] whose\n  [[businessFunction]] is [sell](http://purl.org/goodrelations/v1#Sell.). See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for\n  background on the underlying concepts."""
    schema_type: ClassVar[str] = "OfferForPurchase"
