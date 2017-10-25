template = "[![{0}](http://img.shields.io/:{1}-{2}-{3}.svg)](https://github.com/Alan-FGR/aelum)"
colors = ["brightgreen","green","yellowgreen","yellow","orange","red","lightgrey","blue"]

import random, Tkinter

def convert(txt):
    txt = txt.replace("-","_")
    txt = txt.replace("$","_")
    txt = txt.rstrip()
    words = txt.split(" ")
    pairs = zip(words,words[1:])[::2]
    return '\n'.join([template.format(x[0]+' '+x[1],x[0],x[1],random.choice(colors)) for x in pairs])+'\n'

root = Tkinter.Tk()
root.geometry("500x500") #tkinter sucks
root.resizable(False,False)

intext = Tkinter.Text(root, height=12)
outtext = Tkinter.Text(root, height=12, wrap=Tkinter.NONE)

def gui_convert():
    outtext.delete('1.0', 'end') # wtf
    outtext.insert('1.0',convert(intext.get('1.0','end'))) #what the actual hell?? :(

Tkinter.Label(root,text="Input text").pack()
intext.pack()
button = Tkinter.Button(root, text="Convert", command=gui_convert).pack()
outtext.pack()

root.mainloop()
