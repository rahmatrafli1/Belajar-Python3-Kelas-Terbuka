# 1. Latihan Konversi Satuan Temperature

# Program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")
input_celcius = float(input('Masukkan Suhu dalam Celcius: '))
print("suhu adalah:",input_celcius,"Celcius")

# Reamur
# 4/5 * celcius
reamur_celcius = (4/5) * input_celcius
print("\nReamur:",reamur_celcius,"Reamur\n")

# Farenhiet
# 9/5 * celcius + 32
farenhiet_celcius = (9/5) * input_celcius + 32
print("Farenhiet:",farenhiet_celcius,"Farenhiet\n")

# Kelvin
# celcius + 273
kelvin_celcius = input_celcius + 273
print("Kelvin:",kelvin_celcius,"Kelvin\n")

# Program konversi reamur ke satuan lain

input_reamur = float(input('Masukkan Suhu dalam Reamur: '))
print("suhu adalah:",input_reamur,"Reamur")

# Celcius
# 5/4 * reamur
celcius_reamur = (5/4) * input_reamur
print("\nCelcius:",celcius_reamur,"Celcius\n")

# Farenhiet
# 9/4 * reamur + 32
farenhiet_reamur = (9/4) * input_reamur + 32
print("Farenhiet:",farenhiet_reamur,"Farenhiet\n")

# Kelvin
# 5/4 * reamur + 273
kelvin_reamur = (5/4) * input_reamur + 273
print("Kelvin:",kelvin_reamur,"Kelvin\n")

# Program konversi farenhiet ke satuan lain

input_farenhiet = float(input('Masukkan Suhu dalam Farenhiet: '))
print("suhu adalah:",input_farenhiet,"Farenhiet")

# Celcius
# 5/9 * (farenhiet - 32)
celcius_farenhiet = (5/9) * (input_farenhiet - 32)
print("\nCelcius:",celcius_farenhiet,"Celcius\n")

# Reamur
# 4/9 * (farenhiet - 32)
reamur_farenhiet = (4/9) * (input_farenhiet - 32)
print("Reamur:",reamur_farenhiet,"Reamur\n")

# Program konversi kelvin ke satuan lain

input_kelvin = float(input('Masukkan Suhu dalam Kelvin: '))
print("suhu adalah:",input_kelvin,"Kelvin")

# Celcius
# kelvin - 273
celcius_kelvin = input_kelvin - 273
print("\nCelcius:",celcius_kelvin,"Celcius\n")

# Reamur
# 4/5 * (kelvin - 273)
reamur_kelvin = (4/5) * (input_kelvin - 273)
print("Reamur:",reamur_kelvin,"Reamur\n")