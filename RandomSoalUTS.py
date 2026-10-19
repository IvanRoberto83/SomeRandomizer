import random

NIMMaster = [
    71241086, 71241113, 71241118, 71241157, 71251173,
    71251177, 71251181, 71251182, 71251186, 71251190,
    71251192, 71251198, 71251199, 71251208, 71251210,
    71251211, 71251212, 71251213, 71251218, 71251224,
    71251225, 71251226, 71251227, 71251228, 71251232
]

SoalMudah = [
    "UTS1: Gacha History Tracker",
    "UTS2: Fantasy Quest Manager",
    "UTS3: Election Konoha"
]

SoalSulit = [
    "UTS4: DwTix Aplikasi Tiket Japfest UKDW",
    "UTS5: Angkringan Mas Anton",
    "UTS6: Halloween"
]

print("===== GACHA SOAL UTS =====")

print("\nDaftar Soal Mudah:")
print("1. UTS1: Gacha History Tracker")
print("2. UTS2: Fantasy Quest Manager")
print("3. UTS3: Election Konoha")

print("\nDaftar Soal Sulit:")
print("4. UTS4: DwTix Aplikasi Tiket Japfest UKDW")
print("5. UTS5: Angkringan Mas Anton")
print("6. UTS6: Halloween\n")

seed = "GACOR KANG"
soal = ""

for i in range(len(NIMMaster)):
    nim = NIMMaster[i]
    random.seed(seed + str(nim))
    soalMudah = random.sample(range(1, 4), 1)
    soalSulit = random.sample(range(4, 7), 1)
    soal = soalMudah + soalSulit
    print("NIM:", nim, "mendapat soal:", soal)
    soal = ""
