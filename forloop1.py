#forloop1.py
#python has a way of encapsulating of the code
print("DEC\tHEX\tBIN\tCHAR")
for d in range(32,128):
	h=hex(d)
	h=h.replace("0x","") #every time it sees "0x" it replaces it with a "$"
	b=bin(d)
	b=b.replace("0b","") #likewise
	c=chr(d)
	#~print(str(d)+" "+h,end="")
	print(str(d)+"\t"+str(h)+"\t"+str(b)+"\t"+str(c))
#str(d)+" " is a concatination
#python3 "%f"
