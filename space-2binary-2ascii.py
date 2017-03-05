'''
Template for:
Revealing secret messages hidden in spaces and tabs.
Take spaces and/or tabs, convert every byte of data into 2-digit hex representation, convert the hex to binary and convert the binary to ascii. 
'''

import sys
from binascii import hexlify


# File with secret message, hidden in spaces and tabs
f = raw_input("Enter the filepath of the file to decrypt\n: ")

try:
	with open(f, "r") as f:
		lines = f.readlines()

except IOError as e:
	print "[!] Error opening file. Verify if correct filepath was entered.\n"

i = 0
out = ''
 
for line in lines:
	# Assuming each character represents a bit in a byte (8 bits)
	sub_str = line[-10:-2]
	sys.stdout.write(str(i) + ': ' )
	# Convert every byte of data into corresponding 2-digit hex representation
	print hexlify(sub_str)
 	# Convert hex to binary
	sub_str = sub_str.replace('\x20', '0')
	sub_str = sub_str.replace('\x09', '1')
	# Convert binary to ascii
	out += chr(int(int(sub_str,2)))
 
	print sub_str
	i += 1
	if i > 75:
		break

# Print the decrypted secret message in ascii 
print out
f.close()

