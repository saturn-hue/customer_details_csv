# csv module
import csv


with open('customer-details.csv', 'r') as customer_file:
    customer_csv = csv.reader(customer_file)

    # The Syntax below removed the header of customer_file
    # next(customer_file)

    for row in customer_file:
        print(row)

