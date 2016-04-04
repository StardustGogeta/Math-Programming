#filepath = input("Where is the file you want to convert? (It will not be overwritten.)\n").replace('"','')
#newFilepath = input("Where would you like to save the file?\n").replace('"','')
##filepath = '.\Test.py'
##newFilepath = '.\CompileTest.cpp'
def compiler(filepath, newFilepath):
    def includeDefs(word):
        return {
            'import'    : '#include',
            'math'      : '<cmath>',
            'from'      : '',
            '*'         : libs(fromStorage)
            }.get(word,'/* ERROR! */')

    def libs(lib):
        return {
            'math'      : '<cmath>',
            '*'         : fromStorage
            }.get(lib,'/* ERROR! */')

    try:
        file = open(filepath)
        words = file.read().splitlines()
        file.close()
        # This is where the transcribing begins.
        output = open(newFilepath,'w')
        phraseType = 'unknown'
        global fromStorage
        fromStorage = ''
        # Parsing each line for a recognizable statement, and marking the syntax type.
        for line in words:
            line = line.split()
            print(line)
            for word in line:

                # Beginning with all possible statements before the main program.
                if word == 'from':
                    phraseType = 'from'
                    
                if word == 'import':
                    phraseType = 'include'
                    
                if phraseType == 'include':
                    word = includeDefs(word)

                if phraseType == 'from2':
                    fromStorage = word
                    word = ''
                    phraseType = 'unknown'

                if phraseType == 'from':
                    word = includeDefs(word)
                    phraseType = 'from2'

                # Moving on to more standard commands for C++.
                if word.split('(').count('print'):
                    word = word.split('(',1)
                    word[0] = 'cout << '
                    word = ' '.join(word)#.replace(',','<<').replace('+','<<')
                    
                    
                output.write("{0} ".format(word))
            output.write('\n')
            phraseType = 'unknown'
            fromStorage = ''
        #output.write(words)
        output.close()

    except IOError:
        print("The file could not be located.")
