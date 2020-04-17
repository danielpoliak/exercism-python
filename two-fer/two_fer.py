def two_fer(name={}):
    if name is two_fer.__defaults__[0]:
        sentence = "One for you, one for me."
        return sentence
    else:
        sentence = "One for {name}, one for me.".format(name = name)
        return sentence
