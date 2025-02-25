

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from collections import defaultdict

    prices = {"A": 50, "B":30, "C":20, "D":15, "E":40, "F":10}
    offers = {"A": [(3, 130), (5,200)], "B": [(2,45)], "E": [(2, "B")], "F": [(3, "F")]}

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



    #for item, n in cart_dict.items():
    #    if item in offers.keys():
    #        total += ((n // offers[item][0] * offers[item][1])) + ((n % offers[item][0]) * prices[item])
    #    else:
    #        total += (n * prices[item])

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
    assert (checkout("1")) == -1
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

    print("Tests Passed")

#test()