class Product(object):
    def __init__ (self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        print self.status
        return self
    def add_tax(self, var):
        tax = self.price * var
        price = tax + self.price
        print price
        return self
    def return_item(self, xReturn):
        if xReturn == "defective": 
            self.price = 0
            print self.price
        if xReturn == "unopened":
            self.status = "On sale!"
            print self.status
        if xReturn == "opened":
            discount = self.price * .20
            self.price = self.price - discount
            print self.price
        return self
    def display_info(self):
        print self.price, self.item_name, self.weight,"lbs", self.brand, self.status
        return self    
product1 = Product(100, "Expensive Shirt", 0.5, "Hugo Boss", "")
product1.return_item("opened").display_info()
