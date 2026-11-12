from ..base import SchemaEnum


class DeliveryMethod(SchemaEnum):
    LOCKER_DELIVERY = "https://schema.org/LockerDelivery"
    ON_SITE_PICKUP = "https://schema.org/OnSitePickup"
    PARCEL_SERVICE = "https://schema.org/ParcelService"
