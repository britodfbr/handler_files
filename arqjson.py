import json


def exemplo1(content, filename):
    """ Write JSON """
    with open(filename, 'w') as json_file:
        json.dump(content, json_file, indent=4)


def exemplo2(filename):
    with open(filename) as f:
        content = json.load(f)
    print(content)