class Order:
    def __init__(self, order_id: str, total_amount: float):
        self.order_id = order_id
        self.total_amount = total_amount

    def get_total(self) -> float:
        return self.total_amount

    @staticmethod
    def format_rupiah(amount: float) -> str:
        return f"Rp {amount:,.0f}".replace(",", ".")

    def print_receipt(self) -> str:
        formatted = self.format_rupiah(self.get_total())
        return f"Nota [{self.order_id}] - Total: {formatted}"


class VIPOrder(Order):
    SERVICE_CHARGE_PERCENT = 5.0  # Class attribute

    def get_total(self) -> float:
        # Mengambil total dasar dari Parent via super()
        base_total = super().get_total()
        # Tambah Service Charge 5%
        service_fee = base_total * (self.SERVICE_CHARGE_PERCENT / 100)
        return base_total + service_fee

    # Class method sebagai Factory Method khusus Tamu Ulang Tahun
    @classmethod
    def create_birthday_vip(cls, order_id: str, base_amount: float):
        # Diskon Ultah 10%
        discounted_amount = base_amount * 0.90
        # cls(...) akan membuat instance dari VIPOrder
        return cls(order_id, discounted_amount)


# --- Test Cases ---

# 1. Order Reguler
order_biasa = Order("ORD-001", 100000)
print(order_biasa.print_receipt())
# Output: Nota [ORD-001] - Total: Rp 100.000

# 2. VIP Order (Otomatis + Charge 5%)
order_vip = VIPOrder("VIP-001", 100000)
print(order_vip.print_receipt())
# Output: Nota [VIP-001] - Total: Rp 105.000 (100rb + 5% service charge)

# 3. VIP Birthday Promo (Diskon 10% dulu, baru + Charge 5%)
order_ultah = VIPOrder.create_birthday_vip("VIP-BDAY", 100000)
print(order_ultah.print_receipt())
# Base: 100rb -> Diskon 10% = 90rb -> Service charge 5% dari 90rb = 4.500 -> Total: 94.500
# Output: Nota [VIP-BDAY] - Total: Rp 94.500