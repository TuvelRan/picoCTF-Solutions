# The flag we found (isn't in the right order):
found = 'ocip{FTC0l_I4_t5m_ll0m_y_y3nc42a6a41ÿ\xc3}'
# It is written in little endian order. So let's convert it to a big endian order.
result = ''
for x in range(0, len(found), 4):
    result += str(found[x+3] + found[x+2] + found[x+1] + found[x]).lstrip('\n')

print(result)