Homer = {'age': 39, 'sexe': 'M', 'prénom': 'Homer', 'nom': 'Simpson'}
Marge = {'age': 34, 'sexe': 'F', 'prénom': 'Majorie', 'nom': 'Bouvier', 'surnom': 'Marge'}
Lisa = {'age': 8, 'sexe': 'F', 'prénom': 'Lisa', 'nom': 'Simpson'}
Bart = {'age': 10, 'sexe': 'M', 'prénom': 'Bartholomew', 'nom': 'Simpson', 'surnom': 'Bart'}


famille = [Homer, Marge, Lisa, Bart]

Homer['enfants'] = [Lisa, Bart]

# Quels sont les prénoms des enfants d'Homer ?

for enfant in Homer['enfants']:
    print(enfant['prénom'], end = ' -- ')
    
# Les enfants d'Homer ont pour père le dénommé Homer
for enfant in Homer['enfants']:
    enfant['père'] = Homer
    enfant['mère'] = Marge

# Est ce que Homer est le père de Lisa ?
test = Homer is Lisa['père']