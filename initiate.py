from persistence import *

import sys
import os

def add_branche(splittedline : list[str]):
    branche = Branche(int(splittedline[0]), splittedline[1], int(splittedline[2])) #id, location and num of employees
    repo._branches.insert(branche)

def add_supplier(splittedline : list[str]):
    supplier = Supplier(int(splittedline[0]), splittedline[1], splittedline[2])
    repo._suppliers.insert(supplier)

def add_product(splittedline : list[str]):
    product = Product(int(splittedline[0]), splittedline[1], float(splittedline[2]), int(splittedline[3]))
    repo._products.insert(product)

def add_employee(splittedline : list[str]):
    employee = Employee(int(splittedline[0]), splittedline[1], float(splittedline[2]), int(splittedline[3]))
    repo._employees.insert(employee)

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:]) #gives the relevant function the arguments

if __name__ == '__main__':
    main(sys.argv)