# not, or, and, xor

print("Operasi Logika\n")

# not
print("Contoh Not:\n")
a = False
b = not a

print("a:", a)
print("not a:", b)

# or
print("\nContoh Or:\n")
a = True
b = False
c = a or b

print(a,'or',b,'=',c)

a = False
b = True
c = a or b

print(a,'or',b,'=',c)

a = False
b = False
c = a or b

print(a,'or',b,'=',c)

a = True
b = True
c = a or b

print(a,'or',b,'=',c)

# and
print("\nContoh And:\n")
a = True
b = False
c = a and b

print(a,'and',b,'=',c)

a = False
b = True
c = a and b

print(a,'and',b,'=',c)

a = False
b = False
c = a and b

print(a,'and',b,'=',c)

a = True
b = True
c = a and b

print(a,'and',b,'=',c)

# xor
print("\nContoh Xor:\n")
a = True
b = False
c = a ^ b

print(a,'xor',b,'=',c)

a = False
b = True
c = a ^ b

print(a,'xor',b,'=',c)

a = False
b = False
c = a ^ b

print(a,'xor',b,'=',c)

a = True
b = True
c = a ^ b

print(a,'xor',b,'=',c)