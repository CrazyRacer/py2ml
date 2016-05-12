from six import u
from zc.zk import ZooKeeper

zk = ZooKeeper('zookeeper4.wohuafu.com:10155')
zk.delete_recursive('/dubbo')
#
#
#
# f = open('/Users/yupeng/Desktop/treeopmng', 'r')
# data = f.read()
# data = u(data)
# data = data.replace('u\'','\'')
# print data
# # print data
# zk.import_tree(data)

# zk.delete_recursive('/')
# zk.delete_recursive('/')
