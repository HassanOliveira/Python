from ctypes.wintypes import tagRECT
import json

authorized_states = ('affamé', 'fatigué', 'endormi', 'repus')

authorized_lieu = ('litière', 'mangeoire', 'nid')

def lit_etat(animal_id):
    with open('animal.json', "r", encoding="utf-8") as file:
        animal = json.load(file)
        if animal_id in animal:
            file.close()
            return animal[animal_id]["ETAT"]
        else:
            print(f"Désolé, {animal_id} n'est pas un animal connu")
            file.close()
            return None

def lit_lieu(animal_id):
    with open('animal.json', "r", encoding="utf-8") as file:
        animal = json.load(file)
        if animal_id in animal:
            file.close()
            return animal[animal_id]["LIEU"]
        else:
            print(f"Désolé, {animal_id} n'est pas un animal connu")
            file.close()
            return None

def verifie_disponibilite(equipment_id):
    with open('equipment.json', "r", encoding="utf-8") as file:
        equipment = json.load(file)
        if equipment_id in equipment:
            file.close()
            return equipment[equipment_id]["DISPONIBILITÉ"]
        else:
            print(f"Désolé, {equipment_id} n'est pas un equipment connu")
            file.close()
            return None

def cherche_occupant(LIEU):
    with open('animal.json', "r", encoding="utf-8") as file:
        animal_file = json.load(file)
        list = []
        for animal in animal_file:
            if (animal_file[animal]['LIEU'] == LIEU):
                list.append(animal)
        if len(list) == 0:
            print (f"Désolé, {LIEU} n'est pas un lieu connu")
            file.close()
            return None
        file.close()
        return list

def change_etat(animal_id, etat):
    with open('animal.json', "r", encoding="utf-8") as file:
        animal = json.load(file)
        if animal_id not in animal:
            print(f"Désolé, {animal_id} n'est pas un animal connu")
            file.close()
            return None
    
    if etat in authorized_states:
        animal[animal_id]["ETAT"] = etat

    json.dump(animal, open("animal.json", "w", encoding="utf-8"), indent=4)
    
    file.close()

def change_lieu(animal_id, LIEU):
    with open('animal.json', "r", encoding="utf-8") as file:
        animal = json.load(file)
        if animal_id not in animal:
            print(f"Désolé, {animal_id} n'est pas un animal connu")
            file.close()
            return None
    
    if LIEU in authorized_lieu:
        animal[animal_id]["LIEU"] = LIEU

    json.dump(animal, open("animal.json", "w", encoding="utf-8"), indent=4)

    file.close()