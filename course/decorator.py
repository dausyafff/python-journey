from datetime import datetime

# 1. Membikin Decorator Kustom
def cek_dapur_buka(func):
    def wrapper(self, *args, **kwargs):
        jam_sekarang = datetime.now().hour
        
        # Misal dapur tutup jam 22 (10 malam)
        if jam_sekarang >= 22:
            print("❌ TRANSAKSI DITOLAK: Dapur restoran sudah tutup!")
            return None # Batalkan eksekusi fungsi
            
        # Jika masih buka, jalankan fungsi aslinya
        return func(self, *args, **kwargs)
    return wrapper


# 2. Penerapan Decorator pada Class Kasir
class KasirRestoran:
    def __init__(self, nama_kasir: str):
        self.nama_kasir = nama_kasir

    # Tempelkan decorator dengan tanda @
    @cek_dapur_buka
    def proses_pesanan(self, nama_menu: str):
        print(f"✅ Pesanan '{nama_menu}' berhasil diproses oleh {self.nama_kasir}.")


# Testing
kasir1 = KasirRestoran("Budi")
kasir1.proses_pesanan("Nasi Goreng Seafood")