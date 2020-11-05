def concat(*strings, sep=' '):
    concatenation = ""
    for word in strings[0:-1]:
        concatenation += word + sep
    concatenation += strings[-1]
    return concatenation
