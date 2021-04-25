import os
import pathlib
import settings


# Write
def exemplo1(content: str):
    # 1ª forma
    f = open(f'{settings.DIR_OUTPUT}/file.txt', 'w')
    f.write(content)
    f.close()


def exemplo2(content, filename):
    # 2ª
    with open(filename, 'w') as f:
        f.write(content)


def exemplo3(content, filename):
    pathlib.Path(filename).write_text(content)


#read
def exemplo4(filename):
    f = open(filename)
    content = f.read()
    f.close()
    return content

def exemplo5(filename):
    with open(filename) as f:
        return f.read()

def exemplo6(filename):
    return pathlib.Path(filename).read_text()
