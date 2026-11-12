from ..base import SchemaEnum


class FulfillmentTypeEnumeration(SchemaEnum):
    FULFILLMENT_TYPE_COLLECTION_POINT = "https://schema.org/FulfillmentTypeCollectionPoint"
    FULFILLMENT_TYPE_DELIVERY = "https://schema.org/FulfillmentTypeDelivery"
    FULFILLMENT_TYPE_PICKUP_DROPOFF = "https://schema.org/FulfillmentTypePickupDropoff"
    FULFILLMENT_TYPE_PICKUP_IN_STORE = "https://schema.org/FulfillmentTypePickupInStore"
    FULFILLMENT_TYPE_SCHEDULED_DELIVERY = "https://schema.org/FulfillmentTypeScheduledDelivery"
