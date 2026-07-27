class RestaurantItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = 0.0  # Private attribute (dua underscore)
        self.set_price(price)

    # Setter dengan validasi
    def set_price(self, price: float):
        if price < 0:
            raise ValueError("Harga tidak boleh minus!")
        self.__price = price

    # Getter
    def get_price(self) -> float:
        return self.__price

    # Method menghitung harga + Tax (PB1 Restoran 10%)
    def get_price_with_tax(self, tax_percent: float = 10.0) -> float:
        return self.__price + (self.__price * (tax_percent / 100))