#SEARCHING

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

arr = []
jumlah_data = int(input("Masukkan jumlah data: "))
for i in range(jumlah_data):
    data = int(input("Masukkan data ke-{}: ".format(i+1)))
    arr.append(data)


x = int(input("Masukkan angka: "))


result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
 print("Elemen ditemukan pada indeks ke-", str(result))
else:
 print("Element tidak ditemukan")