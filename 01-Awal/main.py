import time
start_time = time.time()
print("Hello")
print("World")
print("Hello World")

# Ini adalah komen
"""Ini adalah 
komen multiline"""
a = 10 # ini komen jg 
print(a)

for i in range(1, 1000):
    a = 10

print(time.time() - start_time, 'detik')

"""
cara mengkompilasi dalam bentuk .pyc diterminal
yaitu:
python3 -m py_compile nama_file.py
"""