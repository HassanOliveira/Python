import modèle

def test_lit_etat():
    assert modèle.lit_etat("Tac") == "affamé"

def test_lit_etat_nul():
    assert modèle.lit_etat("Bob") == None

def test_lit_lieu():
    assert modèle.lit_lieu("Tac") == 'litière' 
 
def test_lit_lieu_nul():
    assert modèle.lit_lieu("Bob") == None

def test_verifie_disponibilite():
    assert modèle.verifie_disponibilite('litière') == 'libre'
    assert modèle.verifie_disponibilite('nid') == 'occupé'

def test_verifie_disponibilite_nul():
    assert modèle.verifie_disponibilite('nintendo') == None

def test_cherche_occupant():
    assert modèle.cherche_occupant("nid") == ['Pocahontas']
    assert 'Tac' in modèle.cherche_occupant('litière')
    assert 'Tac' not in modèle.cherche_occupant('mangeoire')

def test_cherche_occupant_nul():
    assert modèle.cherche_occupant('casino') == None

def test_change_etat():
    modèle.change_etat('Totoro', 'fatigué')
    assert modèle.lit_etat('Totoro') == 'fatigué'
    modèle.change_etat('Totoro', 'excité comme un pou')
    assert modèle.lit_etat('Totoro') == 'fatigué'
    modèle.change_etat('Bob', 'fatigué')
    assert modèle.lit_etat('Bob') == None
    
def test_change_lieu():
    modèle.change_lieu('Totoro', 'roue')
    assert modèle.lit_lieu('Totoro') == 'roue'
    assert modèle.verifie_disponibilite('litière') == 'libre'    
    assert modèle.verifie_disponibilite('roue') == 'occupé'    

test_lit_etat()
test_lit_etat_nul()

test_lit_lieu()
test_lit_lieu_nul()

test_verifie_disponibilite()
test_verifie_disponibilite_nul()

test_cherche_occupant()
test_change_etat()
test_change_lieu()