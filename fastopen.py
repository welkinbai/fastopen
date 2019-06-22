#!/usr/local/opt/python/bin/python3.7
import os
import sys
import time

dbfile = '/Users/leyan/baixiaoxuan/pyhome/fastopen.data'
chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
closeChromeScript = '/Users/leyan/baixiaoxuan/pyhome/closeChrome.scpt'
argLen = len(sys.argv)
opt = ''
key = ''
value = ''
if argLen == 3:
    if sys.argv[1] == 'k':
        opt = 'killopen'
        key = sys.argv[2]
    else:
        opt = 'save'
        key = sys.argv[1]
        value = sys.argv[2]
elif argLen == 2:
    if sys.argv[1] == 'k':
        opt = 'kill'
    elif sys.argv[1] == 'h':
        opt = 'help'
    elif sys.argv[1] == 'l':
        opt = 'list'
    else:
        opt = 'open'
        key = sys.argv[1]
else:
    print('非法参数个数')
    sys.exit()


def save():
    newLines = []
    with open(dbfile, 'r') as f:
        lines = f.readlines()        
        existLine = False
        for line in lines:
            lineKV = line.split(sep=':', maxsplit=1)
            if key == lineKV[0]:
                newLines.append(key+':'+value+'\n') 
                existLine = True
            else:
                newLines.append(line)
        if not existLine:
            newLines.append(key+':'+value+'\n')
    with open(dbfile, 'w') as f:
        f.writelines(newLines)
    pass


def fopen():
    target = None
    with open(dbfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            lineKV = line.split(sep=':', maxsplit=1)
            if key == lineKV[0]:
                target = lineKV[1]
                break
    if target != None:
        os.system('open -a "'+chromePath+'" '+target)
    else:
        print('未找到链接，请通过 fop key value 形式预先存储链接')
    pass


def kill():
    os.system('osascript '+closeChromeScript)
    pass

def printHelp():
    print('fastOpen(快速打开)工具帮助：')
    print('使用 fop key value 形式为链接地址存储别名')
    print('使用 fop key形式快速打开链接')
    print('使用 fop k 即参数k来快速关闭浏览器')
    print('使用 fop k key即参数k+key来快速关闭浏览器,同时打开key对应的链接')
    print('使用 fop h 即参数h来查看本帮助')
    pass

def listAll():
    with open(dbfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
    pass

if opt == 'save':
    save()
elif opt == 'open':
    fopen()
elif opt == 'kill':
    kill()
elif opt == 'killopen':
    kill()
    time.sleep(1)
    fopen()
elif opt == 'help':
    printHelp()
elif opt == 'list':
    listAll()
else:
    print("未知操作符")
    sys.exit()

