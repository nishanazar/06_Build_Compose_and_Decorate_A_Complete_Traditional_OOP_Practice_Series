class Product():
    def __init__(self, price):
        self._price = price


    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print("Price cannot be negative!")
        else:
            self._price = new_price

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(100)
print(p.price)   # Get price

p.price = 150    # Set new price
print(p.price)

del p.price # Delete price