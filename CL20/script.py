import random

def pairs(a, word):
    splitList = a.split()
    newList = []
    x = [i for i, x in enumerate(splitList) if x == word]
    for i in x:
        try:
            if splitList[i+1] == splitList[i+1]:
                newList.append([splitList[i] , splitList[i+1]]) 
        except:
            IndexError
    listx = []
    for i in newList:
        if i not in listx:
            listx.append(i)
    newx = [' '.join(i) for i in listx]
    numList = []
    for i in newx:
        if a.count(i) == 0:
            numList.append(a.count(i)+1)
        else:
            numList.append(a.count(i))
    listy = []
    for i in newx:
        listy.append(i.split(' ',1)[1])
    return dict(zip(listy, numList))

def create_chain(s): 
    final = {} 
    splitList = s.split()
    for i in range(len(splitList)-1):
        final.update({splitList[i]: {}})
        for key, value in final.items():
            if len(value) == 0:
                value.update(pairs(s, key))
    return final

def get_next_word(chain, prev_word):
    if prev_word not in chain:
        return random.choice(list(chain.keys()))
    else:
        find = chain[prev_word]
        totalValue = sum(list(find.values()))
        randNum = random.randint(0, totalValue-1)
        for key, value in find.items():
            if randNum < value:
                return key
            else:
                randNum -= value
        return find

#print(get_next_word(create_chain('in the cat in the hat there is a picture of a cat in a hat.\nthe cat in the hat in the book the cat in the hat wears a hat and is a cat'),'in'))

def generate_text(chain, length):
    if list(chain.keys())[0] in chain:
        word = random.choice(list(chain.keys()))   
    string = ''
    while len(string) <= length:
        string += word + ' '
        word = get_next_word(chain, word)
    return string

#print(generate_text(create_chain('in the cat in the hat there is a picture of a cat in a hat.\nthe cat in the hat in the book the cat in the hat wears a hat and is a cat'), 100))

def read_file(file_path):
    with open(file_path, 'r', encoding='utf8') as fh:
        return fh.read()

def write_file(file_path, contents):
    with open(file_path, 'w', encoding='utf8') as fh:
        return fh.write(contents)

def run(input_path, output_path, length):
    text = read_file(input_path)
    chain = create_chain(text)
    result = generate_text(chain, length)
    write_file(output_path, result)

print(run('tp2e.txt', 'generated.txt', 1000))