

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    from collections import defaultdict

    prices = {"A": 50, "B":30, "C":20, "D":15}
    offers = {"A": (3, 130), "B": (2,45)}

    if skus == "":
        return 0
    if not skus.isalpha():
        return -1

    #if len(skus) == 1:
    #    if skus in prices.keys():
    #        return prices[skus]
    #    else:
    #        return -1

    cart_dict = defaultdict(int)
    for i in skus:
        if i in prices.keys():
            cart_dict[i] += 1
        else:
            return -1
    
    total = 0

    for item, n in cart_dict.items():
        if item in offers.keys():
            total += ((n // offers[item][0] * offers[item][1])) + ((n % offers[item][0]) * prices[item])
        else:
            total += (n * prices[item])

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

test()