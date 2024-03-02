data = "Ini adalah string"
print(data)
print(type(data))

# Cara membuat String

'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan Single Quote'
print(f"\n{data}")

data = "Menggunakan Double Quote"
print(data)

print('"Halo, Apa Kabar?"')
print("'Halo, Apa Kabar?'")
print("Ini adalah hari Jum'at")

# 2. menggunakan tanda '

# membuat tanda ' menjadi string
print('mari kita shalat Jum\'at')
print('I haven\'t money')

# backslash
print('C:\\Users\\Rahmat')

# tab
print('Rahmat\tRifqi')

# backspace
print('Rahmat \bRifqi')

# newline
print('baris pertama.\nbaris kedua.') # LF => line feed
print('baris pertama.\rbaris kedua.') # CR => carriage return
print('baris pertama.\r\nbaris kedua.') # CRLF => line feed carriage return

# 3. String Literal atau raw

# hati-hati
print('C:\new folder') # akan salah path

# menggunakan raw string
print(r'C:\new folder')

# multiline string
print('''
Nama: Ujang
Kelas: 5 SD
''')

# multiline string dan raw
print(r'''
Nama: Ujang
Kelas: 5 SD / Normal
Website: www.google.com
''')