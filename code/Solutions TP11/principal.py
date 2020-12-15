print(f'principal: {__name__}')

from convertisseur import deCversF

# lecture
with open('celsius.txt', mode='r') as f:
    liste_tc_str = f.readlines()

# conversion
liste_tf = []
for tc_str in liste_tc_str:
    tc = float(tc_str)
    tf = deCversF(tc)
    liste_tf.append(tf)

# écriture avec print
"""
with open('farenheit.txt', mode='w') as f:
    for tf in liste_tf:
        print(tf, end='\n', file=f)
"""        
# écriture : façon write
with open('farenheit.txt', mode='w') as f:
    for tf in liste_tf:
        f.write(f'{tf}\n')


