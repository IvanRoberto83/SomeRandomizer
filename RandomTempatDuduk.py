import random
import time

NIMMaster = [
    71190489, 71210736, 71231001, 71231025, 71231043, 71231064,
    71241071, 71241072, 71241078, 71241081, 71241082, 71241084,
    71241087, 71241090, 71241091, 71241093, 71241095, 71241106,
    71241107, 71241108, 71241110, 71241114, 71241116, 71241119,
    71241122, 71241123, 71241129, 71241136, 71241144, 71241147,
    71241150, 71241151, 71241156, 71241158, 71241161, 71241168
]

random.seed(int(time.strftime("%S")) * int(time.strftime("%M")))

NIM = NIMMaster.copy()
listBaru = []
rand1 = int(time.strftime("%S"))
rand2 = int(time.strftime("%M"))
rand3 = int(time.strftime("%H"))
rand4 = int(random.randint(1,999))
randlist = [rand1,rand2,rand3,rand4]
randfase21 = random.choice(randlist)+1
randfase22 = random.choice(randlist)+1
randfase23 = random.choice(randlist)+1
randfinal = round(randfase23*randfase21/randfase22)

for i in range(len(NIM)):
    for j in range(randfinal):
        randChoice = int(time.strftime("%S"))
    pilihan = random.choice(NIM)
    NIM.remove(pilihan)
    listBaru.append(pilihan)

batchSize = 14
panjangTotal = len(listBaru)
batches = panjangTotal // batchSize
sisa = panjangTotal % batchSize

index = 0

for i in range(batches):
    print(f"Batch {i+1}\n")
    for j in range(index, index + batchSize):
        print(f"{listBaru[j]}")
    index += batchSize
    print("\n")

if sisa > 0:
    print(f"Batch {batches+1} (Sisa)\n")
    for j in range(index, panjangTotal):
        print(f"{listBaru[j]}")
        index += 1
    print("\n")

print (f"Total ada {index} mahasiswa dari {len(NIMMaster)}")