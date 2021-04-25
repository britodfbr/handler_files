import csv


#
def exemplo1(fieldnames, content, filename):
    """ Write CSV """
    with open(filename, 'w', newline='') as csvfile:
        handler = csv.DictWriter(csvfile, fieldnames=fieldnames)
        handler.writeheader()
        handler.writerow(content)

def exemplo2(content, filename):
    with open(filename, mode='w') as f:
        handler = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        handler.writerow(content)



# read
def exemplo3(filename):

    """ Read CSV """
    with open(filename, newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in handler:
            print(row)
