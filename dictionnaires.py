dict0 = {}
print(dict0)  # Output: {}

eleves = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris",
    "cours": ["Math", "Physique", "Chimie"],
    "note": {
        "Math": 15,
        "Physique": 18,
        "Chimie": 12
    },
    "moyenne": lambda notes: sum(notes.values()) / len(notes),  # Fonction pour calculer la moyenne des notes
    "moyenne_cal": 15
}
print(eleves)  # Output: {'nom': 'Alice', 'age': 25, 'ville': 'Paris', 'cours': ['Math', 'Physique', 'Chimie']}
print(eleves["nom"])  # Output: Alice
print(eleves["cours"][0])  # Output: Math
print(eleves["note"]["Physique"])  # Output: 18
print(eleves["moyenne"](eleves["note"]))  # Output: 15.0
print(eleves["moyenne"])  #Output: <function <lambda> at 0x7f8b8c1e1d30>

print(eleves.get("nom"))  # Output: Alice
print(eleves.get("adresse", "Adresse non trouvee"))  # Output: Adresse non trouvee
print(eleves.get("note").get("Math"))  # Output: 15
print(eleves.get("cours")[1])  # Output: Physique

print(eleves.keys())  # Output: dict_keys(['nom', 'age', 'ville', 'cours', 'note', 'moyenne', 'moyenne_cal'])
print(eleves.values())  # Output: dict_values(['Alice', 25, 'Paris', ['Math', 'Physique', 'Chimie'], {'Math': 15, 'Physique': 18, 'Chimie': 12}, <function <lambda> at 0x7f8b8c1e1d30>, 15])

print(eleves.items())  # Output: dict_items([('nom', 'Alice'), ('age', 25), ('ville', 'Paris'), ('cours', ['Math', 'Physique', 'Chimie']), ('note', {'Math': 15, 'Physique': 18, 'Chimie': 12}), ('moyenne', <function <lambda> at 0x7f8b8c1e1d30>), ('moyenne_cal', 15)])
print(len(eleves))  # Output: 7

print("nom" in eleves)  # Output: True
print("Math" in eleves)  # Output: False
print("Math" in eleves["note"])  # Output: True

eleves["age"] = 26
print(eleves["age"])  # Output: 26

eleves.update({"ville": "Lyon", "moyenne_cal": 12})

print(eleves)  # Output: {'nom': 'Alice', 'age': 26, 'ville': 'Lyon', 'cours': ['Math', 'Physique', 'Chimie'], 'note': {'Math': 15, 'Physique': 18, 'Chimie': 12}, 'moyenne': <function <lambda> at 0x7f8b8c1e1d30>, 'moyenne_cal': 12}

del eleves["moyenne_cal"]
print(eleves) # Output: {'nom': 'Alice', 'age': 26, 'ville': 'Lyon', 'cours': ['Math', 'Physique', 'Chimie'], 'note': {'Math': 15, 'Physique': 18, 'Chimie': 12}, 'moyenne': <function <lambda> at 0x7f8b8c1e1d30>}

del1 = eleves.pop("ville")
print(del1)  # Output: Lyon
del2 = eleves.pop("moyenne_cal", "Cle non trouvee")
print(del2)  # Output: Cle non trouvee

print(eleves)  # Output: {'nom': 'Alice', 'age': 26, 'cours': ['Math', 'Physique', 'Chimie'], 'note': {'Math': 15, 'Physique': 18, 'Chimie': 12}, 'moyenne': <function <lambda> at 0x7f8b8c1e1d30>}

for key, value in eleves.items():
    #print(f"{key}: {value}")
    print(key, value)  # Output: nom Alice, age 26, cours ['Math', 'Physique', 'Chimie'], note {'Math': 15, 'Physique': 18, 'Chimie': 12}, moyenne <function <lambda> at 0x7f8b8c1e1d30>

for key in eleves.keys():
    print(key)  # Output: nom, age, cours, note, moyenne

for value in eleves.values():
    print(value)  # Output: Alice, 26, ['Math', 'Physique', 'Chimie'], {'Math': 15, 'Physique': 18, 'Chimie': 12}, <function <lambda> at 0x7f8b8c1e1d30>

for key in eleves:
    print(key)  # Output: nom, age, cours, note, moyenne        

