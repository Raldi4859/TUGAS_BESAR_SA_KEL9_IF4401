import time
start_time = time.time()
## TUGAS BESAR STRATEGI ALGORITMA
## PERBANDINGAN ALGORITMA BRUTE FORCE DAN DIVIDE & CONQUER UNTUK MENYELESAIKAN KASUS POKER HAND COMBINATION
## KELOMPOK 9:
## AFKAR ARTHAGESANG PRADESTOAN	- 1301200131
## DIAN RAMADHINI - 1301200254
## RASYID RIYALDI - 1301200457
## KELAS: IF-44-01

## Fungsi Input Tipe Kartu
def inputSuits():
    suits = []

    print("Tipe Kartu : D = Diamond, H = Heart, C = Club, S = Spade")
    print("Contoh Input: D,D,D,D,D atau s,s,s,s,s ")
    print("Masukkan Tipe Kartu: ")
    suits = list(map(str, input().upper().split(',')))
  
    return suits

## Fungsi Input Nilai Kartu
def inputValue(suits, flush):
    value = []

    print("Nilai Kartu: Ace(A) = 1, King(K) = 13, Queen(Q) = 12, Jack(J) = 11, 10,..,2")
    print("Contoh Input: 1,13,12,11,10 ")
    print("Masukkan Nilai Kartu: ")
    value = list(map(int, input().split(',')))
    print("Nilai Kartu: ")
    print(value)
  
    return value

def isFlush(suits):
    flush = False
    if suits == ['D','D','D','D','D'] or suits == ['C','C','C','C','C'] or suits == ['S','S','S','S','S'] or suits == ['H','H','H','H','H']:
        flush = True
    else:
        flush = False
    return flush


## Fungsi untuk menampilkan kesimpulan kombinasi kartu
def combination(value,flush):
    card = ()
    arrCount = 0

    if flush == True:
        if value == [1,10,11,12,13]:
            card = print("Kombinasi Kartu adalah Royal Flush")
        elif value == [value[0], value[0]+1, value[0]+2, value[0]+3, value[0]+4]:
            card = print("Kombinasi Kartu adalah Straight Flush")
        else:
            card = print("Kombinasi Kartu adalah Flush")
    else:
        card = print("Kombinasi Kartu Bukan Flush, Straight Flush atau Royal Flush")

    return card
        
## Fungsi Brute Force Menggunakan Bubble Sort
def BruteForce(arr):
    n = len(arr)
    swap = False
    for i in range(n-1):
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1]:
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap:
            return

## Fungsi Divide & Conquer Menggunakan Merge Sort
## Code untuk melakukan merge
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l     

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
## Code untuk melakukan proses Divide & Conquer
def DivideConquer(arr, l, r):
    if l < r:
 
        m = l+(r-l)//2
 
        DivideConquer(arr, l, m)
        DivideConquer(arr, m+1, r)
        merge(arr, l, m, r)
 


## Main Program Untuk Uji Coba Algoritma Brute Force
def testBruteForce():
    print("Uji Program Menggunakan Algoritma Brute Force")
    suits = inputSuits()
    flush = isFlush(suits)
    value = inputValue(suits,flush)
 
    BruteForce(value)
 
    if value != []:
        print("Kartu yang dimiliki: ")
        for i in range(len(value)):
            print(value[i], suits[i])

    combination(value,flush)

    waktu = time.time() - start_time
    print(" %s second " % (waktu))

## Main Program Untuk Uji Coba Algoritma Divide & Conquer
def testDivideConquer():
    print("Uji Program Menggunakan Algoritma Divide & Conquer")
    suits = inputSuits()
    flush = isFlush(suits)
    value = inputValue(suits,flush)

    n = len(value)
    DivideConquer(value, 0, n-1)

    if value != []:
        print("Kartu yang dimiliki: ")
        for i in range(len(value)):
            print(value[i], suits[i])

    combination(value,flush)

    waktu = time.time() - start_time
    print(" %s second " % (waktu))

##testBruteForce()
testDivideConquer()
