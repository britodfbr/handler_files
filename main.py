import settings
from pathlib import Path
from handler_files import arqtxt, arqcsv, arqjson, arqxlsx


path = Path(settings.DIR_OUTPUT).absolute()
path.mkdir(exist_ok=True)

header = ['nome', 'ramal', 'email' ,'celular', 'data aniversário']
content = {'nome': 'João da Silva', 
'ramal': '9999',
'email': 'joao@email.com',
'celular': '(61)9999-9999',
'data aniversário': '1.1.2001'}


if __name__ == '__main__':
    arqtxt.exemplo1('Jesus te ama!')
    arqtxt.exemplo2('Jesus te ama!', path/'exemplo2.txt')
    arqtxt.exemplo3('Jesus te ama!', path/'exemplo3.txt')
    print(arqtxt.exemplo4(path/'file.txt'))
    print(arqtxt.exemplo5(path/'file.txt'))
    print(arqtxt.exemplo6(path/'exemplo3.txt'))
    arqcsv.exemplo1(header, content, path/'file.csv')
    arqcsv.exemplo2(header, path/'file1.csv')
    arqcsv.exemplo3(path/'file.csv')
    arqjson.exemplo1(content, path/'file.json')
    arqjson.exemplo2(path/'file.json')
    print(content.items())
    arqxlsx.exemplo1(content.items(), path/'file.xlsx')
