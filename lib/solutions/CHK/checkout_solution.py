

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {"A": 50, "B":30, "C":20, "D":15}
    offers = {"A": (3, 130), "B": (2,45)}

    if skus == "":
        return -1
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
    assert checkout("A1B2C3D4") == 215
    assert checkout("A1B3C3D4") == 245
    assert checkout("A1B1C1D1") == 115
    assert checkout("A1") == 50
    assert checkout("A3") == 130
    assert checkout("") == -1
    assert (checkout("1A")) == -1
    assert checkout("A1BB1C1D1") == -1
    assert checkout("A1BB1CC1D1") == -1
    assert checkout("A1B1C1D") == -1



