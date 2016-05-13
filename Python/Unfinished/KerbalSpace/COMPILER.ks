<python>
	import re

	#filepath = 'Test.ks'
	#newFilepath = 'test.py'

	def compiler(filepath, newFilepath):
		
		def tags(word):
			return {
				'python' : 'py'
				}.get(word,'ks')

		def parse(line,s=''):
			startTag = re.match("<(?P<lang>.*)>", line)
			bypass = re.match("\s*--(?P<a>.*)", line)
			printing = re.match("\s*>\s*(?P<a>.*)", line)
			reading = re.match("\s*<\s*(?P<a>[^,]*)(,(?P<b>.*[^>]))?", line)
			ifStatement = re.match("\s*\?(?P<a>[^:]*)(:(?P<b>[^:]*))?(:(?P<c>.*))?", line)
			
			if startTag:
				global LANG
				LANG = tags(startTag.group('lang'))
			elif bypass:
				output.write(bypass.group('a'))
			elif printing:
				output.write('print('+printing.group('a')+')')
			elif reading:
				output.write(reading.group('a')+" = input(")
				if reading.group('b'):
					output.write(reading.group('b'))
				output.write(")")
			elif ifStatement:
				print(ifStatement.group('a'),ifStatement.group('b'),ifStatement.group('c'))
				output.write('if '+ifStatement.group('a')+':')
				if ifStatement.group('b'):
					output.write('\n'+s+'    ')
					parse(ifStatement.group('b'))
					if ifStatement.group('c'):
						output.write('\n'+s+'else:')
						output.write('\n'+s+'    ')
						parse(ifStatement.group('c'))
			else:
				output.write('# Unrecognized syntax: '+line)

		try:
			file = open(filepath)
			words = file.read().splitlines()
			file.close()
			output = open(newFilepath,'w')
			global LANG
			LANG = 'ks'
			# Parsing each line for a recognizable statement.
			for line in words:
				# If the Python tags are used...
				if LANG == 'py':
					if re.match("</python>", line):
						LANG = 'ks'
						line = ''
					s = re.match('(?P<s>\s*.*)', line)
					line = line.split()
					output.write(s.group('s')[1:])
					
				# If the content is native KerbalSpace...
				else:
					if not line:
						continue
					s = re.match('(?P<s>\s*)', line).group('s')
					output.write(s)
					parse(line,s)
						
				output.write('\n')
			output.close()

		except IOError:
			print("The file could not be located.")
			
	#compiler(filepath, newFilepath)
</python>