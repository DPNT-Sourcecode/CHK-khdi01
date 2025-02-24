

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {"A": 50, "B":30, "C":20, "D":15}
    offers = {"A": (3, 130), "B": (2,45)}


    if skus[0].isnumeric():
        return -1

    current_number = ""

    item_list = []
    for i in skus.upper():
        if i in prices.keys():
            if current_number != "":
                item_list.append(current_number)
                current_number = ""
            item_list.append(i)
        else:
            current_number += i
    
    item_list.append(i)

    items = item_list[::2]
    quantities = item_list[1::2]

    all_quantites_are_numbers_check = [i.isnumeric() for i in quantities]

    print(items)
    print(quantities)

    if (len(items) != len(quantities)) or False in all_quantites_are_numbers_check:
        return -1

    total = 0

    for item, n in zip(items,[int(i) for i in quantities]):
        if item in offers.keys():
            total += ((n // offers[item][0] * offers[item][1])) + ((n % offers[item][0]) * prices[item])
        else:
            total += (n * prices[item])

    return total

def test():
    checkout("A1B2C3D4")
    assert checkout("A1B2C3D4") == 200

print(checkout("A1B2C3D4"))


