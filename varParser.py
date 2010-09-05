import string, sys, re, os

print '###########################################################'
print '[*]FASL Variable Declaration Type Error Scanner           #'
print '[*]Author: Sujit Ghosal                                   #'
print '[*]Mail: thesujit@gmail.com                               #'
print '[*]Copyright: SecPod Technologies                         #'
print '[*]Website: http://www.secpod.com                         #'
print '[*]All rights reserved.                                   #'
print '###########################################################\n'

def variableScanner(file):
    # Parse the variable names which are initialized in their in-correct methods.
    try:
        file = sys.argv[1]
        ext = os.path.splitext(file)
        if ext[1] == '.fasl3':
            print '[+]Parsing variables inside the program code.'
        elif not ext[1] == '.fasl3':
            print '[+]Wrong filename passed to the parameters list.'
            print '[+]Usage: python parser.py script-name.fasl3'
            sys.exit(0)
        fObj = open(file, 'r')
        incorrect = []
        for lines in fObj:
            lines = lines.strip()
            incFilter = re.findall('^\w+ = ', lines)
            for variables in incFilter:
                if variables:
                    items = string.replace(variables, ' = ', '')
                    incorrect.extend(items.split())
                    #print str(incorrect)
                elif not variables:
                    print '[+]No variables found.'
                    sys.exit(0)
                elif len(variables) <= 0:
                    print '[+]Incorrect variable declaration not found. Program terminating'
                    sys.exit(0)
        fObj.close()

    except IOError:
        print '[+]File not found.'
        print '[+]Please input the file name correctly!'

    # Parse the variable names which are initialized in their correct methods.
    try:
        fObj2 = open(file, 'r')
        correct = []
        for varLines in fObj2:
            varLines = varLines.strip()
            varFilters = re.findall('var\ \w+', varLines)
            for patterns in varFilters:
                if patterns:
                    varItems = string.replace(patterns, 'var ', '')
                    correct.extend(varItems.split())
                    #print str(correct)
                elif not patterns:
                    print '[+]No variable initialization keyword found.'
                    sys.exit(0)
        fObj2.close()

    except IOError:
        print '[+]No var built-in keyword usage found in the code.'

    print '[+]Number of correct variables found    :', int(len(correct))
    print '[+]Number of in-correct variables found :', int(len(incorrect))

    print '\n[+]Correct Variables Name List:'
    for corData in correct:
        print '   >>', corData
    print '[+]Incorrect Variables Name List:'
    for incData in incorrect:
        print '   >>', incData

    print '\n<<  <<  <<  PARSING RESULT  >>  >>  >>'
    print '.......................................'
    diffResult = list(set(incorrect).difference(correct))
    if len(diffResult) > 0:
        print '[+]Probably these are the incorrect variables names list:'
        for unInit in diffResult:
            print '   >>', str(unInit)
    else:
        print '[+]No variable initialization errors found in this script.'

def main():
    if len(sys.argv) > 2:
        print '[+]Wrong number of arguments passed.'
        print '[+]Usage: python parser.py script-name.fasl3'
        sys.exit(0)

if __name__ == "__main__":
    main()
    call = variableScanner(file)
