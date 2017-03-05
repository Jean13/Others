# Convert from logged HID keyboard usage to Ascii

from HID_Table import HIDKeyboard
 
# The log file - modify accordingly
file = open('TIC.txt','r').read().splitlines()
 
for line in file:
	line = line.split()
	for i in line:
		if '+' in i:
			i = '0x' + i[1:]
			print HIDKeyboard[i]

