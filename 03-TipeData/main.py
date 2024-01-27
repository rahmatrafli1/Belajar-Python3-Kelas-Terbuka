# angka (integer)
data_int = 1
print("- data:",data_int)
print("- bertipe:", type(data_int))
print()

# angka (float)
data_float = 1.2
print("- data:",data_float)
print("- bertipe:", type(data_float))
print()

# string
data_str = "Hello"
print("- data:",data_str)
print("- bertipe:", type(data_str))
print()

# boolean
data_bool = False
print("- data:",data_bool)
print("- bertipe:", type(data_bool))
print()

# tipe data khusus

# bilangan kompleks
data_kompleks = complex(5,6)
print("- data:",data_kompleks)
print("- bertipe:", type(data_kompleks))
print()

# tipe data dari bahasa c
from ctypes import c_double

data_c_double = c_double(10.5)
print("- data:",data_c_double)
print("- bertipe:", type(data_c_double))
print()