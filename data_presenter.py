open_file = open('CupcakeInvoices.csv')

for line in open_file:
    print(line)

open_file.seek(0)

for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[2])

open_file.seek(0)

for line in open_file:
    line = line.strip()
    values = line.split(",")
    cupcake_number = float(values[3])
    cupcake_price = float(values[4])
    invoice_total = cupcake_number * cupcake_price
    print(round(invoice_total, 2))

open_file.seek(0)

total_invoice = 0;

for line in open_file:
    line = line.strip()
    values = line.split(",")
    cupcake_number = float(values[3])
    cupcake_price = float(values[4])
    cupcake_invoice = cupcake_number * cupcake_price
    total_invoice += cupcake_invoice

grand_total = round(total_invoice, 2)

print(f'The grand total is ${grand_total}') #used dollar sign to appear in terminal
