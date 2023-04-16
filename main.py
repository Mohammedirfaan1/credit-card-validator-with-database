import os
from credit_card_validator import CreditCardValidator
from dotenv import load_dotenv
from mongo_db import MongoDB

MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")
MONGODB_COLLECTION_NAME = os.environ.get("MONGODB_COLLECTION_NAME")

#MONGODB_URI="mongodb://127.0.0.1:27017"
#MONGODB_NAME="card_numbers"
#MONGODB_COLLECTION_NAME="data"


def main():
    card_number = input("Enter credit card number: ")
    name = input("Enter name on card: ")
    validator = CreditCardValidator(card_number, name)
    if validator.validate():
        print("Valid!")
        mongo = MongoDB(MONGODB_URI, MONGODB_NAME, MONGODB_COLLECTION_NAME)
        mongo.insert_one(validator.to_dict())
    else:
        print("Invalid!")

if __name__ == "__main__":
    main()
