import random
import time

NIMMaster = [
    71241086, 71241113, 71241118, 71241157, 71251173,
    71251177, 71251181, 71251182, 71251186, 71251190,
    71251192, 71251198, 71251199, 71251208, 71251210,
    71251211, 71251212, 71251213, 71251218, 71251224,
    71251225, 71251226, 71251227, 71251228, 71251232
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