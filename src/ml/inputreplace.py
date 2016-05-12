f = open('test.txt', 'r')
lines = f.readlines()
list = []
for line in lines:
    line = line.strip()
    strarray = line.split('\t')
    if strarray[-1] == 'largeDoses':
        strarray[-1] = 2
    elif strarray[-1] == 'didntLike':
        strarray[-1] = 0
    elif strarray[-1] == 'smallDoses':
        strarray[-1] = 1
    list.append(strarray)

f = open('test2.txt', 'w')
for l in list:
    l[-1] = str(l[-1])+'\n'
    f.write('\t'.join(l))
