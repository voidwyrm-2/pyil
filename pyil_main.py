from pathlib import Path
from random import randint


vaild_exts = [
    '.pyl',
    '.pyil',
    '.💩'
]


dontprint = ['']


symbols = ['!','@','#','$','%','^','&','*','(',')'
    #,''
]

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def minmax(input: int | float, min: int | float, max: int | float):
    if input < min: return min
    elif input > max: return max
    else: return input


def log(data):
    with open('LOG.txt', 'at') as logfile: logfile.write(str(data) + '\n')



DEBUG = [False, False]

#pointer storages
pointer = 0
pointers = []

#translation storage
transnums = []

#"is" bool
isa = None

#"if" bools
ifjump = False
elsejump = False
isif = False
iselse = False

#"goto" bool
cangoto = True

#function storages
funcs = []
gotfunc= False



def grab(file):
    tfile = ''
    for ext in vaild_exts:
        if Path(file + ext).exists(): tfile = file + ext

    if tfile == '': print(f'error: {file}.(pyl/pyil/💩) does not exist'); return ('', False)
    with open(tfile, 'rt') as fi: return (fi.read(), True)
    print('how did we get here?'); return ('', False)


def printline(lin):
    canprint = True
    liact = lin.split(' ')[0]
    for act in dontprint:
        if liact == act: canprint = False
    if canprint: print(lin)


def get(): getin = input('type a number below\n'); return int(getin)

def wait(): input('waiting for user...')

def translate(numbers: str | list | tuple):
    global letters
    tra = ''
    for lnum in list(numbers):
        lnum = minmax(lnum, 0, len(letters) - 1)
        tra = f'{tra}{letters[lnum]}'
    return f'translate: {tra}'

def encrypt(numbers: str | list | tuple):
    global symbols
    enc = ''
    for enum in list(numbers):
        enum = minmax(enum, 0, len(symbols) - 1)
        enc = f'{enc}{symbols[enum]}'
    return f'encrypt: {enc}'

def stitchfunc(facts: str):
    out = ''
    sfacts = facts.split('/')
    for fac in sfacts:
        #print(f'sfac:{sfac}')
        out = f'{out}{fac.replace(",", " ")}\n'
    return out.removesuffix('\n')



