fin = open('etr_input.txt', 'rt')
text = fin.read()
fin.close()
new_text = ""
text = text.split('\n')
for line in text:
    line = line.replace("Rusty Quill Gaming – SEAS - Below Deck 2", "").strip("")
    line = line.replace('’', '\'')
    line = line.replace('‘', '\'')
    line = line.replace('–', '-')
    line = line.replace(' -', ' --')
    if line.isdigit() or line == '' or line.isspace():
        continue
    if line[0] == '[':
        line = '##### ' + line.upper()
    elif line.upper() == line:
        line = '#### ' + line
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