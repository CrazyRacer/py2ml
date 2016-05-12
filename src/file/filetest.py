list=[]
for i in range(3000,10000):
    list.append(str(186000)+("%05d" % i))

f  = open('/Users/yupeng/Desktop/mobile','w')

for l in list:
   f.write(str(l)+"\n")