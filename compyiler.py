from pathlib import Path



indir = 'compyil-in/'
outdir = 'compyil-out/'
out_ext = '.zpyl'

vaild_exts = [
    '.pyl',
    '.pyil',
    '.💩'
]

gottenfile = ''

def grabfile(file):
    global gottenfile
    gottenfile = ''
    for ext in vaild_exts:
        if Path(indir + file + ext).exists(): 
            with open(indir + file + ext, 'rt') as fin: gottenfile = file; return fin.read()
        else: print(f'error: {file}.(pyl/pyil/💩) does not exist'); return None

def savefile(data):
    global gottenfile
    with open(outdir + gottenfile + out_ext, 'xt') as fout: fout.write(str(data))

def compyil(readfile):
    if readfile == None: return
    final = ''
    rli = []
    flines = readfile.split('\n')
    for line in flines:
        if not '##' in line:
            li = line

            li = li.replace('print', 'pr')
            li = li.replace('add', 'a')
            li = li.replace('sub', 's')
            li = li.replace('mul', 'm')
            li = li.replace('div', 'd')
            li = li.replace('zero', 'z')
            li = li.replace('wait', 'w')
            li = li.replace('make', 'm')
            li = li.replace('let', 'l')
            li = li.replace('get', 'ge')
            li = li.replace('else', 'el')
            li = li.replace('end', 'en')
            li = li.replace('cleartrans', 'ct')
            li = li.replace('totrans', 'to')
            li = li.replace('trans', 'tr')
            li = li.replace('rand', 'r')
            li = li.replace('new', 'n')
            li = li.replace('func', 'f')
            li = li.replace('funcs', 'fs')
            li = li.replace('funcdel', 'fd')
            li = li.replace('funcsclear', 'fc')
            li = li.replace('pointer', 'ptr')
            li = li.replace('pointers', 'ps')
            li = li.replace('pst', 'pst')
            li = li.replace('topointer', 'tp')
            li = li.replace('pointeradd', 'pa')
            #li = li.replace('', '')
            #li = li.replace('', '')

            li = li.replace(' ', '|')
            rli.append(li)
    #print(rli)
    for i in rli:
        final = f'{final}{i}/>'
    final = final.removesuffix('/>')
    savefile(final)



def fileconsole():
    while True:
        finp = input('>>> ')
        if finp == 'exit': break
        else: compyil(grabfile(finp))


print('"exit" to exit the program\n"file" to compile a file\n"compall" to compile all files')
while True:
    inp = input('>> ')
    if inp == 'exit': break
    elif inp == 'file': fileconsole()
    #elif inp == 'compall': compyilall()
    else: print(f'unknown command "{inp}"')