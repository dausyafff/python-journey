# Python (Pola Odoo)
class Order:
    def __init__(self, amount: float):
        self.amount = amount

    def calculate_total(self) -> float:
        # Logika dasar Odoo
        return self.amount


class VIPOrder(Order):
    def calculate_total(self) -> float:
        # 1. Minta hasil perhitungan dari Class Induk (Parent)
        base_total = super().calculate_total()
        
        # 2. Tambahkan logika kustom kita (Diskon 10% Member)
        discount = base_total * 0.10
        final_total = base_total - discount
        
        return final_total

# Testing
pesanan_vip = VIPOrder(amount=100000)
print(pesanan_vip.calculate_total())  # Output: 90000.0