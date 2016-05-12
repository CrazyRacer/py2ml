from zc.zk import ZooKeeper


def export_node(host, path='/com'):
    zk = ZooKeeper(host)
    data = zk.export_tree(path)
    return data


def import_node(host, data):
    zk = ZooKeeper(host)
    zk.import_tree(data)
