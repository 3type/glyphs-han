with open("Unicode CJK Unified Ideographs.txt", "w") as f:
	f.write("\n".join([chr(i) for i in range(0x4e00,  0x9ffc+1)]) + "\n")
with open("Unicode CJK Unified Ideographs Extension A.txt", "w") as f:
	f.write("\n".join([chr(i) for i in range(0x3400,  0x4dbf+1)]) + "\n")
with open("Unicode CJK Unified Ideographs Extension B.txt", "w") as f:
	f.write("\n".join([chr(i) for i in range(0x20000, 0x2a6dd+1)]) + "\n")
with open("Unicode CJK Unified Ideographs Extension C.txt", "w") as f:
	f.write("\n".join([chr(i) for i in range(0x2a700, 0x2b734+1)]) + "\n")
with open("Unicode CJK Unified Ideographs Extension D.txt", "w") as f:
	f.write("\n".join([chr(i) for i in range(0x2b740, 0x2b81d+1)]) + "\n")
with open("Unicode CJK Unified Ideographs Extension E.txt", "w") as f:
	f.write("\n".join([chr(i) for i in range(0x2b820, 0x2cea1+1)]) + "\n")
with open("Unicode CJK Unified Ideographs Extension F.txt", "w") as f:
	f.write("\n".join([chr(i) for i in range(0x2ceb0, 0x2ebe0+1)]) + "\n")
with open("Unicode CJK Unified Ideographs Extension G.txt", "w") as f:
	f.write("\n".join([chr(i) for i in range(0x30000, 0x3134a+1)]) + "\n")
