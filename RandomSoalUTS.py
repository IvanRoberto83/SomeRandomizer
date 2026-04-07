import random

print("===== GACHA SOAL UTS =====")
print("Semoga Beruntung Yak, GWS!")

print("\nDaftar Soal:")
print("1. UTS1: Kasir Sederhana")
print("2. UTS2: Simulasi Summonhenge")
print("3. UTS3: Karyawan")
print("4. UTS4: Teyvat System")
print("5. UTS5: Logitrack")
print("6. UTS6: Rekam Medis")
print("7. UTS7: Digimon")

nim = input("\nMasukkan NIM Kamu: ")

seed = "UTS_PBO_2026"
random.seed(seed + nim)

soal = random.sample(range(1, 8), 2)

print("\nNIM:", nim)
print("Selamat! Kamu dapat soal:", soal)