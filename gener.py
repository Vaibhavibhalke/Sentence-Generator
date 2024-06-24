#gener
from diction import *
import random

def chance(a):
    n = random.randint(0,1)
    if n == 1:
        b = a
        return b
    else:
        return None

    
tenses = ['past','present','future']

def ver():
    return random.choice(verbs)

def nou():
    return random.choice(nouns)

def adj():
    return random.choice(adjectives)

def adv():
    return random.choice(adverbs)

def ten():
    return random.choice(tenses)

def con():
    return random.choice(conjunctions)

sverb = ['had','is','will']

def sen1(t):
    #t = ten()
    sen = []
    sen += [chance(adj())]
    sen += [nou()]
    if t == "past":
        sen += [sverb[0]]
        sen += [chance(adv())]
        v = ver()
        if v.endswith('e'):
            v += 'd'
        elif v.endswith('y'):
            ve = ''
            for i in range(len(v)-1):
                ve += v[i]
            ve += 'ied'
            v = ve
        else:
            v += 'ed'
    elif t == 'present':
        sen += [sverb[1]]
        sen += [chance(adv())]
        v = ver()
        if v.endswith('e'):
            ve = ''
            for i in range(len(v)-1):
                ve += v[i]
            ve += 'ing'
            v = ve
        else:
            v+='ing'
    elif t == 'future':
        sen += [sverb[2]]
        sen += [chance(adv())]
        v = ver()
    sen += [v]
    sen += [chance(adv())]
    return sen



###




def sen2(a,b):
    if b == 'nouns':
        t = ten()
        sen = []
        sen += [chance(adj())]
        sen += [a]
        if t == "past":
            sen += [sverb[0]]
            sen += [chance(adv())]
            v = ver()
            if v.endswith('e'):
                v += 'd'
            elif v.endswith('y'):
                ve = ''
                for i in range(len(v)-1):
                    ve += v[i]
                ve += 'ied'
                v = ve
            else:
                v += 'ed'
        elif t == 'present':
            sen += [sverb[1]]
            sen += [chance(adv())]
            v = ver()
            if v.endswith('e'):
                ve = ''
                for i in range(len(v)-1):
                    ve += v[i]
                ve += 'ing'
                v = ve
            else:
                v+='ing'
        elif t == 'future':
            sen += [sverb[2]]
            sen += [chance(adv())]
            v = ver()
        sen += [v]
        sen += [chance(adv())]
        return sen

#
    
    elif b == 'verbs':
        t = ten()
        sen = []
        sen += [chance(adj())]
        sen += [nou()]
        if t == "past":
            sen += [sverb[0]]
            sen += [chance(adv())]
            v = a
            if v.endswith('e'):
                v += 'd'
            elif v.endswith('y'):
                ve = ''
                for i in range(len(v)-1):
                    ve += v[i]
                ve += 'ied'
                v = ve
            else:
                v += 'ed'
        elif t == 'present':
            sen += [sverb[1]]
            sen += [chance(adv())]
            v = a
            if v.endswith('e'):
                ve = ''
                for i in range(len(v)-1):
                    ve += v[i]
                ve += 'ing'
                v = ve
            else:
                v+='ing'
        elif t == 'future':
            sen += [sverb[2]]
            sen += [chance(adv())]
            v = a
        sen += [v]
        sen += [chance(adv())]
        return sen

#

    elif b == 'adjectives':
        t = ten()
        sen = []
        sen += [a]
        sen += [nou()]
        if t == "past":
            sen += [sverb[0]]
            sen += [chance(adv())]
            v = ver()
            if v.endswith('e'):
                v += 'd'
            elif v.endswith('y'):
                ve = ''
                for i in range(len(v)-1):
                    ve += v[i]
                ve += 'ied'
                v = ve
            else:
                v += 'ed'
        elif t == 'present':
            sen += [sverb[1]]
            sen += [chance(adv())]
            v = ver()
            if v.endswith('e'):
                ve = ''
                for i in range(len(v)-1):
                    ve += v[i]
                ve += 'ing'
                v = ve
            else:
                v+='ing'
        elif t == 'future':
            sen += [sverb[2]]
            sen += [chance(adv())]
            v = ver()
        sen += [v]
        sen += [chance(adv())]
        return sen

#

    elif b == (adverbs):
        t = ten()
        sen = []
        sen += [chance(adj())]
        sen += [nou()]
        if t == "past":
            sen += [sverb[0]]
            sen += [chance(adv())]
            v = ver()
            if v.endswith('e'):
                v += 'd'
            elif v.endswith('y'):
                ve = ''
                for i in range(len(v)-1):
                    ve += v[i]
                ve += 'ied'
                v = ve
            else:
                v += 'ed'
        elif t == 'present':
            sen += [sverb[1]]
            sen += [chance(adv())]
            v = ver()
            if v.endswith('e'):
                ve = ''
                for i in range(len(v)-1):
                    ve += v[i]
                ve += 'ing'
                v = ve
            else:
                v+='ing'
        elif t == 'future':
            sen += [sverb[2]]
            sen += [a]
            v = ver()
        sen += [v]
        sen += [chance(adv())]
        return sen

#

'''
s = sen1(ten())
print(s)
se = ''
for i in s:
    if i != None:
        se = se +' '+ i.lower()

print(se)
'''

