import pytest
from credit_card_validator import CreditCardValidator

def test_validate_card_number():
    assert CreditCardValidator("4929537721266964") == "Valid"
    assert CreditCardValidator("4716111049662895") == "Valid"
    assert CreditCardValidator("5574552811652176") == "Valid"
    assert CreditCardValidator("370777153052423") == "Valid"
    assert CreditCardValidator("30569309025904") == "Valid"
    assert CreditCardValidator("35301113333000") == "Valid"
    assert CreditCardValidator("353011133330") == "Invalid"
    assert CreditCardValidator("1234-5678-9101-1") == "Invalid"
    assert CreditCardValidator("4111-1111112") == "Invalid"
    assert CreditCardValidator("6011-1117") == "Invalid"
