import binascii

data = int(binascii.hexlify(open('flag.enc', 'rb').read()), 16)

for exp in range(2, 2**10):
	i = 1
	temp_bit = ''
	temp_data = data
	while temp_data > 0:
		temp_bit += str((temp_data % exp - (-1) ** i) % exp)
		temp_data //= exp
		i += 1
	print(temp_bit)
	if exp == 10: break
