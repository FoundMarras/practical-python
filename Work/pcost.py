# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(name):
    f = open(name,"rt")

    total = 0
    next(f)
    for line in f:
        row = line.split(",")
        if(len(row) > 1):
            try:
                shares = row[1]
                price = row[2]
                total += float(price) * float(shares)
            except ValueError:
                print(f"shares of {row[0]} is missing")
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)