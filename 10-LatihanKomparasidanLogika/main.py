# Latihan Logika dan Komparasi

# Membuat gabungan area rentang dari angka

# ++++++3-------------10++++++++
inputUser = int(input("Masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10: "))

# ++++++3--------------
# Ini adalah memeriksa angka yang kurang dari 3
is_kurang_dari = inputUser < 3
print(f"\n{inputUser} < 3 adalah {is_kurang_dari}")

# -------------10++++++
# Ini adalah memeriksa angka yang lebih dari 10
is_lebih_dari = inputUser > 10
print(f"{inputUser} > 10 adalah {is_lebih_dari}")

# ++++++3-------------10++++++++
# Ini adalah gabungan area angka
isCorrectOr = is_kurang_dari or is_lebih_dari
print(f"{is_kurang_dari} or {is_lebih_dari} adalah {isCorrectOr}")

# ------3+++++++++++++10--------
inputUser = int(input("\nMasukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10: "))

# ------3+++++++++++++
# Ini adalah memeriksa angka yang lebih dari 3
is_lebih_dari = inputUser > 3
print(f"\n{inputUser} > 3 adalah {is_lebih_dari}")

# ++++++++++++10------
# Ini adalah memeriksa angka yang kurang dari 10
is_kurang_dari = inputUser < 10
print(f"{inputUser} < 10 adalah {is_kurang_dari}")

# ------3+++++++++++++10--------
# Ini adalah irisan area angka
isCorrectAnd = is_lebih_dari and is_kurang_dari
print(f"{is_lebih_dari} and {is_kurang_dari} adalah {isCorrectAnd}")


# ------0+++++++5--------8+++++++11-------
inputUser = int(input("\nMasukkan angka yang bernilai\nlebih dari 0 dan kurang dari 5\natau\nlebih dari 8 dan kurang dari 11: "))

# ------0+++++++++++++
# Ini adalah memeriksa angka yang lebih dari 0
is_lebih_dari = inputUser > 0
print(f"\n{inputUser} > 0 adalah {is_lebih_dari}")

# ++++++++++++5-------
# Ini adalah memeriksa angka yang kurang dari 5
is_kurang_dari = inputUser < 5
print(f"{inputUser} < 5 adalah {is_kurang_dari}")


# ------0+++++++5--------
# Ini adalah irisan area angka
isCorrectAnd1 = is_lebih_dari and is_kurang_dari
print(f"{is_lebih_dari} and {is_kurang_dari} adalah {isCorrectAnd1}")

# ------8+++++++++++++
# Ini adalah memeriksa angka yang lebih dari 8
is_lebih_dari = inputUser > 8
print(f"\n{inputUser} > 8 adalah {is_lebih_dari}")

# ++++++++++++11------
# Ini adalah memeriksa angka yang kurang dari 11
is_kurang_dari = inputUser < 11
print(f"{inputUser} < 11 adalah {is_kurang_dari}")

# ------8+++++++11--------
# Ini adalah irisan area angka
isCorrectAnd2 = is_lebih_dari and is_kurang_dari
print(f"{is_lebih_dari} and {is_kurang_dari} adalah {isCorrectAnd2}")

# ------0+++++++5--------8+++++++11-------
# Ini adalah gabungan area angka
isCorrectOr = isCorrectAnd1 or isCorrectAnd2
print(f"\n{isCorrectAnd1} or {isCorrectAnd2} adalah {isCorrectOr}")


# ++++++0-------5++++++++8-------11+++++++
inputUser = int(input("\nMasukkan angka yang bernilai\nkurang dari 0 atau lebih dari 5\ndan\nkurang dari 8 atau lebih dari 11: "))

# ++++++++++++0-------
# Ini adalah memeriksa angka yang kurang dari 0
is_kurang_dari = inputUser < 0
print(f"\n{inputUser} < 0 adalah {is_kurang_dari}")

# ------5+++++++++++++
# Ini adalah memeriksa angka yang lebih dari 5
is_lebih_dari = inputUser > 5
print(f"{inputUser} > 5 adalah {is_lebih_dari}")


# ++++++0------5++++++
# Ini adalah gabungan area angka
isCorrectOr1 = is_kurang_dari or is_lebih_dari
print(f"{is_kurang_dari} or {is_lebih_dari} adalah {isCorrectOr1}")

# ++++++8-------------
# Ini adalah memeriksa angka yang kurang dari 8
is_kurang_dari = inputUser < 8
print(f"\n{inputUser} < 8 adalah {is_kurang_dari}")

# ------------11++++++
# Ini adalah memeriksa angka yang kurang dari 11
is_lebih_dari = inputUser > 11
print(f"{inputUser} > 11 adalah {is_lebih_dari}")

# ++++++8-------11++++++
# Ini adalah gabungan area angka
isCorrectOr2 = is_lebih_dari or is_kurang_dari
print(f"{is_lebih_dari} or {is_kurang_dari} adalah {isCorrectOr2}")

# ++++++0-------5++++++++8-------11+++++++
# Ini adalah gabungan area angka
isCorrectAnd = isCorrectOr1 and isCorrectOr2
print(f"\n{isCorrectOr1} and {isCorrectOr2} adalah {isCorrectAnd}")