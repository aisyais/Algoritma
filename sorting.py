import random

# Fungsi merge_sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Fungsi quick_sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def main():
    # Ini adalah array original atau array yang ditampilkan di soal.
    original_array = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    
    # Tampilkan array original sebelum masuk ke pilihan
    print("Array Original:", original_array)

    # Setelah program dijalankan, akan tampil opsi-opsi dimana kita dapat memilih ingin melihat contoh best case, worst case, dan average case.
    # Dalam merge sort, kompleksitas waktu untuk best case adalah O(nlogn), untuk worst case adalah O(nlogn), dan averagenya adalah O(nlogn).
    # dalam quick sort sendiri, umumnya best case memiliki kompleksitas waktu O(nlogn), worst case O(n^2), dan averagenya adalah O(nlogn).
    while True:
        print("\nPilih jenis kasus untuk analisis:")
        print("1. Best Case (sudah terurut)")
        print("2. Worst Case (terbalik urutannya)")
        print("3. Average Case (acak)")
        print("4. Keluar dari program")
        choice = int(input("Masukkan pilihan Anda (1/2/3/4): "))
        
        if choice == 1:
            # Bagian pertama atau 1 adalah Best Case dimana contohnya bisa berupa array yang acak tadi kita urutkan secara ascending seperti di output nanti.
            array = sorted(original_array)
            print("\nArray Best Case:", array)
        elif choice == 2:
            # Bagian ini adalah logika untuk Worst Case, dimana contohnya adalah array yang diurutkan secara terbalik maka dari itu dalam program saya menggunakan reverse=true
            array = sorted(original_array, reverse=True)
            print("\nArray Worst Case:", array)
        elif choice == 3:
            # Untuk bagian ketiga ini adalah average case. Dimana nanti array akan diacak, maka dari itu saya mengimpor modul random.
            array = original_array[:]
            random.shuffle(array)
            print("\nArray Average Case (acak):", array)
            
            # setelah Pengguna memilih opsi ketiga yaitu Average case, pengguna dapat memasukkan angka yang ingin dicari.
            # Average case sendiri adalah sepemahaman saya case dimana komputer mencari data yang berada di tengah array atau di dalam array maka dari itu contohnya saya buat pengguna bisa menginput angka yang ingin dicari.
            target = int(input("\nMasukkan angka yang ingin dicari: "))
            if target in array:
                print(f"Angka {target} ditemukan dalam array.")
            else:
                print(f"Angka {target} tidak ditemukan dalam array.")
        elif choice == 4:
            #untuk bagian 4 ini sendiri adalah opsi ketika pengguna sudah tidak ingin lagi melihat kasus best, worst, dan average atau keluar dari program.
            # Keluar dari program
            print("Telah keluar dari program")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
            continue

        # Ini adalah bagian sortingnya
        merge_sorted_array = array[:]
        merge_sort(merge_sorted_array)
        quick_sorted_array = quick_sort(array)

        # bagian ini akan menampilkan hasil sortingnya.
        print("\nHasil Merge Sort:", merge_sorted_array)
        print("Hasil Quick Sort:", quick_sorted_array)

# Menjalankan program
main()
