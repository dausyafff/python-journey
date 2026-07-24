class Order:
    # 1. Deklarasikan 'menu' di tingkat CLASS (Class Attribute)
    # Mirip public static $menu di PHP. BISA diakses oleh @classmethod maupun instance!
    menu = {
        "Nasi Goreng": 35000,
        "Es Teh Manis": 10000,
        "Mie Ayam Geprek": 30000
    }

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    def add_menu(self, item_name):
        if item_name in self.menu:
            self.__total_amount += self.menu[item_name]
            print(f"✅ {item_name} berhasil ditambahkan.")
        else:
            print("❌ Menu tidak tersedia.")

    @classmethod
    def bundling_promo(cls, bundling_items: list, discount_percentage: float):
        # Sekarang cls.menu BISA diakses dengan aman!
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
        return f"\n--- NOTA MEJA {self.table_number} ---\nPelanggan: {self.customer_name}\nTotal Tagihan: {formatted_total}"


# ==========================================
# JALANKAN PROGRAM
# ==========================================

customer1 = input("Masukkan nama pelanggan: ")
table1 = int(input("Masukkan nomor meja: "))

print("\n--- SILAKAN PILIH MENU ---")
# Mengakses Order.menu sekarang SUDAH BISA karena menu adalah Class Attribute
for pilih, (namaMenu, harga) in enumerate(Order.menu.items(), start=1):
    print(f"{pilih}. {namaMenu} - Rp {harga:,}".replace(",", "."))

order1 = ChooseOrder(table1, customer1)

# Pilihan menu oleh user (misal: "1,2")
pilihan = input("\nPilih menu (pisahkan dengan koma, contoh: 1,2): ")

daftar_menu_keys = list(Order.menu.keys()) # ['Nasi Goreng', 'Es Teh Manis', 'Mie Ayam Geprek']

for nomor in pilihan.split(","):
    nomor_int = int(nomor.strip())
    # Ambil nama menu berdasarkan nomor indeks (dikurangi 1)
    if 1 <= nomor_int <= len(daftar_menu_keys):
        nama_menu_dipilih = daftar_menu_keys[nomor_int - 1]
        order1.add_menu(nama_menu_dipilih)

# Cetak Nota
print(order1.print_receipt())