from os import walk

def index_end(string, sub):
    #returns the next index after the end of the first occurrence of [sub] in [string]
    return string.index(sub) + len(sub)

def insert(string, index, sub):
    #returns a new string with [sub] inserted so the first character of [sub] is at [index] in [string]
    new_string = string[:index] + sub + string[index:]
    return new_string

f = []
for (dirpath, dirnames, filenames) in walk('_posts'):
    f.extend(filenames)
    break
f = sorted(f)[1:]
# print(f)

ep_list = []

for path in f:
    fin = open('_posts/' + path)
    text = str(fin.read())
    fin.close()
    ind = index_end(text, 'episode_title:')
    while text[ind].isspace():
        ind += 1
    title = ''
    while text[ind] != '\n':
        title += text[ind]
        ind += 1
    title = title.strip(' ').strip('\'').strip('"')
    ep_list.append(title)
    # fout = open('_posts/' + path, 'w')
    # fout.write(text)
    # fout.close()
# print(ep_dict)

for path in f:
    fin = open('_posts/' + path)
    text = str(fin.read())
    fin.close()
    ind = index_end(text, 'episode_title:')
    while text[ind].isspace():
        ind += 1
    title = ''
    while text[ind] != '\n':
        title += text[ind]
        ind += 1
    title = title.strip(' ').strip('\'').strip('"')
    ind = ep_list.index(title)
    string = ''
    if ind == 0:
        string = f'next_episode_title:\t\t{ep_list[ind + 1]}\n'
    elif ind == len(ep_list) - 1:
        string = f'prev_episode_title:\t\t{ep_list[ind - 1]}\n'
    else:
        string = f'prev_episode_title:\t\t{ep_list[ind - 1]}\nnext_episode_title:\t\t{ep_list[ind + 1]}\n'
    ind = text.index('episode_title:')
    text = insert(text, ind, string)
    fout = open('_posts/' + path, 'w')
    fout.write(text)
    fout.close()