from tkinter import *
cf1='#EFEBE9'
hc1='#37474F'

class Conta:
    def __init__(self,root):
        self.root = root
        self.root.config(bg=cf1)
        #self.root.geometry('440x280')
        self.IntroLabel = Label(root, text='Gerenciamento de Contas',font=('Arial',12,'bold'), fg='white', bg=hc1, width=60)
        self.NomeLabel = Label(root, text='Titular:',bg=cf1,font=('Arial',12,'bold'))
        self.NomeEntry = Entry(root, width=13)
        self.AgencLabel = Label(root, text='Agência:',bg=cf1,font=('Arial',12,'bold'))
        self.AgenEntry = Entry(root, width=8)
        self.ContaLabel = Label(root, text='Conta:',bg=cf1,font=('Arial',12,'bold'))
        self.ContaEntry = Entry(root, width=8)

        self.IntroLabel.grid(row=1, column=1, columnspan=6)
        self.NomeLabel.grid(row=2, column=1, pady=4)
        self.NomeEntry.grid(row=2, column=2, pady=4)
        self.AgencLabel.grid(row=2, column=3, pady=4)
        self.AgenEntry.grid(row=2, column=4, pady=8)
        self.ContaLabel.grid(row=2, column=5, pady=8)
        self.ContaEntry.grid(row=2, column=6, pady=8)





root = Tk()

c1 = Conta(root)

root.mainloop()