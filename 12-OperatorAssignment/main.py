a = 5 # adalah assignment
print('Nilai a:',a)

# tambah
a += 1 # setara dengan a = a + 1
print('Nilai a += 1:',a)

# kurang
a -= 2 # setara dengan a = a - 2
print('Nilai a -= 2:',a)

# kali
a *= 5 # setara dengan a = a * 5
print('Nilai a *= 5:',a)

# bagi
a /= 2 # setara dengan a = a / 2
print('Nilai a /= 2:',a)

# modulus dan floor division
b = 10
print("\nNilai b:",b)

b %= 3 # setara dengan b = b % 3
print("Nilai b %= 3:",b)

b = 10
print("\nNilai b:",b)

b //= 3 # setara dengan b = b // 3
print("Nilai b //= 3:",b)

# pangkat
a = 5
print("\nNilai a:",a)

a **= 3 # setara dengan a = a ** 3
print("Nilai a **= 3:",a)

# Operasi Bitwise
# OR
c = True
print("\nNilai c:",c)

c |= False
print("Nilai c |= False:",c)

c = False
print("\nNilai c:",c)

c |= False
print("Nilai c |= False:",c)

# AND
c = True
print("\nNilai c:",c)

c &= True
print("Nilai c &= True:",c)

c = False
print("\nNilai c:",c)

c &= False
print("Nilai c &= False:",c)

# XOR
c = True
print("\nNilai c:",c)

c ^= True
print("Nilai c ^= True:",c)

c = False
print("\nNilai c:",c)

c ^= False
print("Nilai c ^= False:",c)

# geser geser
d = 0b0100
print("\nNilai d:",format(d, '04b'))

d >>= 2
print("Nilai d >>= 2:",format(d, '04b'))

d <<= 1
print("Nilai d >>= 1:",format(d, '04b'))