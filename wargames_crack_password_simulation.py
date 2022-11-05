import tkinter as tk
import tkinter.font as tkFont
import string
import time
import random


#Définition popup pour les entrées
def tkinter_input():
    popup = tk.Tk()
    popup.title("Definition du mot de pass")
    popup.configure(background="grey")
    tk.Label(popup, text="Entrer le mot de passe",bg="grey").pack()
    entry_m = tk.Entry(popup)
    entry_m.pack()
    tk.Label(popup, text="Entrer la puissance de calcul",bg="grey").pack()
    scala = tk.Scale(popup, from_=1, to=10,orient="horizontal",bg="grey")
    scala.pack()
    button_ok=tk.Button(popup, text="OK",bg="red")
    button_ok.pack()

    
    mdp = None
    puissance=None
    def callback(event):
        nonlocal mdp
        nonlocal puissance
        mdp = entry_m.get()
        puissance=scala.get()
        popup.destroy()

    button_ok.bind("<Button-1>", callback)
    popup.mainloop()
    return mdp,puissance




#Définition Constantes et variables
PASSWORD,PUISSANCE = tkinter_input()
if not PASSWORD: PASSWORD=""
liste_PUISSANCE={10:0.01,9:0.02,8:0.03,7:0.02,6:0.05,5:0.06,4:0.07,3:0.08,2:0.09,1:0.1}
PUISSANCE=liste_PUISSANCE[int(PUISSANCE)]
ALPHABET=string.ascii_letters+'0123456789'+"%$*ù^!:;#~"
liste_secure = ['']*len(PASSWORD)
liste_crack = [' ']*len(PASSWORD)
lettres=[f"lettre{i}" for i in range(len(PASSWORD))]
labels={i:0 for i in range(len(PASSWORD))}

#Configuration du GUI
root = tk.Tk()
root.title("Password Cracker")
root.configure(background="black")
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.resizable(width=False, height=False)
ft = tkFont.Font(family='Guru Meditation NBP',size=78)




def update_geometry(w,h):
    """Cette fonction prend en paramètre w pour width(largeur) et h pour height(hauteur)
    Son but est de redimenssionner la fenetre selon les paramètres w et h
    """
    alignstr = '%dx%d+%d+%d' % (w, h, (screenwidth - w) / 2, (screenheight - h) / 2)
    root.geometry(alignstr)

def creer_affichage(n=len(PASSWORD)):
    """Cette fonction prend en paramètre n(de valeur par défaut la longueur de PASSWORD) et affiche n lettres
    tout en adaptant la taille de la fenêtre"""
    for indice_lettre in range(n):
        label=tk.Label(root)
        label.place(x=50+indice_lettre*100,y=90,width=90,height=115)
        label["bg"]="black"
        label["font"] = ft
        label["fg"] = "#1e90ff"
        label["justify"] = "center"
        label["text"] = "_"
        labels[indice_lettre]=label
        update_geometry(45+100*(indice_lettre+1),275)
    else:
        update_geometry(90+100*(indice_lettre+1),275)# décalage de la derniere lettre au bord droit


def main():
    """Programme pincipal"""
    if len(PASSWORD)==0:raise SystemExit # Si aucun mot de passe spécifier arreter le programme
    creer_affichage()
    while liste_secure!=list(PASSWORD):  
        for i in range(len(PASSWORD)):
            if liste_crack[i]==liste_secure[i]: # si l'element de l'indice i est égale a lelement de l'indice i du passwd tu fais rien
                continue
            random_text=random.choice(ALPHABET)
            liste_crack[i]=random_text
            labels[i].configure(text=random_text,)

        
        indice_au_hasard=random.randint(0,len(PASSWORD)-1)
        if liste_crack[indice_au_hasard] == list(PASSWORD)[indice_au_hasard]: # si un element (pris au hasard) de liste_crack est le meme element que celui de PASSWORD pris au meme hasard
            labels[indice_au_hasard].configure(fg="green")
            liste_secure[indice_au_hasard]=list(PASSWORD)[indice_au_hasard]

        time.sleep(PUISSANCE+0.01)
        root.update()
    root.mainloop()# empêche que la fenêtre se ferme après que le mdp soit trouvé
    
    
if __name__=='__main__':
    main()


