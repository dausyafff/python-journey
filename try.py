class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.menu = {
            "Nasi Goreng": 35000,
            "Es Teh Manis": 10000,
            "Mie Ayam Geprek": 30000
        }
        self.__total_amount = 0

    def add_menu(self, item_name):
        if item_name in self.menu:
            self.__total_amount = self.__total_amount + self.menu[item_name]
            print(f"{item_name} berhasil ditambahkan.")
        else:
            print("Menu tidak tersedia.")

    @classmethod
    def bundling_promo(cls, bundling_items: list, discount_percentage: float):
        total_price = sum(cls.menu[item] for item in bundling_items if item in cls.menu)
        discount_amount = total_price * (discount_percentage / 100)
        return total_price - discount_amount

    def get_total(self):
        return self.__total_amount

class ChooseOrder(Order):
    def __init__(self, table_number, customer_name):
        super().__init__(table_number)
        self.customer_name = customer_name

    def print_receipt(self):
        formatted_total = f"Rp {self.get_total():,}".replace(",", ".")
        return f"Nota Meja {self.table_number} - Total: {formatted_total} - Customer: {self.customer_name}"



customer1 = input("Masukkan nama pelanggan: ")
table1 = int(input("Masukkan nomor meja: "))
print("Silahkan Pilih Menu")
for pilih, (namaMenu, harga) in enumerate(Order.menu.items(), start=1):
    print(f"{pilih}, {namaMenu}, {harga}")


order1 = ChooseOrder(table1, customer1)

print(order1.print_receipt())










# =========================

# table = int(input("Masukkan nomor meja: "))
# order = Order(table)

# print("\n===== DAFTAR MENU =====")
# for i, (nama, harga) in enumerate(order.menu.items(), start=1):
#     print(f"{i}. {nama} - Rp {harga:,}".replace(",", "."))

# pilihan = input("\nPilih menu (contoh: 1,2,3): ")

# for nomor in pilihan.split(","):
#     nomor = int(nomor.strip())

#     nama_menu = list(order.menu.keys())[nomor - 1]
#     order.add_menu(nama_menu)

# print(f"\nTotal Tagihan Meja {order.table_number}")
# print(f"Rp {order.get_total():,}".replace(",", "."))