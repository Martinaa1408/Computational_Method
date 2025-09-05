from sys import argv

def read_products(filename):
    products = []
    try:
        file = open(filename, 'r')
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) >= 3:
                    code = parts[0]
                    name = ' '.join(parts[1:-1])
                    price_str = parts[-1]
                    try:
                        price = float(price_str)
                        products.append((code, name, price))
                    except:
                        pass
        file.close()
    except:
        print("Error: Cannot read file '" + filename + "'")
        exit(1)
    return products

def find_product(products, code):
    for product in products:
        if product[0] == code:
            return product
    return None

def process_session(products):
    basket = []
    print("\n--- Starting a new session ---")
    print("Enter product codes, or 0 to end.")
    
    while True:
        code = input("Enter product code: ").strip()
        if code == '0':
            break
        
        product = find_product(products, code)
        if product is None:
            print("Invalid product code. Please try again.")
            continue
        
        code, name, price = product
        
        # Check if product already in basket
        found = False
        for i in range(len(basket)):
            if basket[i][0] == code:
                basket[i] = (basket[i][0], basket[i][1], basket[i][2], basket[i][3] + 1)
                found = True
                break
        
        if not found:
            basket.append((code, name, price, 1))
        
        print("Added: " + name + " ($" + str(price) + ")")
    
    print("Session ended. Printing the bill.\n")
    return basket

def generate_bill(basket):
    print("--- Your Bill ---")
    print("Quantity        Product                  Subtotal")
    print("--------------------------------------------------")
    
    total = 0.0
    for item in basket:
        code, name, price, quantity = item
        subtotal = quantity * price
        total += subtotal
        
        # Format quantity
        qty_str = str(quantity)
        while len(qty_str) < 15:
            qty_str += " "
        
        # Format name
        name_str = name
        if len(name_str) > 25:
            name_str = name_str[:22] + "..."
        while len(name_str) < 25:
            name_str += " "
        
        # Format subtotal
        subtotal_str = str(subtotal)
        if '.' in subtotal_str:
            parts = subtotal_str.split('.')
            if len(parts[1]) == 1:
                subtotal_str += "0"
        else:
            subtotal_str += ".00"
        
        while len(subtotal_str) < 8:
            subtotal_str = " " + subtotal_str
        
        print(qty_str + " " + name_str + " " + subtotal_str)
    
    print("--------------------------------------------------")
    
    # Format total
    total_str = str(total)
    if '.' in total_str:
        parts = total_str.split('.')
        if len(parts[1]) == 1:
            total_str += "0"
    else:
        total_str += ".00"
    
    spaces = ""
    for i in range(40 - len(total_str)):
        spaces += " "
    
    print("Total:" + spaces + total_str)
    print("-------------------\n")

def main():
    if len(argv) != 2:
        print("Usage: python supermarket.py <products_file>")
        exit(1)
    
    products_file = argv[1]
    products = read_products(products_file)
    
    while True:
        basket = process_session(products)
        if basket:
            generate_bill(basket)
        
        response = input("Start a new session? (y/n): ").strip().lower()
        if response != 'y':
            break
    
    print("Closing the program. Thank you!")

if __name__ == "__main__":
    main()
