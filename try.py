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

    def get_total(self):
        return self.__total_amount


# =========================

table = int(input("Masukkan nomor meja: "))
order = Order(table)

print("\n===== DAFTAR MENU =====")
for i, (nama, harga) in enumerate(order.menu.items(), start=1):
    print(f"{i}. {nama} - Rp {harga:,}".replace(",", "."))

pilihan = input("\nPilih menu (contoh: 1,2,3): ")

for nomor in pilihan.split(","):
    nomor = int(nomor.strip())

    nama_menu = list(order.menu.keys())[nomor - 1]
    order.add_menu(nama_menu)

print(f"\nTotal Tagihan Meja {order.table_number}")
print(f"Rp {order.get_total():,}".replace(",", "."))