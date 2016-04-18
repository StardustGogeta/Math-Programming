vim: syntax=kerbalspace

<python>
	import re

	#filepath = 'Test.ks'
	#newFilepath = 'test.py'

	def compiler(filepath, newFilepath):
		
		def tags(word):
			return {
				'python' : 'py'
				}.get(word,'# ERROR!')

		try:
			file = open(filepath)
			words = file.read().splitlines()
			file.close()
			# This is where the transcribing begins.
			output = open(newFilepath,'w')
			lang = 'ks'
			# Parsing each line for a recognizable statement, and marking the syntax type.
			for line in words:
				s = re.match('(?P<s>\s*)', line)
				line = line.split()
				print(line)
				output.write(s.group('s')[1:])
				for word in line:
					startTag = re.match("<(?P<lang>.*)>", word)
					endTag = re.match("</(.*)>", word)
					if startTag and not endTag:
						lang = tags(startTag.group('lang'))
						word=''
					if endTag:
						lang = 'ks'
						
					if lang == 'py':
						output.write("{0} ".format(word))
					else:
						print('--- ks begins here ---')
						
				output.write('\n')
			output.close()

		except IOError:
			print("The file could not be located.")
			
	#compiler(filepath, newFilepath)
</python>