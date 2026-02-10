import sqlite3

# Koneksi ke database
conn = sqlite3.connect('absensi.db')
cursor = conn.cursor()

# Ambil data
cursor.execute("SELECT ID_Siswa FROM Absensi")
data = [row[0] for row in cursor.fetchall()]

# Algoritma pencarian (binary search)
def binary_search(data, target):
    left, right = 0, len(data)-1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif target < data[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print("Hasil pencarian:", binary_search(sorted(data), 25))
