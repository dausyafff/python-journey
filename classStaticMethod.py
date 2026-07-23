class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    # 1. Instance Method (Butuh 'self')
    def get_details(self) -> str:
        # Menggunakan static method di dalam instance method
        return f"{self.name} - {MenuItem.format_rupiah(self.price)}"

    # 2. Class Method (Butuh 'cls' - merujuk ke Class itu sendiri)
    # Di Odoo, ini mirip operasi yang bekerja di level Model (search, create batch, dll)
    @classmethod
    def create_promo_bundle(cls, bundle_name: str):
        # cls(...) sama dengan memanggil MenuItem(...)
        return cls(f"Paket Promo: {bundle_name}", 25000)

    # 3. Static Method (Tidak butuh 'self' maupun 'cls')
    # Pure Helper / Utility Function
    @staticmethod
    def format_rupiah(amount: float) -> str:
        return f"Rp {amount:,.0f}".replace(",", ".")


# --- Pemanggilan di Python ---

# Memanggil Static Method
print(MenuItem.format_rupiah(50000))  # Output: Rp 50.000

# Memanggil Class Method (Factory Pattern)
promo = MenuItem.create_promo_bundle("Paket Hemat Lunch")
print(promo.get_details())  # Output: Paket Promo: Paket Hemat Lunch - Rp 25.000