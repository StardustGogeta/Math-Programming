import re

#filepath = 'Test.ks'
#newFilepath = 'test.py'

def compiler(filepath, newFilepath):
    
    def tags(word):
        return {
            'python' : 'py'
            }.get(word,'ks')

    try:
        file = open(filepath)
        words = file.read().splitlines()
        file.close()
        output = open(newFilepath,'w')
        lang = 'ks'
        # Parsing each line for a recognizable statement.
        for line in words:
            if lang == 'py':
                if re.match("</python>", line):
                    lang = 'ks'
                    line = ''
                s = re.match('(?P<s>\s*.*)', line)
                line = line.split()
                output.write(s.group('s')[1:])
            else:
                startTag = re.match("<(?P<lang>.*)>", line)
                printing = re.match(">\s*(?P<a>.*)", line)
                reading = re.match("<\s*(?P<a>[^,]*)(,(?P<b>.*[^>]))?", line)
                if startTag:
                    lang = tags(startTag.group('lang'))
                elif printing:
                    output.write('print('+printing.group('a')+')')
                elif reading:
                    output.write(reading.group('a')+" = input(")
                    if reading.group('b'):
                        output.write(reading.group('b'))
                    output.write(")")
                else:
                    output.write('# Unrecognized syntax: '+line)
            output.write('\n')
        output.close()

    except IOError:
        print("The file could not be located.")
        
#compiler(filepath, newFilepath)
