filename = '2022-10-18-007.md'
fin = open('_posts/' + filename, 'rt')
read = fin.read()
fin.close()
fout = open('_posts/' + filename, 'wt')
for line in read.split('\n'):
    if line[:4] == '####':
        line = line.upper()
    fout.write(line + '\n')
fout.close()