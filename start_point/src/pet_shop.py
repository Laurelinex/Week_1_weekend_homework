# WRITE YOUR FUNCTIONS HERE

# Note: the tests are reset (setup method), not running in any partciular order, so no
# one test has any impact on another, ie if you struggle with one test feel free to skip it
# and work on another :)

### GOOD RULE OF THUMB: if function is to get or find sth, needs to return
### but to remove create or add, ie modifie sth: no return needed

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# # why not working >>> BECAUSE RETURN AND - and - is +
# def add_or_remove_cash(pet_shop, value):
#     if value > 0:
#         return (get_total_cash(pet_shop)) + value
#     elif value < 0:
#         return (get_total_cash(pet_shop)) - value
#     else:
#         return None

#IMPORTANT:  if not new variable in test, no need to return anything

def add_or_remove_cash(pet_shop, amount):
        pet_shop["admin"]["total_cash"] += amount

# This cannot work by calling previous function because it returns a value:
# def add_or_remove_cash(pet_shop, amount):
#     get_total_cash(pet_shop) += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# # def increase_pets_sold(dict, number):
# #     return dict["admin"]["pets_sold"] = dict["admin"]["pets_sold"] + number

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    # return [pet for pet in pet_shop["pets"] if pet["breed"] == breed]
    found_breeds = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_breeds.append(pet)
            # not .append(pet["i"]), best practise to bring back...
            # ...the full object to have access to everything we might need later on
    return found_breeds

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None 
    # above line is optional because Python does that by default

def remove_pet_by_name(pet_shop, name):
#IMPORTANT: you can't remove in a loop because of indexes:
    # for pet in pet_shop["pets"]:
    #     if pet["name"] == name:
    #         pet_shop["pets"].remove(pet)
    pet_to_remove = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_remove)

    # OR this also works but less straightforward:
    # index_of_pet = pet_shop["pets"].index(pet_to_remove)
    # pet_shop["pets"].pop(index_of_pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    # if customer["cash"] >= pet["price"]:
    #     return True
    # else:
    #     return False
# OR shorthand way of doing it, instead of an if statement that returns True or False,
# + best practise
    return customer["cash"] >= pet["price"]

# IMPORTANT: if you're checking anything that's None, do it first or the test will break
# should the function check for sth on sth that's None:
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
        add_or_remove_cash(pet_shop, pet["price"])
        remove_pet_by_name(pet_shop, pet["name"])
        remove_customer_cash(customer, pet["price"])

