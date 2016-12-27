from tkinter import *
import Cookbook

root = Tk()
root.attributes("-fullscreen", True)

#menu
menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

#LIST BOX
i = 0
listBox = Listbox(root, selectmode=SINGLE)
for recipe in Cookbook.cookbook:
    listBox.insert(i, recipe.title)
    i += 1
listBox.pack({"side": "left"})

#TEXT BOX
textBox = Text(root)
textBox.pack({"side": "right"})
def refreshTextBox(*args):
    textBox.delete('1.0', END)
    textBox.insert(INSERT, Cookbook.printRecipeInstructions(listBox.get(ACTIVE)))
listBox.bind("<Double-Button-1>", refreshTextBox)
refreshTextBox()

root.config(menu=menuBar)
root.mainloop()
root.destroy()