def trueparse(line: str):
    shouldwork = True ##if this is true, the program works flawlessly, but otherwise it breaks with no explaination
    global pointer
    global isa
    global ifjump
    global elsejump
    global isif
    global iselse
    global cangoto
    global transnums
    global funcs
    #print('line: ' + line)
    sl = line.split(' ')
    #print(sl)
    #print(sl)
    #print(type(sl))

    if DEBUG[0]: print(f'isa:{isa}, ifjump:{ifjump}, elsejump:{elsejump}, iselse{iselse}') ##debug info
    if DEBUG[1]: print(f'line:{line}') ##debug info


    if not ifjump and not elsejump:

        ##if the line starts with the do-not-run flag, don't parse
        if sl[0].startswith('##'): return

        ##if cangoto is false and the current action isn't goto, make it true
        if sl[0] != 'goto' and not cangoto: cangoto = True; pass

        ##print the pointer's current value to the console
        if sl[0] == 'print': print(f'pointer: {pointer}')

        ##add a number
        elif sl[0] == 'add':
            if sl[1] == 'get': pointer += get() ##if "get" is given as an instead of a number, add the user's input
            else: pointer += int(sl[1]) ##otherwise, add the given number

        ##subtract a number
        elif sl[0] == 'sub':
            if sl[1] == 'get': pointer -= get() ##if "get" is given as an instead of a number, subtract the user's input
            else: pointer -= int(sl[1]) ##otherwise, subtract the given number

        ##multiply by a number
        elif sl[0] == 'mul':
            if sl[1] == 'get': pointer *= get() ##if "get" is given as an instead of a number, multiply by the user's input
            else: pointer *= int(sl[1]) ##otherwise, multiply by the given number

        ##divide by a number
        elif sl[0] == 'div':
            if sl[1] == 'get': pointer //= get() ##if "get" is given as an instead of a number, divide by the user's input
            else: pointer //= int(sl[1]) ##otherwise, divide by the given number

        ##make the counter 0
        elif sl[0] == 'zero': pointer = 0

        ##waits for the user to give any input at all
        elif sl[0] == 'wait': wait()

        ##makes the pointer the given number
        elif sl[0] == 'make': pointer = int(sl[1])

        ##if the pointer is the second number, make it the first number
        elif sl[0] == 'let':
            antilet = False
            if len(sl) == 3:
                if '!' in sl[2]: antilet = True ##if the second number has the "!" prefix, instead if the pointer IS NOT the second number, make it the first number

                if antilet:
                    if pointer != int(sl[2].replace('!', '')): pointer = int(sl[1])
                else:
                    if pointer == int(sl[2]): pointer = int(sl[1])
            else:
                if pointer == 0: pointer = int(sl[1]) ##if no second number given, make it the first number if the pointer is 0

        ##get a number from the user and make the pointer that number
        elif sl[0] == 'get': pointer = get()

        ##checks then says if it is or is not the given number
        elif sl[0] == 'is':
            if pointer == int(sl[1]): print(f'pointer is {sl[1]}'); isa = True
            else: print(f'pointer is not {sl[1]}'); isa = False

        elif sl[0] == 'if':
            #print(f'got {bool(sl[1])} from the bool')
            if isa != bool(sl[1]): ifjump = True; iselse = True#; print('got "is False"')
            else: ifjump == False; isif = True#; print('got "is True"')

        ##if the action is "else" and we ran the if's actions, skip the else's actions
        elif sl[0] == 'else' and isif: elsejump = True

        #elif sl[0] == 'end': None

        ##clear the list of numbers to translate
        elif sl[0] == 'cleartrans': transnums.clear()

        ##add the current pointer's value to the list of numbers to translate
        elif sl[0] == 'totrans': transnums.append(pointer)

        ##translate all the numbers in the list of numbers to translate
        elif sl[0] == 'trans':
            if sl[1] == 'L': print(translate(transnums))
            elif sl[1] == 'E': print(encrypt(transnums))
            else: print(f'(trans) unknown input "{sl[1]}"')

        ##generates a random number between the given numbers
        elif sl[0] == 'rand':
            rand = 0
            rand = randint(int(sl[-2]), int(sl[-1]))
            #log(f'rand: got "{rand}"!')
            #print(f'rand: got "{rand}"!')
            if len(sl) >= 4:
                if sl[1] == 'add': pointer += rand
                elif sl[1] == 'sub': pointer -= rand
                elif sl[1] == 'mul': pointer *= rand
                elif sl[1] == 'div': pointer //= rand
                elif sl[1] == 'make': pointer = rand
            else: pointer = rand ##otherwise, make the pointer the generated number

        ##adds a new instance of the given object; currently only works with the pointer
        elif sl[0] == 'new':
            if len(sl) >= 3: ##if it has more inputs than just two
                if sl[1] == 'pointer':
                    if sl[2] == 'P': pointers.append(pointer) ##if it is "P", add a new instance of the pointer with the same value as the main pointer
                    else: pointers.append(int(sl[2])) ##otherwise, add a new instance of the pointer with the given value
            else: ##otherwise
                if sl[1] == 'pointer': pointers.append(0) ##if it is "pointer", add a new instance of the pointer with a value of 0

        elif sl[0] == 'func':
            sfunc = sl[1].split(':')
            funcs.append((sfunc[0], stitchfunc(sfunc[1])))

        elif sl[0] == 'funcs':
            funccount = 0
            for func in funcs:
                pfunc = func[0], func[1].replace("\n", '/')
                print(f'{funccount}-{pfunc[0]}({pfunc[1]})')

        elif sl[0] == 'funcdel': del funcs[int(sl[1])]

        elif sl[0] == 'funcsclear': funcs.clear()

        ##prints each pointer instance that is not the main pointer and its value
        elif sl[0] == 'pointers':
            pt = 0
            for poi in pointers: print(f'{pt}({poi})'); pt += 1
            #print(f'total pointers: {pt}')

        ##"print" action for pointer instances that aren't the main pointer
        elif sl[0] == 'pointerget': print(f'pointer({sl[1]}): {pointers[int(sl[1])]}')

        ##"make" action for pointer instances that aren't the main pointer
        elif sl[0] == 'pointerset': pointers[int(sl[1])] = int(sl[2])

        ##sets the main pointer to the given pointer instance
        elif sl[0] == 'topointer': pointer = pointers[int(sl[1])]

        ##"add" action for pointer instances that aren't the main pointer
        elif sl[0] == 'pointeradd':
            if sl[2] == 'P': pointers[int(sl[1])] += pointer
            else: pointers[int(sl[1])] += int(sl[2])

        ##if it's not a valid action and it's not empty, treat it as a comment and print it to the console
        else:
            if sl[0] != 'else' and sl[0] != 'end' and sl[0] != 'goto' and sl[0] != '': print(line) ##otherwise print it to the console

    elif ifjump and sl[0] == 'else': ifjump = False; iselse == True; print

    elif elsejump and sl[0] == 'end': ifjump = False; elsejump = False; isif = False; iselse == False; isa = None#; print('found "end"! continuing as normal!')

    else: print('how did we get here, after the else and end?')
        #if sl[0] == 'else': ifjump = False; elsejump = False; iselse == False

    #elif iselse: None
        #if sl[0] == 'end': ifjump = False; elsejump = False; iselse == False; isa = None


