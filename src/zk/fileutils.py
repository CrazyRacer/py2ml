def writefile(data, path):
    f = open(path, 'w')
    f.write(data)


def readfile(path):
    f = open(path, 'r')
    return f.read()
