# WRITE YOUR FUNCTIONS HERE

customers = [
    {
        "name": "Alice",
        "pets": [],
        "cash": 1000
    },
    {
        "name": "Bob",
        "pets": [],
        "cash": 50
    },
    {
        "name": "Jack",
        "pets": [],
        "cash": 100
    }
    ]

new_pet = {
    "name": "Bors the Younger",
    "pet_type": "cat",
    "breed": "Cornish Rex",
    "price": 100
}

cc_pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}

def get_pet_shop_name(dict):
    return cc_pet_shop["name"]

def get_total_cash(dict):
    return cc_pet_shop["admin"]["total_cash"]

# why not working???
def add_or_remove_cash(dict, value):
    if value > 0:
        return (get_total_cash(cc_pet_shop)) + value
    if value < 0:
        return (get_total_cash(cc_pet_shop)) - value
    else:
        return None

# print(get_total_cash(cc_pet_shop))
# print(add_or_remove_cash(cc_pet_shop, 10))

def get_pets_sold(dict):
    return cc_pet_shop["admin"]["pets_sold"]

