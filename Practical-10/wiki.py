import wikipedia

result = wikipedia.search("Barack")
print(result)

suggestion = wikipedia.suggest("Barak Obama")
print(suggestion)

monty = wikipedia.search("Monty")
print(monty)

ford = wikipedia.search("Ford", results=3)
print(ford)

apple = wikipedia.summary("Apple III", sentences=1)
print(apple)

mercury = wikipedia.summary("Mercury")
print(mercury)



ny = wikipedia.page("New York")

print(ny.title)
print(ny.url)
print(ny.content)
print(ny.images[0])
print(ny.links[0])


wikipedia.set_lang("fr")
print(wikipedia.summary("Francois Hollande"))

# 'en' in wikipedia.languages()
print(wikipedia.languages()['es'])

def donation():
    return wikipedia.donate()