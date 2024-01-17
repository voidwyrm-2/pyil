INPUT = ['print', 'add', 'sub', 'mul', 'div', 'zero', 'make', 'get', 'is', 'goto'], '|'

OUTS = ['print', 'file']
out = 0



def form(input: str): return input.replace('<class \'', '').replace('\'>', '')


inrange = 0
intype = form(str(type(INPUT[0])))
#print(intype)
if intype == 'int': inrange = INPUT[0]#; print('got int!')
elif intype == 'list' or intype == 'tuple': inrange = len(INPUT[0]); print('got list or tuple!')


final = ''
for n in range(inrange):
    inp = INPUT[0]
    if intype == 'int': final = f'{final}{n}{INPUT[1]}'
    elif intype == 'list' or intype == 'tuple': final = f'{final}{inp[n]}{INPUT[1]}'


if OUTS[out] == 'print': print(final)
elif OUTS[out] == 'file': None