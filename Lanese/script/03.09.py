from sys import argv

def load_products(fname):
    prods = []  #  (code, name, price)
    f = open(fname, "r")
    for line in f:
        parts = line.strip().split()
        code = parts[0]
        name = parts[1]
        price = float(parts[2])
        prods.append((code, name, price))
    f.close()
    return prods

def find_product(prods, code):
    for p in prods:
        if p[0] == code:
            return p
    return None

def print_bill(basket):
    total = 0
    print("\n--- BILL ---")
    for item in basket:
        code, name, price, qty = item
        sub = qty * price
        total += sub
        print(qty, name, sub)
    print("TOTAL:", total)

def main():
    fname = argv[1]
    prods = load_products(fname)

    while True:
        print("\n--- New Session ---")
        basket = []  # (code, name, price, qty)

        while True:
            c = input("Code (0=end): ").strip()
            if c == "0":
                break

            prod = find_product(prods, c)
            if prod is None:
                print("Unknown code.")
                continue

            found = False
            for item in basket:
                if item[0] == c:
                    item[3] += 1
                    found = True
                    break

            if not found:
                code, name, price = prod
                basket.append([code, name, price, 1])

            print("Added:", prod[1])

        print_bill(basket)

        again = input("New session? (y/n): ").strip().lower()
        if again != "y":
            break

main()
