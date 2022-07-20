from os import walk

def index_end(string, sub):
    #returns the next index after the end of the first occurrence of [sub] in [string]
    try:
        return string.index(sub) + len(sub)
    except:
        return -1

def insert(string, index, sub):
    #returns a new string with [sub] inserted so the first character of [sub] is at [index] in [string]
    new_string = string[:index] + sub + string[index:]
    return new_string

def delete(string, index, sub):
    new_string = string[:index] + string[(index + len(sub)):]
    return new_string

f = []
for (dirpath, dirnames, filenames) in walk('_posts'):
    f.extend(filenames)
    break
f = sorted(f)
# print(f)

for path in f:
    fin = open('_posts/' + path)
    text = str(fin.read())
    fin.close()
    try:
        ind = index_end(text, "prev_categories:")
        if ind < 0:
            pass
        else:
            while text[ind].isspace():
                ind += 1
            endind = ind
            while text[endind] != ']':
                endind += 1
            prev_categories = text[(ind + 1):(endind)].split(',')
            # print(prev_categories)
            prev_prefixes = []
            for cat in prev_categories:
                if cat == '"tma"':
                    prev_prefixes.append('"MAG"')
                elif cat == '"rqg"':
                    prev_prefixes.append('"RQG"')
            addition = ', '.join(prev_prefixes)
            # print(addition)
            ind = index_end(text, "prev_prefixes:")
            while text[ind].isspace():
                ind += 1
            ind += 1
            text = insert(text, ind, addition)
    except:
        pass
    try:
        ind = index_end(text, "next_categories:")
        if ind < 0:
            pass
        else:
            while text[ind].isspace():
                ind += 1
            endind = ind
            while text[endind] != ']':
                endind += 1
            next_categories = text[(ind + 1):(endind)].split(',')
            # print(next_categories)
            next_prefixes = []
            for cat in next_categories:
                if cat == '"tma"':
                    next_prefixes.append('"MAG"')
                elif cat == '"rqg"':
                    next_prefixes.append('"RQG"')
            addition = ', '.join(next_prefixes)
            # print(addition)
            ind = index_end(text, "next_prefixes:")
            while text[ind].isspace():
                ind += 1
            ind += 1
            text = insert(text, ind, addition)
    except:
        pass
    fout = open('_posts/' + path, 'w')
    fout.write(text)
    fout.close()