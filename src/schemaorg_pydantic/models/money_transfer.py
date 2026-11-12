from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING, Union

from pydantic import Field

from ..base import Is, Number, Ref, Text
from .transfer_action import TransferAction

if TYPE_CHECKING:
    from .bank_or_credit_union import BankOrCreditUnion
    from .monetary_amount import MonetaryAmount

if TYPE_CHECKING:
    BankOrCreditUnion_Text_Ref = Union[BankOrCreditUnion, Text, Ref]
else:
    BankOrCreditUnion_Text_Ref = Union[Is["BankOrCreditUnion"], Text, Ref]

if TYPE_CHECKING:
    MonetaryAmount_Number_Ref = Union[MonetaryAmount, Number, Ref]
else:
    MonetaryAmount_Number_Ref = Union[Is["MonetaryAmount"], Number, Ref]


class MoneyTransfer(TransferAction):
    """The act of transferring money from one place to another place. This may occur electronically or physically."""
    schema_type: ClassVar[str] = "MoneyTransfer"
    amount: MonetaryAmount_Number_Ref | list[MonetaryAmount_Number_Ref] | None = Field(default=None)
    beneficiary_bank: BankOrCreditUnion_Text_Ref | list[BankOrCreditUnion_Text_Ref] | None = Field(default=None, validation_alias="beneficiaryBank", serialization_alias="beneficiaryBank")
