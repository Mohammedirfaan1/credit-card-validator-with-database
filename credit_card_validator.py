def luhn_check(card_number):
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False

    digits = [int(x) for x in card_number]
    check = sum(digits[-1::-2])
    check += sum(sum(divmod(d * 2, 10)) for d in digits[-2::-2])
    return check % 10 == 0

class CreditCardValidator:
    def __init__(self, card_number, name):
        self.card_number = card_number
        self.name = name

    def validate(self):
        return luhn_check(self.card_number)

    def to_dict(self):
        return {"card_number": self.card_number, "name": self.name}

