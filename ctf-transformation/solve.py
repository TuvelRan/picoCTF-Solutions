# -*- coding: utf-8 -*-
enc = open('enc').readlines()[0]
decoded = []
for c in enc:
    decoded.append(hex(ord(c)).lstrip('0x'))
    
print(decoded)

numbers = []

for i in decoded:
    numbers.append(i.decode('utf-16-be'))


print(numbers)