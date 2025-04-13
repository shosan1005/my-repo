import sys

path = sys.argv[1]

f = open(path, 'a', encoding="utf-8")

f.write('こんにちは\n')

datalist = ['お元気ですか？\n', 'それではまた\n']
f.writelines(datalist)

f.close()