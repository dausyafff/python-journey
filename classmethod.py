class MenuItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
    
    def get_details(self):
        return f"{self.name} [{self.category}] - Rp {self.price:,.0f}".replace(",", ".")
    
item1 = MenuItem("Nasi Goreng", "Makanan", 15000)
print(item1.get_details())