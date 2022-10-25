blocks = {
	'CJK Unified Ideographs Extension A': (0x3400, 0x4DBF),
	'CJK Unified Ideographs': (0x4E00, 0x9FFF),
	'CJK Unified Ideographs Extension B': (0x20000, 0x2A6DF),
	'CJK Unified Ideographs Extension C': (0x2A700, 0x2B739),
	'CJK Unified Ideographs Extension D': (0x2B740, 0x2B81D),
	'CJK Unified Ideographs Extension E': (0x2B820, 0x2CEA1),
	'CJK Unified Ideographs Extension F': (0x2CEB0, 0x2EBE0),
	'CJK Unified Ideographs Extension G': (0x30000, 0x3134A),
	'CJK Unified Ideographs Extension H': (0x31350, 0x323AF),
}

for name, (start, end) in blocks.items():
	with open(f'Tables/Character Sets/Unicode {name}.txt', 'w', encoding='utf-8') as f:
		f.writelines(chr(i) + '\n' for i in range(start, end + 1))
