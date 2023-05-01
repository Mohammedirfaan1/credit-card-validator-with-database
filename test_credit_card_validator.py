import pytest
from credit_card_validator import CreditCardValidator

def test_validate_card_number():
    assert CreditCardValidator("4929537721266964",name="Neymar") == "Valid"
    assert CreditCardValidator("4716111049662895","Mbappe") == "Valid"
    assert CreditCardValidator("5574552811652176","Ziyech") == "Valid"
    assert CreditCardValidator("370777153052423","Mosalah") == "Valid"
    assert CreditCardValidator("342658788906503","Kante") == "Valid"
    assert CreditCardValidator("374245455400126","Coutinho") == "Valid"
    assert CreditCardValidator("353011133330") == "Invalid"
    assert CreditCardValidator("1234-5678-9101-1") == "Invalid"
    assert CreditCardValidator("4111-1111112") == "Invalid"
    assert CreditCardValidator("6011-1117") == "Invalid"
