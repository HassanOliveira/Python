import modèle

def nourrir(animal_id):
    if (modèle.verifie_disponibilite('mangeoire') == 'occupé'):
        return f"Impossible, la mangeoire est actuellement occupé par {modèle.cherche_occupant('mangeoire')}"
    
    if (modèle.lit_etat(animal_id) == None):
        return None

    if (modèle.lit_etat(animal_id) != 'affamé'):
        return f"Désolé, {animal_id} n'a pas faim!"

    if ((modèle.verifie_disponibilite('mangeoire') == 'libre') and (modèle.lit_etat(animal_id) == 'affamé')):
        modèle.change_lieu(animal_id, 'mangeoire')
        modèle.change_etat(animal_id, 'repus')
        return f"Félicitations, {animal_id} a rejoint le mangeoire et est maintenant repus."
    else:
        return None


def divertir(animal_id):
    if (modèle.verifie_disponibilite('roue') == 'occupé'):
        return f"Impossible, le roue est actuellement occupé par {modèle.cherche_occupant('roue')}"
    if (modèle.lit_etat(animal_id) == None):
        return None    
    if (modèle.lit_etat(animal_id) != 'repus'):
        return f"Désolé, {animal_id} n'est pas en état de faire du sport!"
    if ((modèle.verifie_disponibilite('roue') == 'libre') and (modèle.lit_etat(animal_id) == 'repus')):
        modèle.change_lieu(animal_id, 'roue')
        modèle.change_etat(animal_id, 'fatigué')
        return f"Félicitations, {animal_id} a rejoint le roue et est maintenant fatigué."
    else:
        return None

def coucher(animal_id):
    if (modèle.verifie_disponibilite('nid') == 'occupé'):
        return f"Impossible, le nid est actuellement occupé par {modèle.cherche_occupant('nid')}"
    if (modèle.lit_etat(animal_id) == None):
        return None    
    if (modèle.lit_etat(animal_id) != 'fatigué'):
        return f"Désolé, {animal_id} n'est pas fatigué!"
    if ((modèle.verifie_disponibilite('nid') == 'libre') and (modèle.lit_etat(animal_id) == 'fatigué')):
        modèle.change_lieu(animal_id, 'nid')
        modèle.change_etat(animal_id, 'endormi')
        return f"Félicitations, {animal_id} a rejoint le nid et est maintenant endormi."
    else:
        return None

def reveiller(animal_id):
    if (modèle.lit_etat(animal_id) == None):
        return None    
    if (modèle.lit_etat(animal_id) != 'endormi'):
        return f"Désolé, {animal_id} ne dort pas!"
    if (modèle.lit_etat(animal_id) == 'endormi'):
        modèle.change_lieu(animal_id, 'litière')
        modèle.change_etat(animal_id, 'affamé')
        return f"{animal_id} s'est réveillé et maintenant affamé."
    else:
        return None