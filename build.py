TEMPLATE_STR = r'''
	{{
		icon = HanTemplate;
		name = Chinese;
		predicate = "script == \"han\"";
		subGroup = ({}
		);
	}},'''

main_str = ''

def add_quotes(s: str) -> str:
	if s.find(' ') != -1:
		return '"{}"'.format(s)
	else:
		return s

def get_char_list(rel_path: str, tabs: int, use_char=True) -> str:
	with open('Tables/{}.txt'.format(rel_path)) as f:
		if use_char:
			lines = ['"{}"'.format(line[0]) for line in f.readlines()]
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
	main_str += '''
			{{
				name = {};
				charList = ({});
			}},'''.format(add_quotes(i), get_char_list(i, 5))

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
		sub_group += '''
							{{
								name = {};
								charList = ({});
							}},'''.format(
								add_quotes(i),
								get_char_list('Regional/{}/{}'.format(name, i), 9))
	regional_str += '''
					{{
						name = {};
						subGroup = ({});
					}},'''.format(add_quotes(name), sub_group + '\n' + '\t' * 6)

main_str += '''
			{{
				name = Regional;
				subGroup = ({});
			}},'''.format(regional_str + '\n\t\t\t\t')

########################################
## Part 3 - Character Sets
########################################

charset_str = ''

for i in [
		'GB 2312',
		'Big 5',
		'Unicode CJK Unified Ideographs',
		'Unicode CJK Unified Ideographs Extension A',
	]:
	charset_str += '''
					{{
						name = {};
						charList = ({});
					}},'''.format(add_quotes(i), get_char_list('Character Sets/' + i, 7))

main_str += '''
			{{
				name = "Character Sets";
				subGroup = ({});
			}},'''.format(charset_str + '\n\t\t\t\t')

########################################
## Part 4 - Symbols
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
	symbols_str += '''
					{{
						name = {};
						{} = ({});
					}},'''.format(
						add_quotes(i[0]),
						'charList' if i[1] else 'coverage',
						get_char_list('Radicals, Strokes and Symbols/' + i[0], 7, use_char=i[1]))

main_str += '''
			{{
				name = "Radicals, Strokes and Symbols";
				subGroup = ({});
			}},'''.format(symbols_str + '\n\t\t\t\t')

########################################
## Final print
########################################

print(TEMPLATE_STR.format(main_str))
