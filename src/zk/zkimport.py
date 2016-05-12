import zkutils
import fileutils
import sys

if __name__ == '__main__':
    data = fileutils.readfile(sys.argv[1])
    zkutils.import_node(sys.argv[2], data)
