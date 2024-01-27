# Integer
print("===INTEGER===")
data_int = -2
print("data:",data_int,". Dengan tipe:",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false apabila nilai pada integer tersebut 0 selain dari 0 maka nilainya True
print("data:",data_float,". Dengan tipe:",type(data_float))
print("data:",data_str,". Dengan tipe:",type(data_str))
print("data:",data_bool,". Dengan tipe:",type(data_bool))
print()

# Float
print("===FLOAT===")
data_float = 2.5
print("data:",data_float,". Dengan tipe:",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan false apabila nilai pada integer tersebut 0 selain dari 0 maka nilainya True
print("data:",data_int,". Dengan tipe:",type(data_int))
print("data:",data_str,". Dengan tipe:",type(data_str))
print("data:",data_bool,". Dengan tipe:",type(data_bool))
print()

# Boolean
print("===BOOLEAN===")
data_bool = True
print("data:",data_bool,". Dengan tipe:",type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data:",data_int,". Dengan tipe:",type(data_int))
print("data:",data_float,". Dengan tipe:",type(data_float))
print("data:",data_str,". Dengan tipe:",type(data_str))
print()

# String
print("===STRING===")
data_str = "0"
print("data:",data_str,". Dengan tipe:",type(data_str))

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str) # akan True apabila nilainya berupa tipe datanya string kecuali string kosong baru bernilai False
print("data:",data_int,". Dengan tipe:",type(data_int))
print("data:",data_float,". Dengan tipe:",type(data_float))
print("data:",data_bool,". Dengan tipe:",type(data_bool))
print()