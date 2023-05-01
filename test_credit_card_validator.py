import pytest
from credit_card_validator import CreditCardValidator

def test_validate_card_number():
    # Arrange
    card_number = "4929537721266964"
    name = "Neymar"
    validator = CreditCardValidator(card_number, name)

    # Act
    result = validator.validate()

    # Assert
    assert result == True



