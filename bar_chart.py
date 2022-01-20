open_file = open('CupcakeInvoices.csv')

import matplotlib.pyplot as plt

chocolate_number = 0
vanilla_number = 0
strawberry_number = 0

chocolate_invoice = 0
vanilla_invoice = 0
strawberry_invoice = 0

# Get data for number of invoices

for line in open_file:
    line = line.strip()
    values = line.split(",")
    if values[2] == 'Chocolate':
        chocolate_number += 1
    elif values[2] == 'Vanilla':
        vanilla_number += 1
    else:
        strawberry_number += 1 

open_file.seek(0)

# Get data for total invoices

for line in  open_file:
    line = line.strip()
    values = line.split(",")
    cupcake_price = float(values[4])
    cupcake_number = float(values[3])
    if values[2] == 'Chocolate':
        chocolate_invoice += cupcake_price * cupcake_number
    elif values[2] == 'Vanilla':
        vanilla_invoice += cupcake_price * cupcake_number
    else:
        strawberry_invoice += cupcake_price * cupcake_number

total_chocolate = round(chocolate_invoice, 2)
total_vanilla = round(vanilla_invoice, 2)
total_strawberry = round(strawberry_invoice, 2)

# print(total_chocolate)
# print(total_vanilla)
# print(total_strawberry)


# print(chocolate_number)
# print(vanilla_number)
# print(strawberry_number)


#plot Number of invoices graph

numbers = [chocolate_number, vanilla_number, strawberry_number]
labels = ['Chocolate', 'Vanilla', 'Strawberry']
pos = list(range(3))
# print(numbers)

def cupcakes_sold(numbers, labels, pos):
    plt.bar(pos, numbers, color='green')
    plt.xticks(ticks=pos, labels=labels)
    plt.xlabel('Flavors')
    plt.ylabel('Number of Invoices')
    plt.show()

cupcakes_sold(numbers, labels, pos)

open_file.seek(0)


#plot Invoice amounts graph

invoice_numbers = [total_chocolate, total_vanilla, total_strawberry]
# print(invoice_numbers)

def cupcakes_invoice(numbers, labels, pos):
    plt.bar(pos, numbers, color='blue')
    plt.xticks(ticks=pos, labels=labels)
    plt.xlabel('Flavors')
    plt.ylabel('Invoice Amount in Dollars')
    plt.show()

cupcakes_invoice(invoice_numbers, labels, pos)

open_file.close()