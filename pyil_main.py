from pathlib import Path



def minmax(input: int | float, min: int | float, max: int | float):
    if input < min: return min
    elif input > max: return max
    else: return input


DEBUG = [False, False]

pointer = 0

isa = None

ifjump = False
elsejump = False
iselse = False

cangoto = True

def grab(file):
    if not Path(file + '.pyl').exists(): print(f'error: {file}.pyl does not exist'); return ('', False)
    with open(f'{file}.pyl', 'rt') as fi: return (fi.read(), True)
    print('how did we get here?'); return ('', False)


def get(): getin = input('type a number below\n'); return int(getin)

def wait(): input('waiting for user...')


def trueparse(line: str, lis: list):
    global pointer
    global isa
    global ifjump
    global elsejump
    global iselse
    #print('line: ' + line)
    sl = line.split(' ')
    #print(sl)
    #print(sl)
    #print(type(sl))
    
    if DEBUG[0]: print(f'isa:{isa}, ifjump:{ifjump}, elsejump:{elsejump}, iselse{iselse}')
    if DEBUG[1]: print(f'line:{line}')

    if (not ifjump and not elsejump) or (iselse or isa == None):
        if sl[0].startswith('##'): return

        if sl[0] == 'print': print(f'pointer: {pointer}')
    
        elif sl[0] == 'add':
            if sl[1] == 'get': pointer += get()
            else: pointer += int(sl[1])
    
        elif sl[0] == 'sub':
            if sl[1] == 'get': pointer -= get()
            else: pointer -= int(sl[1])
    
        elif sl[0] == 'mul':
            if sl[1] == 'get': pointer *= get()
            else: pointer *= int(sl[1])
    
        elif sl[0] == 'div':
            if sl[1] == 'get': pointer //= get()
            else: pointer //= int(sl[1])
    
        elif sl[0] == 'zero': pointer = 0

        elif sl[0] == 'wait': wait()
    
        elif sl[0] == 'make': pointer = int(sl[1])

        elif sl[0] == 'let':
            if len(sl) == 3:
                if pointer == int(sl[2]): pointer = int(sl[1])
            else:
                if pointer == 0: pointer = int(sl[1])


        elif sl[0] == 'get': pointer = get()
    
        elif sl[0] == 'is':
            if pointer == int(sl[1]): print(f'pointer is {sl[1]}'); isa = True
            else: print(f'pointer is not {sl[1]}'); isa = False

        elif sl[0] == 'if':
            #print(f'got {bool(sl[1])} from the bool')
            if isa != bool(sl[1]): ifjump = True; elsejump = False#; print('got "is False"')
            else: ifjump == False; elsejump = True#; print('got "is True"')

        elif sl[0] == 'else' and isa != None: iselse = True

        
        else:
            if sl[0] != 'else' and sl[0] != 'end' and sl[0] != 'goto' and sl[0] != '': print(line)

    elif ifjump:
        if sl[0] == 'else': ifjump = False; iselse == True

    elif elsejump:
        #if sl[0] == 'else': ifjump = False; elsejump = False; iselse == False
        if sl[0] == 'end': ifjump = False; elsejump = False; iselse == False; isa = None

    elif iselse:
        if sl[0] == 'end': ifjump = False; elsejump = False; iselse == False; isa = None


def fakeparse(input: tuple):
    global pointer
    global cangoto
    #print('whaaat?')
    if not input[1]: return
    sinp = input[0].split('\n')
    #print(f'sinp: {sinp}')
    #print(sinp)
    maxlines = len(sinp)
    #print(f'maxlines:{maxlines}')
    lineindex = 0
    while lineindex != maxlines:
        #print(f'lineindex:{lineindex}')
        l = sinp[lineindex]
        #print(l.split(' '))
        if l.split(' ')[0] == 'return' or l.split(' ')[0] == 'break' or l.split(' ')[0] == 'stop':
            #print('twas quit')
            break
        elif l.split(' ')[0] == 'loop':
            #print('loop found!')
            for i in range(int(l.split(' ')[1])): trueparse(l.split(' ')[2] + ' ' + l.split(' ')[3], sinp)
        elif l.split(' ')[0] == 'goto' and cangoto:
            if len(l.split(' ')) == 2:
                toline = int(l.split(' ')[1])
                toline = minmax(toline, 0, maxlines - 1)
                lineindex = toline
                
            else: lineindex = 0
            cangoto = False
        elif l.split(' ')[0] == 'lines': print(f'line count: {maxlines}')
        else:
            #print('got else in fakeparse!')
            trueparse(l, sinp)
        lineindex += 1

def parsegrab(file): fakeparse(grab(file))

print('''welcome to the pyil interpreter!

type a vaild pyil action to run it
type "file" or "run" [file name, not including extension] to run a file; file must be a .pyl
type "reset" to reset the pointer to zero(0)''')
running = True
while running:
    inp = input('input argument below\n')
    #print(f'inp:"{inp}"')
    if inp.split(' ')[0] == 'reset': pointer = 0; print('pointer reset to zero')
    elif inp.split(' ')[0] == 'file' or inp.split(' ')[0] == 'run': parsegrab(inp.split(' ')[1])
    else: fakeparse((inp, True))