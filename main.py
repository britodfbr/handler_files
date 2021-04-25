import settings
from pathlib import Path
from arqtxt import (exemplo1, exemplo2, exemplo3, exemplo4, exemplo5, exemplo6)
import arqcsv
import arqjson
import arqxlsx


path = Path(settings.DIR_OUTPUT)
path.mkdir(exist_ok=True)

header = ['nome', 'ramal', 'email' ,'celular', 'data aniversário']
content = {'nome': 'João da Silva', 
'ramal': '9999',
'email': 'joao@email.com',
'celular': '(61)9999-9999',
'data aniversário': '1.1.2001'}


if __name__ == '__main__':
    exemplo1('Jesus te ama!')
    exemplo2('Jesus te ama!', path/'exemplo2.txt')
    exemplo3('Jesus te ama!', path/'exemplo3.txt')
    print(exemplo4(path/'file.txt'))
    print(exemplo5(path/'file.txt'))
    print(exemplo6(path/'exemplo3.txt'))
    arqcsv.exemplo1(header, content, path/'file.csv')
    arqcsv.exemplo2(header, path/'file1.csv')
    arqcsv.exemplo3(path/'file.csv')
    arqjson.exemplo1(content, path/'file.json')
    arqjson.exemplo2(path/'file.json')
    print(content.items())
    arqxlsx.exemplo1(content.items(), path/'file.xlsx')
