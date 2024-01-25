def calculate_total(items_purchased, grocery_list):
    item_prices = {
        "milk": 2.50,
        "eggs": 3.25,
        "bread": 1.21,
        "cheese": 3.50,
        "apples": 7.44,
        "bananas": 3.88,
        "carrots": 3.89,
        "lettuce": 1.12,
        "potatoes": 32.21,
        "cereal": 5.99,
    }
        # Don't touch above this line
    not_found_items = []
    total_price = 0
    receipt = {}
    for item in grocery_list:
        if item not in items_purchased:
            not_found_items.append(item)
    for item in items_purchased:
        total_price += item_prices[item]
        receipt[item] = item_prices[item]
    return not_found_items, receipt, total_price