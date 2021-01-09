# WRITE YOUR FUNCTIONS HERE

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

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# # why not working???
# def add_or_remove_cash(pet_shop, value):
#     if value > 0:
#         return (get_total_cash(pet_shop)) + value
#     elif value < 0:
#         return (get_total_cash(pet_shop)) - value
#     else:
#         return None

def add_or_remove_cash(pet_shop, num):
    if num > 0:
        pet_shop["admin"]["total_cash"] += num
    else:
        pet_shop["admin"]["total_cash"] -= num

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# # def increase_pets_sold(dict, number):
# #     return dict["admin"]["pets_sold"] = dict["admin"]["pets_sold"] + number

def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# def get_pets_by_breed(pet_shop, breed):
#     pets_by_breed = 0
#     for pet in pet_shop:
#         if pet_shop["pets"][3]["breed"] == breed:
#             return len(pet_shop["pets"][3]["breed"])
#     return pets_by_breed

def get_pets_by_breed(pet_shop, breed):
    # return [pet for pet in pet_shop["pets"] if pet["breed"] == breed]
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

# print(get_pets_by_breed(cc_pet_shop, "British Shorthair"))

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None