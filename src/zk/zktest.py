# coding=utf-8
from kazoo.client import KazooClient
from zc.zk import ZooKeeper
import zc.zk
import json

# zk = ZooKeeper('zookeeper1.wohuafu.com:10013')
# data =zk.export_tree('/')

zk2 = ZooKeeper('zookeeper4.wohuafu.com:10155')

# f = open('/Users/yupeng/Desktop/zknode','r')


data = zk2.export_tree('/com')
f = open("/Users/yupeng/Desktop/treeopmng",'w')
f.write(data)
# print data.decode('utf_8')
# u = u'111'
# print u


# list2[i]=str()

# for l in list2:
#     print l
#     print list2[l]
#     print zk.create_recursive(l,list2[l],None)
