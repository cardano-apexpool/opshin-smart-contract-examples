from opshin.ledger.interval import *


@dataclass
class PublishParams(PlutusData):
    owner: PubKeyHash
    deadline: POSIXTime
    info: int


@dataclass
class RefundRedeemer(PlutusData):
    pass


def validator(
        datum: PublishParams,
        redeemer: RefundRedeemer,
        context: ScriptContext
) -> None:

    assert contains(make_from(datum.deadline), context.tx_info.valid_range), "TX submitted too early!"
    assert datum.owner in context.tx_info.signatories, "Refund signature missing!"
