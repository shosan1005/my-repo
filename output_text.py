import sys
import os

dir = sys.argv[1]
path = os.path.join(dir, "my_text.txt")
os.makedirs(dir)

f = open(path, 'a', encoding="utf-8")

f.write('こんにちは\n')

datalist = ['お元気ですか？\n', 'それではまた\n']
f.writelines(datalist)

f.close()