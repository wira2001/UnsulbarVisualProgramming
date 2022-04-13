class Mahasiswa:

     def __init__(self, merk):
         self.__merk = merk
         
     def tampilkan_merk(self):
         print(f'Nama: {self.__merk}')
jip = Mahasiswa('Wira Pratidina Iptu Tahang Palle - D0219024')
jip.tampilkan_merk()