def runfunc(funcindex: int, funcname: str):
    global gotfunc
    global funcs; thefunc = funcs[funcindex]
    if thefunc[0] == funcname:
        thefuncacts = thefunc[1].split('\n')
        for funcl in thefuncacts: trueparse(funcl)
    gotfunc = False


def fakeparse(input: tuple):
    global pointer
    global cangoto
    global isa
    global ifjump
    global elsejump
    global isif
    global iselse
    global gotfunc
    #print('whaaat?')
    if not input[1]: return ##small do-not-run check
    sinp = input[0].split('\n') ##split the input by lines
    #print(f'sinp: {sinp}')
    #print(sinp)
    maxlines = len(sinp) ##gets the amount of lines
    #print(f'maxlines:{maxlines}')
    lineindex = 0 ##the current line
    while lineindex != maxlines: ##if we have not reached the end of the file
        l = sinp[lineindex] ##get the contents of the current line
        #log(f'lineindex:{lineindex + 1}("{l}")')
        #print(l.split(' '))

        if l.split(' ')[0] == 'return' or l.split(' ')[0] == 'break' or l.split(' ')[0] == 'stop': ##if it's "return/break/stop", stop parsing the code completely
            #print('twas quit')
            break
        
        elif l.split(' ')[0] == 'loop': ##if it's "loop", repeat the given action the given amount of times
            #print('loop found!')
            for i in range(int(l.split(' ')[1])): trueparse(l.split(' ')[2] + ' ' + l.split(' ')[3])

        elif l.split(' ')[0] == 'goto' and cangoto: ##if it's "goto", 
            if len(l.split(' ')) == 2:
                toline = int(l.split(' ')[1]) - 1 ##gets the given line to go to
                toline = minmax(toline, 0, maxlines - 1) #stops it from being too large or small
                #log(f'HEY, TOLINE IS "{toline}" AFTER THE MINMAX')
                lineindex = toline ##makes the current line the given line to go to

            else: lineindex = -1 ##if a line to go to isn't given, go to the first line of the file

            #if len(l.split(' ')) != 3: cangoto = False
            #else:
                #if l.split(' ')[2] != 'rep': cangoto = False
            cangoto = False
            #ifjump = False; elsejump = False; isif = False; iselse == False; isa = None
            #ifjump = False; elsejump = False; isif = False; iselse == False; isa = None

        elif l.split(' ')[0] == 'lines': print(f'line count: {maxlines}') ##if it's "lines", give the amount of lines in the file

        else:
            print(funcs)
            functicker = 0
            for fun in funcs:
                print(f'checking {fun}...')
                if l == fun[0]: print(f'found match!({l}=={fun[0]})'); gotfunc = True; runfunc(functicker, fun)
                else: functicker += 1

            if not gotfunc: trueparse(l) ##otherwise parse it as pyil code
        
        if cangoto: lineindex += 1 ##increment the current line by 1

def parsegrab(file): fakeparse(grab(file))

print('''welcome to the pyil interpreter!

type a vaild pyil action to run it
type "file/run [file name, not including extension]" to run a file; file must be a .pyl or .pyil
type "reset" to reset the pointer to zero(0)''')
running = True
while running:
    inp = input('input argument below\n') ##get a user's input
    #print(f'inp:"{inp}"')
    if inp.split(' ')[0] == 'reset': pointer = 0; print('pointer reset to zero') ##if "reset", reset the counter to 0
    elif inp.split(' ')[0] == 'file' or inp.split(' ')[0] == 'run': parsegrab(inp.split(' ')[1]) ##if "file", get the contents of the given file
    else: fakeparse((inp, True)) ##otherwise parse the arguments as pyil code