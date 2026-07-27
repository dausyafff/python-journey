class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f"{self.name} ({MenuItem.format_rupiah(self.price)})"

    @staticmethod
    def format_rupiah(amount: float) -> str:
        return f"Rp {amount:,.0f}".replace(",", ".")


# Child Class 1: Makanan (Inherit dari MenuItem)
class FoodItem(MenuItem):
    def __init__(self, name: str, price: float, spicy_level: int):
        # super().__init__() menggantikan parent::__construct()
        super().__init__(name, price)
        self.spicy_level = spicy_level

    # Method Overriding / Polymorphism
    def get_info(self) -> str:
        # Panggil method parent via super()
        base_info = super().get_info()
        return f"{base_info} [Pedas Level {self.spicy_level}]"


# Child Class 2: Minuman (Inherit dari MenuItem)
class DrinkItem(MenuItem):
    def __init__(self, name: str, price: float, is_less_ice: bool = False):
        super().__init__(name, price)
        self.is_less_ice = is_less_ice

    def get_info(self) -> str:
        base_info = super().get_info()
        ice_note = "Less Ice" if self.is_less_ice else "Normal Ice"
        return f"{base_info} [{ice_note}]"


# Testing
es_teh = DrinkItem("Es Teh Manis", 5000, is_less_ice=True)
ayam_geprek = FoodItem("Ayam Geprek", 20000, spicy_level=5)

print(es_teh.get_info())      
# Output: Es Teh Manis (Rp 5.000) [Less Ice]

print(ayam_geprek.get_info()) 
# Output: Ayam Geprek (Rp 20.000) [Pedas Level 5]