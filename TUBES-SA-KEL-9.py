from collections import defaultdict
from this import d
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
  n = 5


  print("Tipe Kartu : D = Diamond, H = Heart, C = Club, S = Spade")
  print("Contoh Input: ")
  print("D")
  print("D")
  print("D")
  print("D")
  print("D")
  print("Masukkan Tipe Kartu: ")

  suits = [str(input()) for i in range(n)]
  
  if suits == ['D', 'D', 'D', 'D','D']:
    print("Tipe Kartu: Diamond")
  elif suits == ['S', 'S', 'S', 'S', 'S']:
    print("Tipe Kartu: Spade")
  elif suits == ['C', 'C', 'C', 'C', 'C']:
    print("Tipe Kartu: Club")
  elif suits == ['H', 'H', 'H','H', 'H']:
    print("Tipe Kartu: Heart")
  return suits

## Fungsi Input Nilai Kartu
def inputValue(suits):
  value = []
  n = 5

  if suits == ['D', 'D', 'D', 'D', 'D'] or suits == ['C', 'C', 'C', 'C', 'C'] or suits == ['S', 'S', 'S', 'S', 'S'] or suits == ['H', 'H', 'H','H', 'H']:
    print("Nilai Kartu: Ace(A) = 1, King(K) = 13, Queen(Q) = 12, Jack(J) = 11, 10,..,2")
    print("Contoh Input: ")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("Masukkan Nilai Kartu: ")
    value = [str(input()) for i in range(n)]
    print("Nilai Kartu: ")
    print(value)
  else:
    print("Kombinasi Kartu Bukan Merupakan Flush, Straight Flush, atau Royal Flush")

  return value

## Fungsi untuk menampilkan kesimpulan kombinasi kartu
def combination(arr):
    cardOrder = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "11":11, "11":12, "13":13}
    n = len(arr)
    card = ()
    values = [i[0] for i in arr]
    valueCount = defaultdict(lambda:0)

    if arr == ["1", "10", "11", "12", "13"]:
        card = "Kombinasi Kartu adalah Royal Flush"
    else:
        try:
            for v in values:
                valueCount[v] += 1
            rankValue = [cardOrder[i] for i in values]
            valueRange = max(rankValue) - min(rankValue)
            if len(set(valueCount.values())) == 1 and (valueRange == 4):
                card = "Kombinasi Karttu adalah Straight Flush"
            else:
                card = "Kombinasi Kartu adalah Flush"
        except Exception:
            pass
        
    if card != ():
        print(card)
        
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
    value = inputValue(suits)
 
    BruteForce(value)
 
    if value != []:
        print("Kartu yang dimiliki: ")
        for i in range(len(value)):
            print(value[i], suits[i])

    combination(value)

    waktu = time.time() - start_time
    print(" %s second " % (waktu))

## Main Program Untuk Uji Coba Algoritma Divide & Conquer
def testDivideConquer():
    print("Uji Program Menggunakan Algoritma Divide & Conquer")
    suits = inputSuits()
    value = inputValue(suits)

    n = len(value)
    DivideConquer(value, 0, n-1)

    if value != []:
        print("Kartu yang dimiliki: ")
        for i in range(len(value)):
            print(value[i], suits[i])

    combination(value)

    waktu = time.time() - start_time
    print(" %s second " % (waktu))

##testBruteForce()
testDivideConquer()