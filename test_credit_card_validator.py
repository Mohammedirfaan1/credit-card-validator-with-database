import pytest
from credit_card_validator import CreditCardValidator

from credit_card_validator import CreditCardValidator

def test_validate_card_number():
    # Arrange
    cards = [("4929537721266964", "Neymar"),
             ("4716111049662895", "Mbappe"),
             ("5574552811652176", "Ziyech"),
             ("370777153052423", "Mosalah"),
             ("374245455400126", "Coutihno"),
             ("342658788906503", "Kante")
            ]

    # Act and Assert
    for card_number, name in cards:
        validator = CreditCardValidator(card_number, name)
        assert validator.validate() == True



