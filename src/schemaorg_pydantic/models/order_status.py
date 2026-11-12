from ..base import SchemaEnum


class OrderStatus(SchemaEnum):
    ORDER_CANCELLED = "https://schema.org/OrderCancelled"
    ORDER_DELIVERED = "https://schema.org/OrderDelivered"
    ORDER_IN_TRANSIT = "https://schema.org/OrderInTransit"
    ORDER_PAYMENT_DUE = "https://schema.org/OrderPaymentDue"
    ORDER_PICKUP_AVAILABLE = "https://schema.org/OrderPickupAvailable"
    ORDER_PROBLEM = "https://schema.org/OrderProblem"
    ORDER_PROCESSING = "https://schema.org/OrderProcessing"
    ORDER_RETURNED = "https://schema.org/OrderReturned"
