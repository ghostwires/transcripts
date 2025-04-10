#before running this program you must have a file named "etr_input.txt" in the same folder as this program (edit_transcript.py). copy the result of your TXT file
fin = open('etr_input.txt', 'rt')
text = fin.read()
fin.close()
new_text = ""
text = text.split('\n')
for line in text:
    if line.isdigit() or line == '' or line.isspace():
        #gets rid of blank spaces or page numbers
        #it does sometimes accidentally eat the numbers that are results of dice rolls, however. if you want to avoid that you can delete the "line.isdigit()" at the beginning so it doesn't eat any numbers
        continue
    if line in ('©Rusty Quill 2024', 'Private & Confidential', 'V3.1', '12-09-2023', 'Inexplicables – E03 – Public Speaking') or line.startswith("Page ") or (len(line) >= 3 and line[1:len(line)-1].isdigit()):
        #put any recurring lines you notice up here. the episode title usually is one, since it occurs in the header of each page on the PDF
        continue
    # if line[:4] == 'Page' and line[-5:] == 'of 19':
    #     continue
    line = line.replace('’', '\'')
    line = line.replace('', '') #gets rid of invisible unicode character (000c)
    line = line.replace('‘', '\'')
    line = line.replace('–', '-')
    line = line.replace('—', '-')
    line = line.replace(' -', ' --')
    line = line.replace('…', '...')
    # if line[0].isdigit():
    #     line = line[3:]
    if line[0] == '[':
        line = '##### ' + line
    elif line.strip("(cont'd)") == line.upper():
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
#copy and paste the result from etr_output.txt!