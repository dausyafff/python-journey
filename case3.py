class BaseRestaurantOrder:
    def __init__(self, order_id: str, items: list):
        self.order_id = order_id
        self.items = items  # List of dict: [{'name': 'Nasi', 'price': 10000}]

    def process_checkout(self) -> float:
        """Hitung total biaya semua item"""
        total = sum(item['price'] for item in self.items)
        print(f"--- [BaseOrder {self.order_id}] Processing total: Rp {total:,.0f} ---")
        return total


class OdooRestaurantOrderCustom(BaseRestaurantOrder):
    """
    Simulasi modul kustom kita yang meng-INHERIT BaseOrder bawaan restoran
    """
    def process_checkout(self) -> float:
        # 1. Panggil logika hitung dasar milik Parent via super()
        base_total = super().process_checkout()
        
        # 2. Tambahkan PB1 / Pajak Restoran 10%
        tax = base_total * 0.10
        grand_total = base_total + tax
        
        print(f"--- [Custom Module] Added PB1 Tax 10%: Rp {tax:,.0f} ---")
        print(f"--- Grand Total Final: Rp {grand_total:,.0f} ---")
        
        return grand_total


# --- EXECUTION ---
pesanan_meja_5 = OdooRestaurantOrderCustom(
    order_id="MEJA-05", 
    items=[
        {'name': 'Steak Wagyu', 'price': 120000},
        {'name': 'Es Lemon Tea', 'price': 15000}
    ]
)

pesanan_meja_5.process_checkout()

# Output Log:
# --- [BaseOrder MEJA-05] Processing total: Rp 135.000 ---
# --- [Custom Module] Added PB1 Tax 10%: Rp 13.500 ---
# --- Grand Total Final: Rp 148.500 ---