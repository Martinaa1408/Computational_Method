'''Exercise module Lanese
Write a Python program to manage a supermarket cash desk. The program
should handle customer transactions and generate a final bill.

Program Requirements

- Product Data: The program must read product information (code, name,
  price) from a file, containing one product per line as space
  separated fields. The name of this file should be provided as a
  command-line argument when running the program.

- Customer Session: A customer session starts when the program is run. It proceeds as follows:

  1) The user enters product codes (non-zero natural numbers) one by one.

  2) Information on the corresponding product is printed on the
  screen, and the product is added to the shopping basket.

  3) Entering the number 0 ends the current session.

- Bill Generation: When the session ends, the program must print on
  the screen a detailed bill. If a product was entered multiple times,
  it must appear as a single line on the bill with the total quantity
  and subtotal price. The order of items in the bill is not
  relevant. The total price for the entire basket is printed at the
  end of the bill.

- Session Control: After printing the bill, the program should ask the
  user if they want to start a new session or close the program.

Sample input file:

101 Apple 0.50
102 Bread 2.75
103 Milk 1.50
104 Eggs 3.25
201 ChickenBreast 8.99

Sample interaction:

--- Starting a new session ---
Enter product codes, or 0 to end.
Enter product code: 101
Added: Apple ($0.50)
Enter product code: 103
Added: Milk ($1.50)
Enter product code: 101
Added: Apple ($0.50)
Enter product code: 0
Session ended. Printing the bill.

--- Your Bill ---
Quantity        Product                  Subtotal
--------------------------------------------------
2               Apple                        1.00
1               Milk                         1.50
--------------------------------------------------
Total:                                       2.50
-------------------

Start a new session? (y/n): n
Closing the program. Thank you! '''

def read_products(filename):
    products = {}
    try:
        with open(filename) as reader:
            for line in reader:
                line = line.strip()
                if line == '':
                    continue
                parts = line.split()
                code = int(parts[0])
                name = parts[1]
                price = float(parts[2])
                products[code] = (name, price)
    except FileNotFoundError:
        exit()
    return products


def print_bill(products, basket):
    print('\n--- Your Bill ---')
    print('Quantity | Product | Subtotal')
    print('-------------------------------')

    total = 0.0

    for code in basket:
        qty = basket[code]
        name, price = products[code]
        subtotal = qty * price
        total += subtotal

        print(qty, '|', name, '|', subtotal)

    print('-------------------------------')
    print('Total:', total)
    print('-------------------------------')


def session(products):
    print('--- Starting a new session ---')
    print('Enter product codes, or 0 to end.')

    basket = {}

    while True:
        code_str = input('Enter product code: ').strip()

        if not code_str.isdigit():
            print('warning: invalid code')
            continue

        code = int(code_str)

        if code == 0:
            print('Session ended. Printing the bill.')
            print_bill(products, basket)
            break

        if code not in products:
            print('warning: product not found')
            continue

        name, price = products[code]
        print('Added:', name, '($', price, ')')

        basket[code] = basket.get(code, 0) + 1


def main():
    products = read_products(filename)

    while True:
        session(products)
        ans = input('Start a new session? (y/n): ').strip().lower()
        if ans != 'y':
            print('Closing the program. Thank you!')
            break


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        exit()
    filename = argv[1]
    main()

    
    
            