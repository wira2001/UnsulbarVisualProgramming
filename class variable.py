class transportasi():
    motor = "Scoopy"

    def __init__(self, input_nama):
        self.nama = input_nama #public
kendaraan = transportasi("Motor Scoopy")

print(transportasi.motor)
print(kendaraan.motor)
