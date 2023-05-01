import pytest
from credit_card_validator import CreditCardValidator

def test_validate_card_number():
    validator = CreditCardValidator("4929537721266964", name="Neymar")
    assert validator.validate() == "Valid!"
    validator = CreditCardValidator("4716111049662895", name="Mbappe")
    assert validator.validate() == "Valid!"
    validator = CreditCardValidator("5574552811652176", name="Ziyech")
    assert validator.validate() == "Valid!"
    validator = CreditCardValidator("370777153052423", name="Mosalah")
    assert validator.validate() == "Valid!"
    validator = CreditCardValidator("342658788906503", name="Kante")
    assert validator.validate() == "Valid!"
    validator = CreditCardValidator("374245455400126", name="Coutihno")
    assert validator.validate() == "Valid!"
    validator = CreditCardValidator("3742454", name="pete")
    assert validator.validate() == "Valid!"
    validator = CreditCardValidator("545540012600000000", name="Copper")
    assert validator.validate() == "Valid!"
    validator = CreditCardValidator("07866_+0126", name="nop")
    assert validator.validate() == "Valid!"



