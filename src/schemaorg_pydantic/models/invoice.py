from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Date, DateTime, Is, Ref, Text
from .intangible import Intangible
from .payment_status_type import PaymentStatusType
from .physical_activity_category import PhysicalActivityCategory

if TYPE_CHECKING:
    from .category_code import CategoryCode
    from .monetary_amount import MonetaryAmount
    from .order import Order
    from .organization import Organization
    from .payment_method import PaymentMethod
    from .person import Person
    from .price_specification import PriceSpecification
    from .thing import Thing

if TYPE_CHECKING:
    R88d1e012 = Union[CategoryCode, PhysicalActivityCategory, Thing, Text, Ref]
else:
    R88d1e012 = Union[Is["CategoryCode"], PhysicalActivityCategory, Is["Thing"], Text, Ref]

Date_DateTime = Union[Date, DateTime]
if TYPE_CHECKING:
    MonetaryAmount_PriceSpecification_Ref = Union[MonetaryAmount, PriceSpecification, Ref]
else:
    MonetaryAmount_PriceSpecification_Ref = Union[Is["MonetaryAmount"], Is["PriceSpecification"], Ref]

if TYPE_CHECKING:
    Order_Ref = Union[Order, Ref]
else:
    Order_Ref = Union[Is["Order"], Ref]

if TYPE_CHECKING:
    Organization_Person_Ref = Union[Organization, Person, Ref]
else:
    Organization_Person_Ref = Union[Is["Organization"], Is["Person"], Ref]

if TYPE_CHECKING:
    PaymentMethod_Text_Ref = Union[PaymentMethod, Text, Ref]
else:
    PaymentMethod_Text_Ref = Union[Is["PaymentMethod"], Text, Ref]

PaymentStatusType_Text = Union[PaymentStatusType, Text]

class Invoice(Intangible):
    """A statement of the money due for goods or services; a bill."""
    schema_type: ClassVar[str] = "Invoice"
    account_id: Text | list[Text] | None = Field(default=None, validation_alias="accountId", serialization_alias="accountId")
    billing_period: Text | list[Text] | None = Field(default=None, validation_alias="billingPeriod", serialization_alias="billingPeriod")
    broker: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    category: R88d1e012 | list[R88d1e012] | None = Field(default=None)
    confirmation_number: Text | list[Text] | None = Field(default=None, validation_alias="confirmationNumber", serialization_alias="confirmationNumber")
    customer: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    minimum_payment_due: MonetaryAmount_PriceSpecification_Ref | list[MonetaryAmount_PriceSpecification_Ref] | None = Field(default=None, validation_alias="minimumPaymentDue", serialization_alias="minimumPaymentDue")
    payment_due_date: Date_DateTime | list[Date_DateTime] | None = Field(default=None, validation_alias="paymentDueDate", serialization_alias="paymentDueDate")
    payment_method: PaymentMethod_Text_Ref | list[PaymentMethod_Text_Ref] | None = Field(default=None, validation_alias="paymentMethod", serialization_alias="paymentMethod")
    payment_method_id: Text | list[Text] | None = Field(default=None, validation_alias="paymentMethodId", serialization_alias="paymentMethodId")
    payment_status: PaymentStatusType_Text | list[PaymentStatusType_Text] | None = Field(default=None, validation_alias="paymentStatus", serialization_alias="paymentStatus")
    provider: Organization_Person_Ref | list[Organization_Person_Ref] | None = Field(default=None)
    references_order: Order_Ref | list[Order_Ref] | None = Field(default=None, validation_alias="referencesOrder", serialization_alias="referencesOrder")
    scheduled_payment_date: Date | list[Date] | None = Field(default=None, validation_alias="scheduledPaymentDate", serialization_alias="scheduledPaymentDate")
    total_payment_due: MonetaryAmount_PriceSpecification_Ref | list[MonetaryAmount_PriceSpecification_Ref] | None = Field(default=None, validation_alias="totalPaymentDue", serialization_alias="totalPaymentDue")
