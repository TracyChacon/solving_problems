# Inventory Update

# Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

#     Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
#     Update items in the inventory by adding the quantity of any matching items from the shipment.
#     If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
#     Return inventory in the order it was given with new items at the end in the order they appear in the shipment.

# For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].


######################################################################
# Initial Solution
######################################################################
# def update_inventory(inventory: list[list], shipment: list[list]) -> list[list]:
#     inventory_details = {}
#     existing_item_order = 0
#     new_item_order = 0

#     for count, item in inventory:
#         if item in inventory_details:
#             inventory_details[item]['count'] += count
#         else:
#             existing_item_order += 1
#             inventory_details[item] = {
#                 'existing_item_order': existing_item_order,
#                 'new_item_order': 0,
#                 'count': count
#              }
    
#     length_existing_items = len(inventory_details)

#     for count, item in shipment:
#         if item in inventory_details:
#             inventory_details[item]['count'] += count
#         else:
#             new_item_order += 1
#             inventory_details[item] = {
#                 'existing_item_order': 0,
#                 'new_item_order': new_item_order,
#                 'count': count
#              }
    
#     updated_inventory = ["" for _ in range(len(inventory_details))]

#     for key in inventory_details:
#         if inventory_details[key]["existing_item_order"] > 0:
#             order_of_existing_item = inventory_details[key]["existing_item_order"] - 1
#             count_of_existing_item = inventory_details[key]["count"]
#             updated_inventory[order_of_existing_item] =  [count_of_existing_item, key]
#         else:
#             order_of_new_item = inventory_details[key]["new_item_order"]
#             count_of_new_item = inventory_details[key]['count']
#             updated_inventory[length_existing_items + order_of_new_item - 1] =  [count_of_new_item, key]

#     return updated_inventory


######################################################################
#  Readable Pythonic Solution
######################################################################
def update_inventory(inventory: list[list], shipment: list[list]) -> list[list]:
    update_inventory = {item: count for count, item in inventory}

    for count, item in shipment:
        if item in update_inventory:
            update_inventory[item] += count
        else:
            update_inventory[item] = count

    return [[count, item] for item, count in update_inventory.items()]

if __name__ == '__main__':
    #  Tests

    # Test 1 should return [[3, "apples"], [8, "bananas"]].
    print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]))
    # Test 2 should return [[3, "apples"], [8, "bananas"], [4, "oranges"]].
    print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]))
    # Test 3 should return [[10, "apples"], [30, "bananas"], [20, "oranges"]].
    print(update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]))
    # Test 4 should return [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]].
    print(update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))