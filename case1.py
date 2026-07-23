class TableOrder:
    def __init__(self, table_number: int, customer_name: str, addOnMenu: bool = False):
        self.table_number = table_number
        self.customer_name = customer_name
        self.addOnMenu = ["tahu", "tempe", "kerupuk"]
        self.__total_amount = 0.0  # Dibuat private agar tidak diubah langsung

    def add_item(self, item_price: float):
        if item_price <= 0:
            print("Harga item tidak valid!")
            return
        self.__total_amount += item_price

    def apply_discount(self, discount_percent: float):
        if 0 < discount_percent <= 100:
            discount_value = self.__total_amount * (discount_percent / 100)
            self.__total_amount -= discount_value

    def get_receipt_summary(self) -> str:
        formatted_price = f"{self.__total_amount:,.0f}".replace(",", ".")
        return f"[Meja {self.table_number}] {self.customer_name} - Total Tagihan: Rp {formatted_price}"

    def add_on_menu(self):
        if self.__total_amount < 100000:
            print(f"Selamat menikmati terimakasih")
            return
        print(f"Selamat menikmati {', '.join(self.addOnMenu)}")
        for i in range(len(self.addOnMenu)):
            print(f"{i + 1}. {self.addOnMenu[i]}")
        pilihan = int(input("Pilih menu tambahan (1-3): "))
        if 1 <= pilihan <= len(self.addOnMenu):
            print(f"Anda memilih {self.addOnMenu[pilihan - 1]}.")
        else:
            print("Pilihan tidak valid.")


# Testing
order1 = TableOrder(table_number=5, customer_name="Pak Budi")
order1.add_item(80000)  # Nasi Goreng
order1.add_item(20000)  # Es Teh Manis
order1.apply_discount(10) # Diskon Member 10%
order1.add_on_menu()
print(order1.get_receipt_summary())