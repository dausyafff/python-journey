class Siswa:
  def __init__(self, nilai):
    self._nilai = nilai

  @property
  def nilai(self): #ini getNilai()
    return self._nilai
  
  @nilai.setter
  def nilai(self, nilai):
    if nilai < 75:
      raise ValueError("Nilai tidak boleh kurang dari 75")
    self._nilai = nilai

s = Siswa(80)
print(s.nilai) #80
s.nilai = 90

# Intinya: @property = cara bikin method kelihatan dan dipakai kayak attribute, padahal di baliknya ada logic (validasi, perhitungan, dll).