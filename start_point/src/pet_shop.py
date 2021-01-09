# WRITE YOUR FUNCTIONS HERE

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

