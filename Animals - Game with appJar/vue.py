from tkinter.font import BOLD
from appJar import gui
import modèle
import contrôleur


app = gui()

liste_animaux = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
liste_action = ['nourrir', 'divertir', 'coucher', 'reveiller']
random_strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

app.addLabel("en-tête", "Bienvenue à l'animalerie!", 0, 0, 2)
app.setLabelBg("en-tête", "DarkSlateBlue")
app.setLabelFg("en-tête", "white")

app.addLabel("tableau", "Tableau de bord")
app.setLabelBg("tableau", "gray")
app.setLabelFg("tableau", "white")


for animal_id in liste_animaux: 
    app.addLabel(random_strings[liste_animaux.index(animal_id)], animal_id, liste_animaux.index(animal_id)+1, 0)
    app.addLabel(random_strings[liste_animaux.index(animal_id)+5], f"{modèle.lit_etat(animal_id)}, {modèle.lit_lieu(animal_id)}", liste_animaux.index(animal_id)+1, 1)
    if liste_animaux.index(animal_id)%2 == 0:
        app.setLabelBg(random_strings[liste_animaux.index(animal_id)], "CornflowerBlue")
        app.setLabelBg(random_strings[liste_animaux.index(animal_id)+5], "CornflowerBlue")
    else:
        app.setLabelBg(random_strings[liste_animaux.index(animal_id)], "LightBlue")
        app.setLabelBg(random_strings[liste_animaux.index(animal_id)+5], "LightBlue")

app.addLabel("faire", "Faire Quelque Chose", 6, 0, 2)
app.setLabelBg("faire", "ForestGreen")
app.setLabelFg("faire", "white")

app.addLabel("animal", "Animal", 7, 0, 1)
app.setLabelBg("animal", "MediumSeaGreen")
app.setLabelFg("animal", "white")

app.addLabel("actions", "Actions", 7, 1, 1)
app.setLabelBg("actions", "SeaGreen")
app.setLabelFg("actions", "white")

for animal_id in liste_animaux:
    app.addRadioButton('animal_id', animal_id, liste_animaux.index(animal_id)+8, 0)

for actions in liste_action:
    app.addRadioButton('actions', actions, liste_action.index(actions)+8, 1)


def press(action):
    action = app.getRadioButton("actions")
    animal = app.getRadioButton("animal_id")

    if (action == 'nourrir' and modèle.lit_etat(animal) == 'affamé'):
        info = contrôleur.nourrir(app.getRadioButton("animal_id"))
        app.infoBox("info", info)  
    elif (action == 'nourrir' and modèle.lit_etat(animal) != 'affamé'):
        app.warningBox("alert", contrôleur.nourrir(animal))
    

    if (action == 'divertir' and modèle.lit_etat(animal) == 'repus'):
        info = contrôleur.divertir(app.getRadioButton("animal_id"))
        app.infoBox("info", info)    
    elif (action == 'divertir' and modèle.lit_etat(animal) != 'repus'):
        app.warningBox("alert", contrôleur.divertir(animal))
    

    if (action == 'coucher' and modèle.lit_etat(animal) == 'fatigué'):
        info = contrôleur.coucher(app.getRadioButton("animal_id"))
        app.infoBox("info", info) 
    elif (action == 'coucher' and modèle.lit_etat(animal) != 'fatigué'):
        app.warningBox("alert", contrôleur.coucher(animal))


    if (action == 'reveiller' and modèle.lit_etat(animal) == 'endormi'):
        info = contrôleur.reveiller(app.getRadioButton("animal_id"))
        app.infoBox("info", info) 
    elif (action == 'reveiller' and modèle.lit_etat(animal) != 'endormi'):
        app.warningBox("alert", contrôleur.reveiller(animal))

    mise_a_jour()

def mise_a_jour():
    for animal_id in liste_animaux:
        app.setLabel(random_strings[liste_animaux.index(animal_id)], animal_id)
        app.setLabel(random_strings[liste_animaux.index(animal_id)+5], f"{modèle.lit_etat(animal_id)}, {modèle.lit_lieu(animal_id)}")
    

app.addButton("go",  press, 13, 0, 2)
app.go()
