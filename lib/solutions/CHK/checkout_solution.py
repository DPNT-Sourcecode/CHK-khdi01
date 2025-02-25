
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from collections import defaultdict

    #prices = {"A": 50, "B":30, "C":20, "D":15, "E":40, "F":10}

    #prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35,
    #          "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
    #          "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50}

    prices =  {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40,
               "F": 10, "G": 20, "H": 10, "I": 35, "J": 60,
               "K": 70, "L": 90, "M": 15, "N": 40, "O": 10,
               "P": 50, "Q": 30, "R": 50, "S": 20, "T": 20,
               "U": 40, "V": 50, "W": 20, "X": 17, "Y": 20,
               "Z": 21}

        
    offers = {"A": [(3, 130), (5,200)], "B": [(2,45)], "E": [(2, "B")], "F": [(3, "F")],
            "H": [(5, 45), (10, 80)], "K": [(2, 150)], "N": [(3, "M")], "P":[(5, 200)],
            "Q":[(3,80)], "R": [(3, "Q")], "U":[(4, "U")], "V":[(2,90),(3,130)]}

    group_discount_items = ["S", "T", "X", "Y", "Z"]
    group_discount = (3,45)

    if skus == "":
        return 0
    if not skus.isalpha():
        return -1

    cart_dict = defaultdict(int)
    for i in skus:
        if i in prices.keys():
            cart_dict[i] += 1
        else:
            return -1
    


    for item in cart_dict.keys():
        if (item in offers) and True in [isinstance(offer[1], str) for offer in offers.get(item, [])]:
            for quantity, free_item in [(q,f) for q,f in offers[item] if isinstance(f, str)]:
                if free_item in cart_dict and cart_dict[item] >= quantity:
                    num_free = cart_dict[item] // quantity
                    cart_dict[free_item] = max(0, cart_dict[free_item] - num_free)

    
    total = 0
    group_items = {}
    for item in group_discount_items:
        if item in cart_dict and cart_dict[item] > 0:
            group_items[item] = (cart_dict[item], prices[item])

            del cart_dict[item]
    
    if group_items != {}:

        group_item_list = []
        for item, (count, price) in group_items.items():
            group_item_list.extend([item] * count)

        group_item_list.sort(key=lambda x: prices[x], reverse=True)

        group_quantity, group_price = group_discount

        num_groups = len(group_item_list) // group_quantity

        if num_groups > 0:
            total += num_groups * group_price

        remaining = group_item_list[num_groups * group_quantity:]

        for item in group_items.keys():
            remaining_count = group_items[item] - remaining.count(item)
            total += remaining_count * prices[item]



    for item, n in cart_dict.items():
        item_total = 0

        if item in offers and True in (isinstance(offer[1], int) for offer in offers.get(item, [])):
            valid_offers = [(q,p) for q,p in offers[item] if isinstance(p, int)]

            valid_offers.sort(key=lambda x: x[0], reverse = True)

            remaining = n

            for quantity, price in valid_offers:
                if remaining >= quantity:
                    num_offers = remaining // quantity
                    item_total += num_offers * price
                    remaining -= num_offers * quantity

            if remaining > 0:
                item_total += remaining * prices[item]

        else:
            item_total = n * prices[item]
        
        total += item_total

    return total

def test():
    assert checkout("ABBCCCDDDD") == 215
    assert checkout("ABBBCCCDDDD") == 245
    assert checkout("ABCD") == 115
    assert checkout("A") == 50
    assert checkout("AAA") == 130
    assert checkout("") == 0
    assert checkout("1") == -1
    assert checkout("A1BB1C1D1") == -1
    assert checkout("A1BB1CC1D1") == -1
    assert checkout("A1B1C1D") == -1
    assert checkout("ABCa") == -1


    assert checkout("E") == 40
    assert checkout("EEB") == 80
    assert checkout("AAABBBEE") == 255
    assert checkout("AAAAAAAAA") ==  380

    assert checkout("FFF") == 20
    assert checkout("FFFFF") == 40
    assert checkout("EEBFFFFFF") == 120

    assert checkout("HHHHH") == 45
    assert checkout("HHHHHHHHHH") == 80
    assert checkout("HHH") == 30
    assert checkout("HHHHHHHH") == 75
    assert checkout("HHHHHHHHH") == 85

    assert checkout("K") == 70
    assert checkout("KK") == 120
    assert checkout("KKK") == 190

    assert checkout("NNNM") == 120
    assert checkout("NNM") == 95

    assert checkout("PPPPP") == 200
    assert checkout("PPPP") == 200

    assert checkout("QQQ") == 80
    assert checkout("QQ") == 60

    assert checkout("RRRQ") == 150
    assert checkout("RRQ") == 130

    assert checkout("UUUU") == 120
    assert checkout("UUU") == 120

    assert checkout("VV") == 90
    assert checkout("VVV") == 130
    assert checkout("VVVV") == 180
    assert checkout("VVVVV") == 220
    assert checkout("VVVVVV") == 260


    assert checkout("STX") == 45
    assert checkout("STXY") == 65
    assert checkout("ZZZ") ==45


    print("Tests Passed")

test()