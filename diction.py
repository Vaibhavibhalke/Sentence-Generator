'''
f = open('nouns.txt',"r")
r = f.read()
l = r.split()
nouns = []
for i in l:
    if i.isalpha() == True:
        nouns.append(i)
f.close()


f = open('pnouns.txt',"r")
r = f.read()
l = r.split()
pnouns = []
for i in l:
    if i.isalpha() == True:
        pnouns.append(i)
'''




nouns = ['boy','girl']

f = open('adjective.txt',"r")
r = f.read()
l = r.split()
adjectives = []
for i in l:
    if i.isalpha() == True:
        adjectives.append(i)
f.close()


f = open('adverb.txt',"r")
r = f.read()
l = r.split()
adverbs = []
for i in l:
    if i.isalpha() == True:
        adverbs.append(i)
f.close()


f = open('conjunctions.txt',"r")
r = f.readlines()
conjunctions = []
for i in r:
    p = i.rstrip()
    conjunctions.append(i)
f.close()


f = open('verb.txt',"r")
r = f.read()
l = r.split()
verbs = []
for i in l:
    if i.isalpha() == True:
        verbs.append(i)
f.close()


