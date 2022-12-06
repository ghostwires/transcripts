fin = open('etr_input.txt', 'rt')
text = fin.read()
fin.close()
new_text = ""
text = text.split('\n')
for line in text:
    if line.isdigit() or line == '' or line.isspace():
        continue
    if line in ('Rusty Quill Gaming – 12 – Keeeeeesh'):
        continue
    if line[:4] == 'Page' and line[-5:] == 'of 19':
        continue
    line = line.replace('’', '\'')
    line = line.replace('‘', '\'')
    line = line.replace('–', '-')
    line = line.replace(' -', ' --')
    if line[0].isdigit():
        line = line[3:]
    if line == line.upper():
        line = '#### ' + line.upper()
    # if line[-1] == ':':
    #     line = '#### ' + line[:-1].upper()
    new_text += line + '\n'
fout = open('etr_middle.txt', 'wt')
fout.write(new_text)
fout.close()

new_new_text = ""
new_text = new_text.split('\n')
for line in new_text:
    line = line.replace('“', '"').replace('”', '"')
    if line == '':
        continue
    if line[0] == "#":
        new_new_text += '\n\n' + line + '\n\n'
    else:
        new_new_text += line + ' '
fout = open('etr_output.txt', 'wt')
fout.write(new_new_text)
fout.close()
