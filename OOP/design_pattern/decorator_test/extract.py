import zipfile
import sys

zf=zipfile.ZipFile(sys.argv[1])
zf.extract(sys.argv[2])

