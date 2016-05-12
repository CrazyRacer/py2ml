import zkutils
import fileutils
import sys

if __name__ == '__main__':
    data = zkutils.export_node(sys.argv[1], sys.argv[2])
    fileutils.writefile(data, sys.argv[3])
