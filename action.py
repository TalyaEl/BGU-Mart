from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            supplier_id = int(splittedline[2])
            date = splittedline[3]

            products = repo._products.find(id = product_id) #current quantity
            if not products:
                continue
            
            current_product = products[0]
            if quantity < 0:
                if current_product.quantity + quantity < 0:
                    continue #if there's not enough quantity

            new_quantity = current_product.quantity + quantity #supply arrival
            repo._conn.execute("""
                UPDATE products
                SET quantity = ?
                WHERE id = ?
                """, [new_quantity, product_id])
            
            activitie = Activitie(product_id, quantity, supplier_id, date)
            repo._activities.insert(activitie) #record
            #TODO: apply the action (and insert to the table) if possible

if __name__ == '__main__':
    main(sys.argv)