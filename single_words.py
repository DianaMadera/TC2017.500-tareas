def single_words(string):
    output = []
    seen = set()
    for word in string.split():
        if word not in seen:
            output.append(word)
            seen.add(word)
    return ' '.join(output)

string = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
print(single_words(string))