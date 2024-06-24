
from tkinter import *
from gener import *

'''
def gen():
    global sen
    sen = random.choice(noun) + ' ' + random.choice(preposition) + ' ' + random.choice(verb)
'''
def gen():
    global sent
    s = sen1(ten())
    print(s)
    se = ''
    for i in s:
        if i != None:
            se = se +' '+ i.lower()
    print(se)
    se = se.lstrip()
    se = se[0].upper() + se[1:]
    se = se + '.'
    sent = se


def updoot():
    gen()
    l2_f1["text"] = sent



def show(f):
    f.tkraise()

def checker():
    n1 = e1.get()
    if n1 in nouns:
        updooter(n1,'nouns')
    elif n1 in verbs:
        updooter(n1,'verbs')
    elif n1 in adjectives:
        updooter(n1,'adjectives')
    elif n1 in adverbs:
        updooter(n1,'adverbs')
    else:
        lbl1 = Label(f2, text = "Select which type of word this is")
        lbl1.grid(row = 6, column = 3)

        btn1= Button(f2,text = "Noun",command = lambda:updooter(n1,"nouns"))
        btn1.grid(row = 7, column = 3)

        btn1= Button(f2,text = "Verb",command = lambda:updooter(n1,"verbs"))
        btn1.grid(row = 8, column = 3)

        btn1= Button(f2,text = "Adj",command = lambda:updooter(n1,"adjectives"))
        btn1.grid(row = 9, column = 3)

        btn1= Button(f2,text = "Adverb",command = lambda:updooter(n1,"adverbs"))
        btn1.grid(row = 10, column = 3)
        






def updooter(x,y):
    global sent
    s = sen2(x,y)
    print(s)
    se = ''
    for i in s:
        if i != None:
            se = se +' '+ i.lower()
    print(se)
    se = se.lstrip()
    se = se[0].upper() + se[1:]
    se = se + '.'
    sent = se
    l3_f2["text"] = sent
    







root = Tk()                     #MAIN




root.title("Sentence Generator")


l = Label(root,text = "Sentence Generator",font = ("Rockwell",50),bg = 'light blue')            #Main Label # Rockwell
l.grid(row = 0,column = 3)

f1 = Frame(root,bd = 100)                                                                       #Initialising Frames
f2 = Frame(root,bd = 100)
f1.grid(row = 1,column = 3)
f2.grid(row = 1,column = 3)

#FRAME 1

l1_f1 = Label(f1, text = "Automated Generation",font = ("Futura",30))
l1_f1.grid(row = 0, column = 3)

blan1 = Label(f1, text = " ")
blan1.grid(row = 1, column = 3)


l2_f1 = Label(f1, text = "Click the button to \n generate a sentence",font = ("",20))
l2_f1.grid(row = 2, column = 3)


blan2 = Label(f1, text = " ")
blan2.grid(row = 3, column = 3)

b1_f1 = Button(f1,text = "Generate",command = updoot) #, height = 3,width = 10 font = ("Futura",15),
b1_f1.grid(row = 4, column = 3)

blan3 = Label(f1, text = " ")
blan3.grid(row = 5, column = 3)


#FRAME 2


l1_f2 = Label(f2, text = "Manual Generation",font = ("Futura",30))
l1_f2.grid(row = 0, column = 3)

blan4 = Label(f2, text = " ")
blan4.grid(row = 1, column = 3)


l2_f2 = Label(f2, text = "Enter word to be generated with",font = ("",20))
l2_f2.grid(row = 2, column = 3)

e1 = Entry(f2)
e1.grid(row = 3,column = 3)


l3_f2 = Label(f2, text = "Click the button to \n generate a sentence",font = ("",20))
l3_f2.grid(row = 4, column = 3)


blan5 = Label(f2, text = " ")
blan5.grid(row = 5, column = 3)

b1_f2 = Button(f2,text = "Generate",command = checker) #, height = 3,width = 10 font = ("Futura",15),
b1_f2.grid(row = 6, column = 3)


l4_f2 = Label(f2, text = " ",font = ("",20))
l4_f2.grid(row = 7, column = 3)


blan6 = Label(f2, text = " ")
blan6.grid(row = 8, column = 3)



#To change Frames
lf1 = Label(f1,text = "To go to Manual Generation",font = ("",20))#,bg = 'orange'
lf1.grid(row = 6,column = 3)
bf1 = Button(f1,text = "Click Here",command = lambda:show(f2))
bf1.grid(row = 7,column = 3)
lf2 = Label(f2,text = "To go to Automated Generation",font = ("",20))#,bg = 'light green'
lf2.grid(row = 15,column = 3)
bf2 = Button(f2,text = "Click Here", command = lambda:show(f1))
bf2.grid(row = 16,column = 3)


f1.tkraise()
root.geometry("510x510")
root.minsize(510, 510)
#root.maxsize(510, 510)
root.mainloop()

