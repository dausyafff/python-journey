class Siswa:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur
  def get_details(self):
    return f"{self.nama} - {self.umur} tahun"
  
rama = Siswa("Rama", 17)
indra = Siswa("Indra", 18)
print(rama.get_details())
print(indra.get_details())