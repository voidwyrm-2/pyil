from pathlib import Path



def minmax(input: int | float, min: int | float, max: int | float):
    if input < min: return min
    elif input > max: return max
    else: return input


pointer = 0
isa = None
jump = False
iselse = False

def grab(file):
    if not Path(file + '.pyl').exists(): print(f'error: {file}.pyl does not exist'); return ('', False)
    with open(f'{file}.pyl', 'rt') as fi: return (fi.read(), True)
    print('how did we get here?'); return ('', False)


def get(): getin = input('type a number below\n'); return int(getin)


def trueparse(line: str):
    global pointer
    global isa
    global jump
    global iselse
    #print('line: ' + line)
    sl = line.split(' ')
    #print(sl)
    #print(sl)
    #print(type(sl))
    
    if (not jump and not iselse) or isa == None:
        if sl[0] == 'print': print(pointer)
    
        elif sl[0] == 'add': pointer += int(sl[1])
    
        elif sl[0] == 'sub': pointer -= int(sl[1])
    
        elif sl[0] == 'mul': pointer *= int(sl[1])
    
        elif sl[0] == 'div': pointer //= int(sl[1])
    
        elif sl[0] == 'zero': pointer = 0
    
        elif sl[0] == 'make': pointer = int(sl[1])

        elif sl[0] == 'get': pointer = get()
    
        elif sl[0] == 'is':
            if pointer == int(sl[1]): print(f'pointer is {sl[1]}'); isa = True
            else: print(f'pointer is not {sl[1]}'); isa = False

        elif sl[0] == 'if':
            print(f'got {bool(sl[1])} from the bool')
            if isa != bool(sl[1]): jump = True
            else: jump == False

        elif sl[0] == 'else' and isa != None: iselse = True

        elif sl[0] == 'goto': pass
            #sln = sl[1]
            #sln = minmax(sln, 0, len(sinp))
        
        else:
            if sl[0] != 'else' and sl[0] != 'end' and sl[0] != '': print(line)

    elif jump:
        if sl[0] == 'else': jump = False; iselse == True

    elif iselse:
        if sl[0] == 'end': jump = False; iselse == False; isa = None


def fakeparse(input: tuple):
    global pointer
    #print('whaaat?')
    if not input[1]: return
    sinp = input[0].split('\n')
    #print(sinp)
    for l in sinp:
        #print(l.split(' '))
        if l.split(' ')[0] == 'return' or l.split(' ')[0] == 'break' or l.split(' ')[0] == 'stop':
            #print('twas quit')
            break
        elif l.split(' ')[0] == 'loop':
            #print('loop found!')
            for i in range(int(l.split(' ')[1])): trueparse(l.split(' ')[2] + ' ' + l.split(' ')[3])
        else:
            #print('got else in fakeparse!')
            trueparse(l)

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