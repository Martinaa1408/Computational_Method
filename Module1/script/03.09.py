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

from sys import argv
input_file=open(argv[1],'r')
products=[]
for line in input_file:
    line=line.strip().split()
    code=int(line[0])
    name=line[1]
    price=float(line[2])
    if line=='':
        continue
    else:
        products.append((code,name,price))
input_file.close()
print(products)

basket=[]
while True:
    user=int(input('Enter product codes, or 0 to end:'))
    if user==0:
        print('Session ended. Printing the bill.')
        print('--- Your Bill ---')
        print('Quantity        Product                  Subtotal')
        print('--------------------------------------------------')
        total=0.0
        used=[]
        for code,name,price in basket:
            if code not in used:
                qty = 0
            for c_check,n_check,p_check in basket:
                if c_check==code:
                    qty+=1
            subtotal=qty*price
            total+=subtotal
            print(qty,'             ',name,'              ',subtotal,'\n')
        print('--------------------------------------------------')
        print('Total:',round(total))
        input('Start a new session? (y/n):').strip().lower()
        if input!='y':
            print('Closing the program. Thank you!')
        break

    for code,name,price in products:
        if user==code:
            print('Added',name,'($',price,')')
            basket.append((code,name,price))
