from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile,asksaveasfile
import os
def newFile():
    global file
    root.title('Untitled-Notepad')
    file=None
    TextArea.delete(1.0,END) #1.0= first line ke zeroth character se end tak sab delete kar dena hain...
def openFile():
    global file
    file=askopenfile(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file.name)+"-Notepad")
        TextArea.delete(1.0,END)
        # f=open(file,'r')
        TextArea.insert(1.0,file.read())
        file.close()    


def saveFile():
    global file
    if file==None:
        file=asksaveasfile(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])


        if file=="":
            file=None
        else:
            #save as new file
            # f=open(file,'w')
            file.write(TextArea.get(1.0,END))
            file.close()
            root.title(os.path.basename(file.name)+'-Notepad')    

def cut():
    TextArea.event_generate("<<Cut>>")#event_generate is used to directly generate the event
def copy():
    TextArea.event_generate("<<Copy>>")
def paste():
    TextArea.event_generate("<<Paste>>")
def about():
    showinfo('Notepad','notepad by manisha')
def quitApp():
    root.destroy()
if __name__=='__main__':
    root=Tk()
    root.title('Untitled-Notepad')
    root.wm_iconbitmap('download.png')
    root.geometry('643x578')
    # add text area


    TextArea=Text(root,font='Arial 13 ')
    file=None

    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    TextArea.pack(expand=True,fill=BOTH)    # if expand is true then it will take the parent width and height....

    # let create menubar
    MenuBar=Menu(root)
    # file menu starts
    FileMenu=Menu(MenuBar,tearoff=0)
    # to open new file
    FileMenu.add_command(label='New',command=newFile)
    # to open already existing file
    FileMenu.add_command(label='Open',command=openFile)
    # to save the current file
    FileMenu.add_command(label='Save',command=saveFile)
    FileMenu.add_separator()
    root.config(menu=MenuBar)
    MenuBar.add_cascade(label='File',menu=FileMenu)
    # file menu ends


    # edit menu starts
    EditMenu=Menu(MenuBar,tearoff=0)
    #cut,copy and paste
    EditMenu.add_command(label='Cut',command=cut)
    EditMenu.add_command(label='Copy',command=copy)
    EditMenu.add_command(label='Paste',command=paste)
    root.config(menu=MenuBar)
    MenuBar.add_cascade(label='Edit',menu=EditMenu)
    # edit menu ends

    #Help menu starts
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label='About Notepad',command=about)
    root.config(menu=MenuBar)
    MenuBar.add_cascade(label='Help',menu=HelpMenu)
    # exit the notepad
    ExitMenu=Menu(MenuBar,tearoff=0)
    ExitMenu.add_command(label='Exit',command=quitApp)
    root.config(menu=MenuBar)
    MenuBar.add_cascade(label='Exit',menu=ExitMenu)






    root.mainloop()