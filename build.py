main_str = ''

def add_quotes(s: str) -> str:
	if s.find(' ') != -1:
		return f'"{s}"'
	return s

def get_char_list(rel_path: str, tabs: int, use_char=True) -> str:
	with open(f'Tables/{rel_path}.txt', encoding='utf-8') as f:
		if use_char:
			lines = [f'"{line[0]}"' for line in f.readlines()]
		else:
			lines = [line[:-1] for line in f.readlines()]
		init = '\n' + '\t' * tabs
		final = ',\n' + '\t' * (tabs - 1)
		return init + (',' + init).join(lines) + final

########################################
## Part 1 - Basic
########################################

for i in [
		'Fundamental (Simplified)',
		'Fundamental (Traditional)',
		'Undecomposable',
		'Commonly Used on Internet',
	]:
	main_str += f'''
			{{
				name = {add_quotes(i)};
				charList = ({get_char_list(i, 5)});
			}},'''

########################################
## Part 2 - Regional
########################################

regional_str = ''

for name, sub in {
		'China Mainland': [
			'Educational Basic',
			'Educational 1',
			'Educational 2',
			'General Standard Chinese Characters 1',
			'General Standard Chinese Characters 2',
			'General Standard Chinese Characters 3',
		],
		'Taiwan': [
			'Frequently Used Chinese Characters',
			'Less Commonly Used Chinese Characters',
		],
		'Hong Kong': [
			'Commonly Used Chinese Characters',
		],
	}.items():
	sub_group = ''
	for i in sub:
		sub_group += f'''
							{{
								name = {add_quotes(i)};
								charList = ({get_char_list(f'Regional/{name}/{i}', 9)});
							}},'''
	regional_str += f'''
					{{
						name = {add_quotes(name)};
						subGroup = ({sub_group}
						);
					}},'''

main_str += f'''
			{{
				name = Regional;
				subGroup = ({regional_str}
				);
			}},'''

########################################
## Part 3 - Character Sets
########################################

charset_str = ''

for item in [
		'GB 2312',
		{'GB 18030': [
			'Level 1',
			'Level 2',
			'Level 3',
		]},
		'Big 5',
	]:
	if isinstance(item, dict):
		name = list(item.keys())[0]
		sub = item[name]
		sub_group = ''
		for i in sub:
			sub_group += f'''
							{{
								name = {add_quotes(i)};
								charList = ({get_char_list(f'Character Sets/{name}/{i}', 9)});
							}},'''
		charset_str += f'''
					{{
						name = {add_quotes(name)};
						subGroup = ({sub_group}
						);
					}},'''
	else:
		charset_str += f'''
					{{
						name = {add_quotes(item)};
						charList = ({get_char_list('Character Sets/' + item, 7)});
					}},'''

main_str += f'''
			{{
				name = "Character Sets";
				subGroup = ({charset_str}
				);
			}},'''

########################################
## Part 4 - Unicode Blocks
########################################

unicode_str = ''

for i in [
		'CJK Unified',
		'CJK Ext. A',
		'CJK Ext. B',
		'CJK Ext. C',
		'CJK Ext. D',
		'CJK Ext. E',
		'CJK Ext. F',
		'CJK Ext. G',
		'CJK Ext. H',
		'CJK Ext. I',
		'CJK Ext. J',
		'CJK Compatibility',
		'CJK Compatibility Supplement',
	]:
	unicode_str += f'''
					{{
						name = {add_quotes(i)};
						charList = ({get_char_list('Unicode Blocks/' + i, 7)});
					}},'''

main_str += f'''
			{{
				name = "Unicode Blocks";
				subGroup = ({unicode_str}
				);
			}},'''

########################################
## Part 5 - Symbols
########################################

symbols_str = ''

for i in [
		('Kangxi Radicals', True),
		('Radicals Supplement', True),
		('Strokes', False),
		('Bopomofo', False),
		('Bopomofo Extended', False),
		('Suzhou Numerals', False),
		('Other Han Symbols', False),
	]:
	key = 'charList' if i[1] else 'coverage'
	val = get_char_list('Radicals, Strokes and Symbols/' + i[0], 7, use_char=i[1])
	symbols_str += f'''
					{{
						name = {add_quotes(i[0])};
						{key} = ({val});
					}},'''

main_str += f'''
			{{
				name = "Radicals, Strokes and Symbols";
				subGroup = ({symbols_str}
				);
			}},'''

########################################
## Final print
########################################

print(rf'''
	{{
		icon = HanTemplate;
		name = Chinese;
		predicate = "script == \"han\"";
		subGroup = ({main_str}
		);
	}},'''
)
