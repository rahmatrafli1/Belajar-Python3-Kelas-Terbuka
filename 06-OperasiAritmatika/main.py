a = 10
b = 3

# operasi tambah
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi kurang
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi kali
hasil = a * b
print(a,'x',b,'=',hasil)

# operasi bagi
hasil = a / b
print(a,':',b,'=',hasil)

# operasi modulus
hasil = a % b
print(a,'mod',b,'=',hasil)

# operasi eksponen
hasil = a ** b
print(a,'^',b,'=',hasil)

# operasi floor division
hasil = a // b
print(a,'//',b,'=',hasil)

# operasi prioritas
'''
    1. ()
    2. eksponen
    3. perkalian, pembagian, modulus, floor division
    4. pertambahan, pengurangan
'''
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

# kurung akan mengambil langkah lebih dulu
hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)