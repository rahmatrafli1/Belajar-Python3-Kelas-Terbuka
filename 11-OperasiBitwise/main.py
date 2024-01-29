# Operasi Bitwise

print("Operasi Bitwise\n")

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print("========== CONTOH OR ==========")
print(f"nilai a: {a}, binary: {format(a,'08b')}")
print(f"nilai b: {b}, binary: {format(b,'08b')}")
print("------------------------------(|)")
print(f"nilai c: {c}, binary: {format(c,'08b')}")


# bitwise AND (&)
c = a & b
print("\n========== CONTOH AND ==========")
print(f"nilai a: {a}, binary: {format(a,'08b')}")
print(f"nilai b: {b}, binary: {format(b,'08b')}")
print("------------------------------(&)")
print(f"nilai c: {c}, binary: {format(c,'08b')}")

# bitwise XOR (^)
c = a ^ b
print("\n========== CONTOH XOR ==========")
print(f"nilai a: {a}, binary: {format(a,'08b')}")
print(f"nilai b: {b}, binary: {format(b,'08b')}")
print("------------------------------(^)")
print(f"nilai c: {c}, binary: {format(c,'08b')}")

# bitwise NOT (~)
c = ~a
print("\n========== CONTOH NOT ==========")
print(f"nilai a: {a}, binary: {format(a,'08b')}")
print("------------------------------(~)")
print(f"nilai c: {c}, binary: {format(c,'08b')}")
print("------------------------------(^)")
d = 0b00001001
e = 0b11111111
print(f"nilai e: {e ^ d}, binary: {format(e^d,'08b')}")

# bitwise SHIFT
print("\n========== CONTOH SHIFT ==========")
# shift right (>>)
c = a >> 1
print("\n========== SHIFT RIGHT ==========")
print(f"nilai a: {a}, binary: {format(a,'08b')}")
print("------------------------------(>>)")
print(f"nilai c: {c}, binary: {format(c,'08b')}")

# shift left (<<)
c = a << 1
print("\n========== SHIFT LEFT ==========")
print(f"nilai a: {a}, binary: {format(a,'08b')}")
print("------------------------------(<<)")
print(f"nilai c: {c}, binary: {format(c,'08b')}")