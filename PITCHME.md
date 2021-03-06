# Introduction à la programmation

Christophe Saint-Jean

[Transparents](https://gitpitch.com/christophesaintjean/IntroProgS1_2020#/) / [Code](https://tinyurl.com/codeintroprogS1) du cours 2020-2021

---

@transition[fade]

## Administration de l'UE

+++

### Mentions légales

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Ce(tte) œuvre est mise à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.

+++

### L'équipe enseignante

* Bernard Besserer (TP)
* Jordan Calandre (TP)
* Laurent Mascarilla (TP)
* Matthieu Robert (TP)
* **Christophe Saint-Jean** (Cours/TP - Resp.)

+++

### Communication

* Questions pédagogiques : [Moodle](https://moodle.univ-lr.fr/)
  * Appronfondissement/Questions (Forum)
  * Organisation de l'UE/Planning (Messages privés)
* Questions administratives (Secrétariat)
  * Appartenance groupes TD/TP
  * Absences/Justifications

+++

### Dispositif horaire

@ul

* 5 cours de 1,5 heures (Amphithéâtre)
* 12 TPs de 1,5 heures (Salles de TP)

@ulend

+++

### Evaluation

$$S_1 = \frac{CC_1+CC_2}{2}$$

$$S_2 = CC_3$$

Les CC se passent en TP (5/6 et 12) sur machine:

@ul

* Une partie QCM
* Une partie évaluée par un enseignant
* Attention à la règle sur les absences

@ulend

+++

### Les objectifs de cet enseignement

* Découvrir les bases de la programmation informatique.
* Développer l'esprit logique par la pratique de la programmation.
* Appprendre un des langages support de votre formation.
* Libérer votre créativité !!

+++

### *Sondage !*

![Sondage](images/langages.png)

---

@transition[fade]

## Généralités sur la programmation

+++

### Langage humain

```
les soir chats, mur promèment sur le
```

@ul

* Un certain _vocabulaire_, _une orthographe_, des _règles de grammaire_ communes
* Grande expressivité et diversité
* Même si l'on commet des erreurs, nous sommes capables de comprendre "globalement" le message

@ulend

### Langage informatique

@ul

* La machine traite des informations binaires: 100110010101000110 ... (même si images, sons, *programmes*, ...)
* Le vocabulaire d'instructions machine est très réduit (arith, logique, mémoire, ...)
* Pas de tolérance aux erreurs d'instructions
* Parler à une machine (et donc programmer), c'est s'adresser une **entité efficace mais peu compréhensive** ...

@ulend

+++

### Niveau d'un langage de programmation

Différents niveaux d'abstraction par rapport aux instructions du processeur:

* 100110010101000110 ... (Quasi-impossible)
* Langages de bas niveau (Ex. Assembleur)
* Langages de bas/haut niveau (Ex. C)
* Langages de haut niveau (Ex. **Python**, Java, C++, R, ...)

+++

### Programme Source (ou Code)

Un programme source est un ___texte___ qui:

* Dépend d'un *langage de programmation*
* Utilise un certain nombre de _conventions_ (nommage, opérations, ...),
* Obéit à des règles de _syntaxe_, de _grammaire_.
* En géneral, sauvegardé puis exécuté depuis un fichier.

Le mode d'exécution du programme est variable (compilation, interprétation, hybride)

+++

### Exemples : Hello World 1/2

c (CM1_helloworld.c):

```c
#include <stdio.h>
int main() {
    printf("Hello World\n");
}
```

Java (HelloWorld.java):

```java
class HelloWorld {
  static public void main( String args[] ) {
    System.out.println( "Hello World" );
  }
}
```

+++

### Exemples : Hello World 2/2

Python 3 (CM1\_helloworld.py):

```python
print("Hello World")
```

Pour aller plus loin [Hello World Collection](http://helloworldcollection.de/) !!

+++

### Les différentes sources d'erreur

@ul

* Erreurs de syntaxe: Non respect des conventions du langage
* Erreurs d'exécution (Runtime-Error): Opération non valide lors de l'exécution
* Erreurs sémantiques: Résultat différent de celui désiré

@ulend

+++

### Exécution d'un programme (Compilation) 1/2

![Compilation](images/compilation.png)

Compilation et exécution pour le compilateur gcc:

```bash
  > gcc source.c -o prog_executable.exe
  > ./prog_executable.exe
```

+++

### Exécution d'un programme (Compilation) 2/2

![Compilation](images/compilation.png)

Analogie: Service de traduction intégrale à distance

Propriétés:

@ul

* Cible un type de machine (rapide)
* Vérification de la syntaxe à la compilation (Temps de compilation long)
  
@ulend

+++

### Exécution d'un programme (Interprétation) 1/2

![Compilation](images/interpretation.png)

Exemple ligne de commande Unix (bash):

```bash
 > echo $((4+5))
 9
 > echo $nexistepas

 > [ -x  3]
 -bash: [: missing `]'
```

+++

### Exécution d'un programme (Interprétation) 2/2

![Compilation](images/interpretation.png)

Analogie: Traduction à la volée puis exécution

Propriétés:

@ul

* Flexible car pas de cible (c'est l'interpréteur)
* Cycle Vérification + Exécution (lent)
* Découverte d'erreurs à l'exécution

@ulend

+++

### Exécution d'un programme (Hybride) 1/2

![Hybride](images/hybride.png)

Compilation et interprétation d'un code Java:

```bash
 > javac HelloWorld.java
 > java HelloWorld
```

+++

### Exécution d'un programme (Hybride) 2/2

![Hybride](images/hybride.png)

Le meilleur des deux mondes:

* Flexible
* Relativement rapide
* Multi-cible
* Supprime les erreurs de syntaxe à la compilation

+++

### Mode d'exécution - Conclusion

* De nombreux langages disposent à la fois de compilateurs et d'interpréteurs.
* C'est l'usage historique qui a fait penché la balance...
* *Python* s'exécute en mode hybride même s'il pourrait croire qu'il s'agit d'un pur interpréteur:

```bash
 > python HelloWorld.py
```

[Arguments techniques - hors cadre de l'UE](http://autourducode.com/le-bytecode-python.html)

+++

### Les outils d'édition du code 1/2

Un "bon" _environnement de développement intégré_ est un programme qui:

@ul

* Facilite l'édition du code (coloration syntaxique, saisie prédictive, ...)
* Intègre les règles de bonnes pratiques d'un langage (Ex.: PEP8 pour Python)
* Détecte les erreurs de syntaxe lors de l'édition

@ulend

+++

### Les outils d'édition du code 2/2

Un "bon" _environnement de développement intégré_ est un programme qui:

@ul

* Permet de compiler/d'interpréter un code source par un clic
* Donne accès à des outils de débogage (valeurs des variables, point d'arrêt, ...)
* Gestion de projets, des versions, lancement du code à distance, ...

@ulend

---

@transition[fade]

## Généralités sur les langages de programmation

+++

### Quelques paradigmes

On peut catégoriser les langages suivants des propriétés qui les caractérisent:

* Langages impératifs
* Langages procéduraux
* Langages à objets
* Langages déclaratifs

[et bien d'autres ...](https://fr.wikipedia.org/wiki/Paradigme_programmation)

La plupart des langages sont multi-paradigmes.

+++

### Langage impératif 1/2

Un langage est dit impératif lorsque le programme correspond à une succession d'instructions:

```python
Instruction 1
Instruction 2
...
Instruction n
```

Chaque instruction tient compte de l'état du système (mémoire, E/S, ...) et peut le modifier.

+++

### Langage impératif 2/2

Exemples typiques d'instructions:

* Affectations d'une valeur à une _variable_
* Le saut conditionnel "If"
* Les répétitives "Pour" et "Tant que"
* Optionnel: le saut inconditionnel "Goto"

+++

### Langage procédural

Il s'agit simplement de pouvoir regrouper un ensemble d'instructions nommé __procédure__ (ou *routine* ou *sous-routine*).

```python
Procédure Quelconque:
    Instruction 1
    Instruction 2
    ...
    Instruction n
```

On parle de __programme modulaire__ lorsque regroupe thématiquement des procédures dans un *module* (ou *bibliothèque* ou *paquet*)

+++

### Langage orienté objet 1/2

Dans ce type de langage, les programmes sont organisés autour de briques logicielles appelées *Objets* qui:

* représente un concept, une entité réelle ou non
* possède une représentation interne (*attributs* ou *slots*)
* disposent de *méthodes* ou *slots*:
  * récupérer/changer sa répresentation interne
  * exécuter des traitements
  * interagir avec d'autres objets

+++

### Langage orienté objet 2/2

```java
 class Ballon {
    double rayon;          // Attribut
    Ballon(double rayon) { // Construction
      this.rayon = rayon;
    }
    void gonfler() {       // Méthode
      this.rayon = this.rayon + 1;
    }
    void collision(Ballon autre){
      double rayon = (this.rayon + autre.rayon)/2;
      this.rayon = autre.rayon = rayon;
    }
  }
```

+++

### Aparté : Langage déclaratif

On parle de *programmation déclarative* lorsque l'on décrit le résultat attendu, les objectifs (**quoi**) sans donner la manière de le faire (**comment**).
Exemple: page HTML5 minimaliste

```html
<!DOCTYPE html>
<html>
<head><title>This is Hello World page</title></head>
<body>
<h1>Hello World</h1>
</body>
</html>
```

---

@transition[fade]

## Généralités sur le langage Python

+++

### Caractéristiques du langage

Créé en 1991, Python est un langage multi-paradigme:

* Impératif et procédural, orienté-objet
* Fourni avec un interpréteur (usage dominant) qui:
  * infère le type des variables lors de l'exécution (typage dynamique)
  * gère la mémoire automatiquement (ramasse-miettes)
* qui dispose d'une grande bibliothèque de base (modules)
* Version actuelle: **3.8**

+++

### Outils d'édition du code Python

* *Thonny* (cette UE, S2)
* *Visual Code*
* *Spyder* (Calcul scientifique)
* NetBeans, *PyCharm*
* *Jupyter Notebook* (voir S2)

[Liste complète](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)

+++

### Exemple d'un programme Python

```python
print('Hello World!!')
```

Test via Thonny:

* en mode interactif
* en mode script

_Par convention, les scripts Python ont pour extension **\*.py**_

---

@transition[fade]

## Les variables

+++

### Variable (définition)

Une variable est une zone de la mémoire dans laquelle une valeur est stockée.

Elle est désignée par:

* un **nom** pour le programmeur
* une **adresse** pour l'ordinateur

La fonction *id* renvoie un nombre unique (~ adresse) qui qualifie une variable.

+++

### Type d'une variable

Le **type** d'une variable définit les opérations valides pour elle.

Types élémentaires:

* Les nombres entiers
* Les nombres "réels" ou "à virgule"
* Les chaînes de caractères
* Les booléens

La fonction *type* renvoie le type d'une variable.

+++

### Déclaration d'un variable

En Python, la **déclaration** et l'**initialisation** d'une variable se fait de manière simultanée.

```python
In [1]: a = 2

In [2]: type(a)
Out[2]: int

In [3]: id(a)
Out[3]: 4525733248
```

+++

#### Remarques sur le typage 1/2

* Le type d'une variable est donné par le type de l'expression à droite du = (*Inférence de type*)
* Toute variable a un type (*Typage fort*) (qui peut changer lors de l'éxécution (*Typage dynamique*)

+++

##### Remarques sur le typage 2/2

```python
In [1]: a = 2

In [2]: type(a)
Out[2]: int

In [3]: a = 3.14159

In [4]: type(a)
Out[4]: float

In [5]: type(3.14159)
Out[5]: float
```

---

## Les types de base de Python

+++

### Les types numériques: *int*

* entier avec précision arbitraire
* attention, le type *long* existait dans les versions précédentes

```python
In [1]: type(2)
Out[1]: int

In [2]: 2**1024
Out[2]: 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
```

+++

### Les types numériques: *float*

* nombre à virgule avec une précision **fixe**
  `$$[2.26.. * 10^{-308}, 1.79.. * 10^{308}]$$`

* Tous les réels **ne sont pas représentables** par le type _float_

```python
In [1]: 1.79e308
Out[1]: 1.79e+308
In [2]: 1.79e308*10
Out[2]: inf
In [3]: type(1.79e308*10)
Out[3]: float
In [4]: 1e20 + 1
Out[4]: 1e+20
```

+++

### Autres types numériques

Seront également évoqués si besoin en TP:

* *complex* : les nombres complexes
* *decimal* : les nombres décimaux
* *fraction* : les nombres rationnels
  
pour mémoire:
*float* $\subset$ *decimal* $\subset$ *fraction* $\subset$ $\mathbb{R}$

type *int* := $\mathbb{Z}$

+++

### Opérations sur les types numériques

* Arithmétique usuelle: +, -, *, /
* Division entière: a // b (arrondi vers $-\infty$)
* Reste de la division entière: a % b
* Puissance: a ** b  ou  pow(a,b)
* Valeur absolue: abs(a)

+++

### Le type booléen

* Il permet de représenter les valeurs de vérité *True* ou *False*
* Opérations sur les booléens (priorité décroissante):
  * *not*: négation logique
  * *and*: "et" logique
  * *or*:  "ou" logique

```python
In [1]: type(True)
Out[1]: bool

In [2]: True and not False
Out[2]: True
```

+++

### Les chaines de caractères 1/2

Les chaînes de caractères sont délimitées par les simples ou doubles guillemets.

L'opération de **concaténation** de deux chaînes est effectuée par le symbole *+*.

+++

### Les chaines de caractères 2/2

```python
In [1]: a = 'abc'

In [2]: b = 'def'

In [3]: a + b
Out[3]: 'abcdef'
```

+++

### Le type NoneType

* *None* est une valeur spéciale pour indiquer qu'une variable *existe* mais *n'a pas de contenu connu* (valeur manquante)
* Peut indiquer également "n'a pas de sens"

```python
In [1: a
...
NameError: name 'a' is not defined

In [2]: a = None

In [3]: a
```

+++

### Conversion implicite entre types numériques

```python
In [1]: type(1+2.)
Out[1]: float

In [2]: 2**100000 + 5.
...
OverflowError: int too large to convert to float
```

**Ccl**: calcul mixte int/float -> float

+++

### Conversion implicite entre types 1/2

Par **convention**, le *True* "équivaut" à 1 et *False* à 0 dans les calculs numériques.

```python
In [1]: True * 2
Out[1]: 2
```

+++

### Conversion implicite entre types 2/2

A l'opposé, *0*, *0.* ou *None* sont considérées comme *False*, sinon *True* dans les expressions booléennes.

```python
In [1]: not 0
Out[1]: True
```

+++

### Conversion explicite entre types

On peut forcer la conversion avec la syntaxe:

```python
    <type>(<expression>)
```

Exemples:

```python
In [1]: int(4.7)
Out[1]: 4

In [2]: bool(0)
Out[2]: False

In [3]: str(4.7)
Out[3]: '4.7'

In [4]: float('4.7')
Out[4]: 4.7
```

---

## Entrées-Sortie Clavier/Ecran

+++

### Affichage à l'écran

Syntaxe sur la fonction *print*:

```python
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

* ... : *print* accepte une suite de valeurs converties en *str*
* sep: le séparateur
* end: le caractère de fin
* file : flux de sortie (sys.stdout est l'écran)
* flush : force à vider le flux immédiatement.

+++

#### Exemples d'affichage 1/2

```python
In [1]: année = 2020

In [2]: print(année)
2020

In [3: print("année", année)
année 2020
```

+++

#### Exemples d'affichage 2/2

```python
In [4]: print("l'année", année, end=""); print(" est un bon cru !!")
l'année  2020 est un bon cru !!

In [5]: print(année, année*2, année / 2, type(année), sep=", ")
2020, 4040, 1010, <class 'int'>
```

On remarque:

* Il n'a pas de "Out" (Output) pour *print*
* *Confusion usuelle*: l'affichage à l'écran n'est pas un retour de la fonction *print*.

+++

#### Affichage formaté avec .format 1/2

```python
In [1]: nom = "toto"
In [2]: age = 8

In [3]: "Salut {}, tu as {} ans".format(nom, age)
Out[3]: 'Salut toto, tu as 8 ans'

In [4]: "Salut {1}, tu as {0} ans".format(nom, age)
Out[4]: 'Salut 8, tu as toto ans'
```

+++

#### Affichage formaté avec .format 2/2

On peut également nommer les champs

```python
In [5]: "Salut {prenom}, tu as {age} ans".format(age=age, prenom=nom)
Out[5]: 'Salut toto, tu as 8 ans'
```

+++

#### Une version moderne, les f-strings

On peut directement désigner des expressions !!!

```python
In [1]: nom = "toto"
In [2]: age = 8

In [3]: f"Salut {nom} !"
Out[3]: 'Salut toto !'

In [4]: f"Le double de {age} est {2*age}"
Out[4]: 'Le double de 8 est 16'
```

A partir de Python 3.6.

+++

### Saisie Utilisateur

Fonction *input* :

```python
  input(prompt=None)
```

* retourne la chaîne de caractères saisie.
* Il est souvent nécessaire de **convertir explicitement dans le type désiré** ensuite.

```python
In [1]: a = int(input('Nombre de pas ? '))
Nombre de pas ? 12

In [2]: b = float(input('pi ? '))
pi ? 3,14
...
ValueError: could not convert string to float: '3,14'
```

C'est la convention anglaise pour les *float*.

---

## Structures conditionnelles

if, else, elseif

+++

### Instruction if, else

```python
if <condition>:
    <instructions si True>
[else:
    <instructions si False>]
```

* La partie else est optionnelle
* **L'indendation est obligatoire car elle marque le début et la fin d'un bloc d'instructions**

+++

##### Condition dans un if 1/2

Une condition peut-être:

* une expression booléenne construite par:
  * un opérateur de comparaison: <=,  <,  >,  >=
  * un opérateur d'égalité: ==, !=, <>
  * un opérateur d'identité: *is*, *is not*
  * un opérateur d'appartenance : *in*, *not in*

+++

##### Condition dans un if 2/2

Une condition peut-être aussi:

* une valeur numérique: 0 ou 0. équivaut à *False* sinon *True*
* une chaine de caractères: '' équivaut à *False* sinon *True*
* *None* équivaut à *False*
* *etc*

Les conditions peuvent être combinées par *not*, *and* et *or*

+++

#### Exemples if

```python
In [1]: a = int(input('Nombre de pas ? '))
Nombre de pas ? 9680

In [2]: if a > 8000:
          print('Vous avez fait le nombre de pas journaliers recommandé.')
        else:
          print('Faire plus d\'exercice.')
Vous avez fait le nombre de pas journaliers recommandé.

In [3]: if a > 8000: print('bravo')
bravo
```

+++

### Instruction elif

* *elif* est une contraction de *else if* qui n'oblige pas à une indentation supplémentaire
* C'est le "switch case" de Python.

```python
In [1]: a = 7

In [2]: if a < 0:
          print('a est négatif')
        elif a % 2 == 0:
          print('a est pair')
        elif a % 3 == 0:
          print('a est divisible par 3')
        else:
          print('a est un nombre positif, impair et non divisible par 3')
a est un nombre positif, impair et non divisible par 3
```

+++

### Démonstration `!`

* Conditions if imbriquées : a $\in$ [0,1]
* [Année bissextile](https://fr.wikipedia.org/wiki/Ann%C3%A9e_bissextile)
* Tortue (version modifiée du TP1)

---

## Répétitives

while, break, for, continue

---

### Répétitive *"Tant que"*

Syntaxe:

```python
while <condition>:
    <instructions>
```

La condition est évaluée **avant** chaque éxécution des instructions.

Conditions de sortie du "while":

* La condition n'est pas vérifiée.
* Une sortie explicite par *break*.
* Crash du programme...

+++

##### Cas fréquents d'utilisation *"Tant que"* 1/2

* Répéter *n* fois

```python
cpt = 0
while cpt < n:
  <instructions>
  cpt = cpt + 1
```

* Compter le nombre d'itérations

```python
cpt = 0
while <condition>:
  <instructions>
  cpt += 1
```

+++

#### Cas fréquents d'utilisation *"Tant que"* 2/2

* Parcourir un intervalle de valeurs $[a,b]$ par pas de $eps$

```python
x = a
while x <= b:
  <instructions>
  x += eps
```

* Une boucle d'événements

```python
while True:
  <instructions>
  if <événement particulier>:
     break
```

+++

##### Petits exos sur "while"

* Combien de fois peut on diviser un nombre par deux ?
* Compter le nombre de entiers impairs entre 1 et 100 divisibles par 3 mais pas par 7.
* Racine carrée entière:
  Etant donné un entier $n$, déterminer le plus grand nombre entier $r$ tel que $r^2 \leq n$.

---

### Répétitive for

Syntaxe:

```python
for <variable> in <sequence>:
     <instructions>
```

La séquence peut être:

* Une plage de valeurs avec *range*
* Une chaîne de caractères
* Une liste, un tuple (plus tard)
* personnalisée ...

Le terme anglais est *iterable*.

+++

#### Instruction *range*

Syntaxe:

```python
range(stop) -> range object
range(start, stop[, step]) -> range object
```

Cas d'utilisation:

* range(i, j) -> i, i+1, i+2, ..., j-1.
* range(i) -> 0, 1, ..., i-1..

Attention, step peut être négatif.

+++

#### Exemples *for* avec *range*

```python
In [1]: for i in range(1,10):
          print(i, end=' ')
###
1 2 3 4 5 6 7 8 9
In [2]: for i in range(5):
          print(i, end=' ')
###
0 1 2 3 4
In [3]: for i in range(8, 0, -1):
          print(i, end=' ')
###
8 7 6 5 4 3 2 1
```

+++

#### Exemple *for* avec *str*

```Python
In [1]: for c in 'Python':
          print(c, end=', ')
###
P, y, t, h, o, n,

In [2]: cpt = 0
        for c in 'Pythonneries':
            if c == 'e':
              cpt += 1
        print('Nombre de "e": ', cpt)
###
Nombre de "e":  2
```

+++

#### Exercice d'application

`$$\lim_{n \rightarrow +\infty} 4 \sum_{k=0}^{n} \frac{(-1)^{k}}{2k+1} = \pi$$`

Ecrire un programme basé sur cette formule qui approxime $\pi$:

```Python
In [1]: n = 10**6; som = 0

In [2]: for k in range(n+1):
          som = som + (-1)**k / (2*k+1)

In [3]: print(4*som)
3.1414926535900345

In [4]: import math; print(math.pi)
3.141592653589793
```

+++

### Bonus: instruction *continue*

*continue* permet d'interrompre une itération:

* On retourne au test de la condition dans *while*
* Prochaine itération dans *for*

```python
In [1]: for i in range(10):
          if i % 2 == 0:
            continue
          print(i, end=' ')
1 3 5 7 9
```

+++

### Bonus: *else* dans *while* et *for*

* *else* est exécuté si:
  * la condition du *while* est *False*
  * *for* a parcouru toute la séquence
* *else* n'est pas exécuté si interruption par un *break*.

```python
In [2]: for i in range(10):
          print(i, end=' ')
        else:
          print('\nTerminé')

0 1 2 3 4 5 6 7 8 9
Terminé
```

---

## Structures de donnnées

liste, tuple, dictionnaire

---

### Liste

Une **liste** est une structure de données qui contient une séquence de valeurs.

Syntaxe:

```python
[<valeur_1>, <valeur_2>, ..., <valeur_n>]
```

* Les valeurs ne sont pas nécessairement de même type.
* Equivalent à avoir un ensemble de variables regroupées en une seule variable.
* Une liste est une séquence.

+++

#### Exemples de listes

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: Sam = [28 , 'Toronto', False, None]

In [3]: Jeff = [70, 'Cambridge', True, 25]

In [4]: People = [Sam, Jeff]

In [5]: print(People)
[[28, 'Toronto', False, None], [70, 'Cambridge', True, 25]]
```

+++

#### Longueur d'une liste / liste vide

```python
In [1]: len(['rouge', 'vert', 'bleu'])
Out[1]: 3

In [2]: L = []

In [3]: print(len(L))
0
```

+++

#### Test d'une liste vide

```python
if L:        #   ou len(L) > 0
    print('non vide')
else:
    print('vide')
```

+++

#### Utilisation d'une liste

On peut rappeler un élément particulier d'une liste par son **indice**.</br>
Pour une liste de longueur *n*, l'indice est un **entier** entre **0** et **n-1**.

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: couleurs[0]
Out[2]: 'rouge'

In [3]: couleurs[5]
...
IndexError: list index out of range
```

+++

#### Liste: Indiçage négatif

Pour faciliter l'accès des derniers éléments d'une liste, *Python* a introduit l'indiçage négatif.

|liste| 'h' | 'e' | 'l' | 'l' | 'o' |
|-|-----|-----|-----|-----|-----|
|indice positif| 0   | 1   | 2   | 3   | 4   |
|indice négatif| -5  | -4  | -3  | -2  | -1  |

Le dernier élément de la liste  toujours l'indice -1.

+++

#### Extraction d'une sous-liste 1/3

Syntaxe ($\sim$ *range*):

```python
       L[<start>:<stop>:<step>]
```

Quelques cas fréquents (L est une liste):

* Eléments entre l'indice 2 (inclus) et l'indice 5 (exclus):</br>
  L[2:5]
* Eléments à partir de  l'indice 4:</br>
  L[4:]
* Les 10 premiers éléments:</br>
  L[:10]

+++

#### Extraction d'une sous-liste 2/3

* Duplication de la liste:</br>
  L[:]
* Un élément sur 2:</br>
  L[::2]

+++

#### Extraction d'une sous-liste 3/3

Quelques cas fréquents avec indice négatif:

* Les 5 derniers éléments:</br>
  L[-5:]
* Tout sauf les derniers 3 éléments:</br>
  L[:-3]
* Duplication de *a* dans l'ordre inverse:</br>
  L[::-1]

+++

#### Affecter une valeur à une liste existante

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: couleurs[0] = 'jaune'

In [3]: couleurs
Out[3]: ['jaune', 'vert', 'bleu']

In [4]: couleurs[:2]= [34, 48]

In [5]: couleurs
Out[5]: [34, 48, 'bleu']
```

+++

#### Insérer un élément en fin de liste : *append*

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: couleurs.append('cyan')

In [3]: couleurs
Out[3]: ['rouge', 'vert', 'bleu', 'cyan']

In [4]: L = []   ## liste vide !!!

In [5]: L.append(4)

In [6]: L
Out[6]: [4]
```

+++

#### Insérer un élément : *insert*

Syntaxe ($\sim$ *range*):

```python
    L.insert(<indice>, <element>)
```

Insère avec décalage vers la fin:

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: couleurs.insert(2, 'cyan')

In [3]: couleurs
Out[3]: ['rouge', 'vert', 'cyan', 'bleu']
```

+++

#### Concaténer deux listes 1/2

Rappel: Concaténer c'est mettre bout à bout deux structures de données.

Deux syntaxes:

```python
    L = L1 + L2 ou L1+=L2
    L1.extend(L2)
```

```python
In [1]: ['rouge', 'vert', 'bleu'] + ['r', 'v', 'b']
Out[1]: ['rouge', 'vert', 'bleu', 'r', 'v', 'b']
```

+++

#### Concaténer deux listes 2/2

```python
In [2]: couleurs = ['rouge', 'vert', 'bleu']

In [3]: couleurs.extend(['r', 'v', 'b'])

In [4]: print(couleurs)
['rouge', 'vert', 'bleu', 'r', 'v', 'b']
```

+++

#### Suppression d'éléments: *del* ou *remove*

```python
    del L[3] ou del L[3:]    ## par indice
    L.remove(5)              ## la première occurrence
```

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: del couleurs[1]

In [3]: couleurs
Out[3]: ['rouge', 'bleu']

In [4]: couleurs = ['rouge', 'vert', 'bleu', 'vert', 'orange']

In [5]: couleurs.remove('vert')

In [6]: couleurs
Out[6]: ['rouge', 'bleu', 'vert', 'orange']
```

+++

#### Parcours d'une liste par indice

On peut utiliser les indices.

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: for i in range(len(couleurs)):
          print(couleurs[i].upper(), end=', ')
###
ROUGE, VERT, BLEU,
```

On peut très bien faire aussi avec un *while*

+++

#### Parcours d'une liste par itérateur

Rappel: *for* permet d'itérer toute séquence.

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: for couleur in couleurs:
          print(couleur.upper(), end=', ')
###
ROUGE, VERT, BLEU,
```

Très simple, mais on a perdu la position dans la liste !

+++

#### Parcours d'une liste par *enumerate*

```python
In [1]: couleurs = ['rouge', 'vert', 'bleu']

In [2]: for i, couleur in enumerate(couleurs):
          print('indice:', i, 'valeur:', couleur.upper())
###
indice: 0 valeur: ROUGE
indice: 1 valeur: VERT
indice: 2 valeur: BLEU
```

C'est le meilleur choix si l'on a besoin de l'indice en plus de la valeur.

+++

#### Exemple sur les listes 1/2

A partir d'une liste de noms, sélectionner ceux qui commencent ou terminent par une voyelle.

```python
In [1]: voyelles = ['a', 'e', 'i', 'o', 'u', 'y']

In [2]: noms = ['mila', 'mathis', 'anne', 'myriam', 'eloan', 'pierre', 'jules']

In [3]: select = []

In [4]: for nom in noms:
          for voyelle in voyelles:
            if nom[0] == voyelle or nom[-1]==voyelle:
              select.append(nom)
              break

In [5]: select
Out[5]: ['mila', 'anne', 'eloan', 'pierre']

```

+++

#### Exemple sur les listes 2/2

Une version plus compacte:

```python
In [1]: voyelles = 'aeiouy'

In [2]: noms = ['mila', 'mathis', 'anne', 'myriam', 'eloan', 'pierre', 'jules']

In [3]: select = []

In [4]: for nom in noms:
          if nom[0] in voyelles or nom[-1] in voyelles:
              select.append(nom)

In [5]: select
Out[5]: ['mila', 'anne', 'eloan', 'pierre']

```

---

### Tuple

Un **tuple** est une structure de données qui contient une séquence de valeurs.

Syntaxe:

```python
      (<valeur_1>, <valeur_2>, ..., <valeur_n>)
```

+++

#### Comparaison *Liste*/*Tuple*

|             |   Liste   | Tuple |
|:-----------:|:---------:|:-----:|
|    Taille   | dynamique |  fixe |
|    Ajout    |    oui    |  non  |
| Suppression |    oui    |  non  |
|   Parcours  |    oui    |  oui  |
|  Test 'in'  |    oui    |  oui  |
|   Rapidité  |     -     |   +   |
|   Mémoire   |     -     |   +   |

+++

#### Exemple stockage avec *tuple*

```python
In [1]: t = ('a', 5000, 'c', 234)

In [2]: t[2:4]
Out[2]: ('c', 234)

In [3]: t = t[:2] + ('b', 858) + t[2:]

In [4]: t
Out[4]: ('a', 5000, 'b', 858, 'c', 234)
```

+++

#### Dépliement (unpacking) d'un tuple (ou f'une liste)

Permet de faire l'affectation multiple de valeurs

```python
In [1]: (a, b, c) = (1, '2', '3.0')

In [2]: print(a, b, c)
1 2 3.0

In [3]: a, b, c = 1, '2', '3.0'  ## syntaxe usuelle identique
```

Echange de valeurs de variables

```python
In [1]: a, b = b, a
```

+++

#### Retour sur *enumerate*

```python
In [1]: lettres = 'abcd'

In [2]: for el in enumerate(lettres):
            print(el)
####
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
```

* *enumerate* renvoie une séquence de tuples (*indice*, *valeur*) que l'on a déplié.

---

### Dictionnaire

Un **dictionnaire** est une structure de données qui contient une séquence de couples (clé, valeur).

Syntaxe:

```python
    {<cle_1>: <valeur_1>, ..., <cle_n>: <valeur_n>}
```

Exemple:

```python
In [1]: Sam = { 'age': 28, 'location': 'Toronto', 'active': False, 'phd': None}

In [2]: Sam['age']   # ou Sam.get('age')
Out[2]: 28
```

+++

#### Propriétés d'un dictionnaire

* Les clés sont uniques, les valeurs peuvent être mutiples.
* Les clés sont immuables (chaînes, nombres, tuples) i.e. ne sont pas modifiables.
* Les valeurs peuvent être mise à jour.

+++

#### Ajout/Mise à jour

```python
In [1]: Sam = {'age': 28}

In [2]: Sam['affiliation'] = 'La Rochelle'

In [3]: Sam['age'] = 29

In [4]: Sam
Out[4]: {'age': 29, 'affiliation': 'La Rochelle'}
```

+++

#### Existence / Test d'une clé

```python
In [1]: Sam = {'age': 28}

In [2]: 'location' in Sam
Out[2]: False

In [3]: Sam['location']
KeyError: 'location'
```

+++

#### Mise à jour/Suppression

```python
In [1]: Sam = {'age': 29, 'affiliation': 'La Rochelle'}

In [2]: Sam.update({ 'age': 30, 'location': 'Toronto'})

In [3]: Sam
Out[3]: {'age': 30, 'affiliation': 'La Rochelle', 'location': 'Toronto'}

In [4]: del Sam['location']

In [5]: del Sam['location']
KeyError: 'location'
```

+++

#### Parcours d'un dictionnaire

Trois façons de parcourir un dictionaire *d*:

* *d.items()*: séquence de paires *cle*:*valeur*.
* *d.keys()* : séquence des clés. (ou seulement d)
* *d.values()*: séquence des valeurs.

```python
In [1]: Sam = {'age':43, 'affiliation':'Toronto', 'active': False}
In [2]: for cle, valeur in Sam.items():
            print(f"'{cle}'={valeur}", end=" -- ")
'age'=43 -- 'affiliation'=Toronto -- 'active'=False --
```

+++

#### Exemples sur les dictionnaires

* Compter le nombre d'occurrences d'une lettre de l'alphabet dans un texte.
* La Famille Simpson

Exercice:

* Imaginer un dictionnaire regroupant les membres d'un club sportif:
  * la clé (un entier) répresente le numéro de licence
  * la valeur est un dictionnaire stockant le nom, l'age, cotisation, actif.

---

## Fonctions

* Qu'est ce qu'une fonction ?
* Comment définir une fonction ?
* Qu'est ce qu'un paramètre ? une valeur de sortie ?
* Comment appeler une fonction ?

+++

### Fonctions et paramètres 1/2

Les fonctions sont un moyen de :

* Regrouper un ensemble d’instructions en les nommant.
* Finaliser la résolution d'un sous-problème pour réutilisation.

Syntaxe pour la **définition** d'une fonction:

```python
def <nom_de_la_fonction>(<parametre_1>, ..., <parametre_n>):
    <instructions>
```

+++

### Fonctions et paramètres 2/2

```python
def <nom_de_la_fonction>(<parametre_1>, ..., <parametre_n>):
    <instructions>
```

Si l’exécution de ces instructions dépend de certaines valeurs, on parlera de fonction avec des *paramètres*.

Les parenthèses sont obligatoires, même si la fonction n'a pas aucun paramètre.

+++

### Exemple de fonction sans paramètre

```python
from datetime import datetime

def bonjour():
  heure = datetime.now()
  print(f"Bonjour, il est {heure}")
```

+++

### Exemple de fonction avec un paramètre

```python
def aff_somme_n_entiers(n):
  som = 0
  for i in range(1, n+1):
    som = som + i
  print(f"Résultat: {som}")
```

+++

### Exemple de fonction avec 2 paramètres

```python
def aff_diff_ch(ch1, ch2):
  ch1_u = ch1.upper()
  ch2_u = ch2.upper()
  if ch1_u == ch2_u:
    print(f"{ch1} et {ch2} sont égales à la casse près")
  else:
    print(f"{ch1} et {ch2} sont différentes")

```

+++

### Nombre et types de paramètres

Les fonctions ont généralement *un nombre fixe* de paramètres (0 à n) de type:

* basique: *int*, *float*, *bool*, *str*, ...
* liste, tuple, dictionnaire
* fonctions...
* objets (non traité dans ce cours)

Python permet de définir une fonction avec un nombre variable de paramètres (\*args, \*\*kwargs non traité dans ce cours) => une liste.

+++

### L'instruction *return*

L'*instruction* **return** indique ce que *renvoie* la fonction.

```python
def somme_n_entiers(n):
  som = 0
  for i in range(1, n+1):
    som = som + i
  return som
```

Il peut y avoir plusieurs **return** dans une même fonction.

+++

### Type de retour d'une fonction

Idem que les paramètres:

* basique: *int*, *float*, *bool*, *str*, ...
* liste, tuple, dictionnaire
* fonctions...
* objets (non traité dans ce cours)

Pour retourner plusieurs valeurs, on utilisera un tuple, une liste ou dictionnaire.

+++

### Retourner plusieurs valeurs

Pour retourner plusieurs valeurs, on utilisera un tuple, une liste ou dictionnaire

```python
def decomposition(n, m):
  a = n // m
  b = n % m
  return (a, b)  
  # return {'quotient': a, 'reste': b}
```

+++

### Une fonction sans return `?!`

Une fonction sans *return* explicite "retournera" la valeur spéciale *None*.
On parlera alors de **procédure** dans certains langages de programmation.

Trois formes équivalentes:

```python
def f1(a, b):   # pas de return
  c = a + b

def f2(a, b):   # la dernière expression n'est pas retournée
  c = a + b
  c

def f3(a, b):   # return explicite sans expression
  c = a + b
  return
```

+++

### Appel de fonction 1/2

Syntaxe pour l'appel d'une fonction (paramètres effectifs):

```python
<nom_de_la_fonction>(<val_1>, ..., <val_n>)
```

On parle aussi de valeurs d'appel de la fonction

+++

### Appel de fonction 2/2

Rappel pour la définition (paramètres formels):

```python
def <nom_de_la_fonction>(<parametre_1>, ..., <parametre_n>):
    <instructions>
```

Tout ce passe comme si les **paramètres effectifs** sont automatiquement copiés dans les **paramètres formels**:

```python
<parametre_1> = <val_1>
...
<parametre_n> = <val_n>
```

+++

### Passage par valeur

La fonction travaille donc avec une copie des paramètres effectifs.

* Pour les types basiques, la fonction ne modifie pas les paramètres effectifs.
* Pour les listes et les dictionnaires, la fonction **modifie** les paramètres effectifs.
On parlera alors d'effet de bord de la fonction (modification de variables externes).

+++

### Exemples de fonctions

* Passage par valeurs de listes

+++

### Exemples de fonctions

* Palindromes
* Nettoyage de dictionnaires
* Les paramètres sont fun !

+++

### Compléments : Valeurs par défaut 1/2

On peut donner des valeurs par défaut à certains paramètres que l'on positionne **à droite**:

```python
In [1]: def f(a,b=2):
          return a**b
In [2]: f(2)
Out[2]: 4

In [3]: f(4,3)
Out[3]: 64
```

+++

### Compléments : Valeurs par défaut 2/2

```python
In [4]: def f(b=2, a):
          return a**b
File "<ipython-input-6-8d9bc7ce0f4b>", line 1
   def f(b=2, a):
         ^
SyntaxError: non-default argument follows default argument
```

+++

### Compléments : Ordre des paramètres

```python
In [4]: def f(b=2, a):
          return a**b
  File "<ipython-input-6-8d9bc7ce0f4b>", line 1
    def f(b=2, a):
         ^
SyntaxError: non-default argument follows default argument
```

+++

### Exemples de fonctions

* Année bissextile (défaut: 2020, None)

+++

### La récursivité

Une fonction est dite récursive si elle se calcule en faisant appel à elle même.

```python
def factorielle(n):
  if n < 2:
    return 1
  return n * factorielle(n-1)
```

Très utile dans le paradigme 'Diviser pour régner' (cf. dichotomie TP5)

+++

### Exemples de fonctions

* Factorielle
* Palindromes

---

## Portée des variables

Quand et comment mes variables sont accessibles ?

+++

### Cas simples 1/2

On a déjà vu que les variables n'existent que si elles ont été assignées (valeur ou *None*)

```python
In [1]: a
NameError: name 'a' is not defined

In [2]: a = 3

In [3]: a
Out[3]: 3
```

Idem pour les fonctions.

+++

### Cas simples 2/2

Et dans un bloc:

```python
In [1]: for i in range(10):
          a=3
In [2]: print(a, i)
3 9
```

On parle du niveau *global* ou *principal*.

+++

### Portée des variables: Fonctions 1/5

```python
In [1]: def f():
   ...:     a = 2 * x
In [2]: f()
....
NameError: name 'x' is not defined
```

* La définition de la fonction *f* ne pose pas de problème.
* L'erreur est détectée **à l'appel** de *f*.

+++

### Portée des variables: Fonctions 2/5

```python
In [1]: a = 1

In [2]: def f():
          print(a)

In [3]: f()
1
```

* Les variables du niveau supérieur sont utilisables dans la fonction.
* Considéré comme une *mauvaise pratique* car *f* **est paramétrée** par *a*.

+++

### Portée des variables: Fonctions 3/5

```python
In [1]: a = 1

In [2]: def f():
          a = 2

In [3]: f()

In [4]: a
Out[4]: 1
1
```

* Dans f, *a*  est vue comme une variable locale.
* La variable globale *a* est surchargée localement mais inchangée globalement.

+++

### Portée des variables: Fonctions 4/5

```python
In [1]: def f(b):
          a = 3
In [2]: a
NameError: name 'a' is not defined

In [3]: b
NameError: name 'b' is not defined
```

Les variables **locales** et les **paramètres** formels n'existent pas à l'extérieur d'une fonction.

+++

### Portée des variables: Fonctions 5/5

```python
In [1]: a = 1

In [2]: def f():
    ...:     a = 2 * a

In [3]: f()
...
UnboundLocalError: local variable 'a' referenced before assignment
```

La variable *a* est prioritairement considérée comme locale.

+++

### Variables globales

Avertissement : ce qui suit est généralement considéré comme une mauvaise pratique.

```python
In [1]: a = 1
In [2]: def f():
          global a
          a = 2 * a
In [3]: f()
In [4]: a
Out[4]: 2
```

* La variable *a* est maintenant vue comme globale.
* Toute modification de *a* à l'intérieur de la fonction la modifie à l'extérieur.

+++

### Variables non locales

Avertissement : ce qui suit est pratique mais rarement utilisé (Python 3)

On parle ici du cas de fonctions locales définies dans une autre fonction (def dans def)

Le mot-clé **non local** permet de faire référence à une variable d'un niveau supérieur sans revenir au niveau global.

---

## Fonctions externes et modules

* Comment organiser son code pour le réutiliser ?
* Comment utiliser du code Python fait par d'autres ?
* Module vs Programme

+++

### Définition d'un module Python

* Les modules en Python sont des fichiers Python avec une extension .py.
* Le nom du module est le nom du fichier.
* Un module Python peut définir un ensemble:
  * de fonctions
  * de variables
  * de classes (en programmation orientée objet)

+++

### Exemple: module *racine*

```python
# Contenu du fichier "racine.py"
def racine_dicho(x):
    min, max, eps = 0, x, 1e-6
    while True:
        r = (min + max) / 2
        if abs(r * r - x) < eps:
            break
        elif r * r < x:
            min = r
        else:
            max = r
    return r
```

+++

### Exemple: réutilisation de racine

```python
# Contenu du fichier  "comp_rac.py"
import math
import racine

x = float(input('x ? '))
if abs(math.sqrt(x) - racine.racine_dicho(x)) < 1e-6:
    print("Les valeurs sont les mêmes")
else:
    print("Roger, on a un problème !!!")
```

+++

### Généralités: Directive import et ses conventions 1/3

```python
# Contenu du fichier "xxx.py"  -> module xxx
ma_variable = <une expression>

def ma_fonction(<les paramètres>):
    <le code>
    return <son retour>

# Contenu du fichier "yyy.py"
import xxx   # nom du module à importer

v = xxx.ma_variable
a = xxx.ma_fonction(4) # directement
```

+++

### Généralités: Directive import et ses conventions 2/3

* Le module xxx à importer est dans le même répertoire que le module yyy qui l'importe
* L'interpréteur connait le chemin de recherche pour les modules de la bibliothèque standard
* On doit préciser le nom du module chaque fois à moins de faire un raccourci:

```python
import xxx

f = xxx.ma_fonction # indirectement: raccourci local
a = f(4)
```

+++

### Généralités: Directive import et ses conventions 3/3

```python
import math
import racine
def sqrt(x):
    return racine.racine_dicho(x)
def print(x):
    pass
```

* Le module créé par l'utilisateur est prioritaire à celui fourni par Python -> print du système est écrasé.
* Pas de confusion entre *sqrt* et *math.sqrt*

+++

### Exemples déjà vus en TP

```python
import math
rc4 = math.sqrt(4.0)

import random
alea = random.randint(1, 10)

import datetime
maintenant = datetime.datetime.now()
print(maintenant)
```

+++

### Modules/packages

* On peut vouloir regrouper des modules au sein d'un paquet (*package*)
* Un paquet peut contenir des sous-paquets (répertoire avec \_\_init\_\_.py)
* Les modules sont à l'intérieur de cette arborescence

[Exemple de la documentation officielle](https://docs.python.org/fr/3/tutorial/modules.html#packages)

+++

### Modules: help, dir

* *help*(<module> ou <fonction> ou <variable>) permet d'accéder à une aide dans la console
* *dir*(<module> ou  <variable>) donne la liste des noms dans l'espace de nommage local:
  * dir()
  * dir(math) ou dir(datetime)
  * a = "" ; dir(a)

+++

### Directive from ... import ... as ...

* On peut décider de n'importer que certains symboles (variables, fonctions, ...)

```python
from racine import racine_dicho
a = racine_dicho(4)
```

* Egalement les renommer localement

```python
from racine import racine_dicho as mon_sqrt
from math import sqrt as py_sqrt, exp as py_exp
a = mon_sqrt(4)
```

+++

### Directive from ... import *

* On peut décider de tout importer:

```python
from racine import *

a = racine_dicho(4)
```

Il existe un mécanisme via \_\_init\_\_.py pour contrôler l'importation.

* Pratique déconseillée car on ne maîtrise pas totalement ce qui est importé.<br>
  On devrait plutôt faire:

```python
from turtle import forward, left, right, done
```

+++

### Quelques modules fournis

* random: fonctions pour produire des nombres aléatoires
* math: opérations mathématiques basiques (cosinus,sinus,exp,etc.)
* turtle: dessin à la tortue
* os: Interagir avec le système d'exploitation
* time: La date, heure, ...
* tkinter: Créer une interface graphique

[Liste complète](https://docs.python.org/3.6/library/index.html)<br>
[Pour aller plus loin](https://docs.python.org/fr/3/tutorial/modules.html)

+++

### Autres modules populaires

* Numpy, Scipy, Pandas: Calcul scientifique.
* Matplotlib: Dessin 2d (courbes, histogrammes, *etc*).
* Django, Flask: Faire des sites par programmation.
* Pillow: Manipuler des images.

Egalement, il existe des modules pour:

* Interagir avec les réseaux sociaux.
* Analyser les pages web.
* ...

+++

### Module vs Programme 1/2

Un module peut contenir:

* des définitions de fonctions
* du code à éxécuter (ex.: une démonstration des fonctions)

Problème: Comment importer des fonctions sans exécuter obligatoirement le code de démo. ?

+++

### Module vs Programme 2/2

Solution: La variable spéciale **\_\_name\_\_** est une chaine de caractère qui vaut:

* le nom du module quand il est importé
* la valeur "\_\_main\_\_" quand il est exécuté.

---

## Fichiers

* Comment charger un fichier texte.
* Comment écrire des données dans un fichier texte
* Comment charger des fichiers au format .csv.

+++

### Modes d'ouverture

```python
f = open('fichier.txt', mode='r')
```

* ‘r’ (read) : Lecture seule
* ‘w’ (write) : Lecture/Ecriture (écrase le fichier existant)
* ‘a’ (append) : Lecture/Ecriture à partir de la fin  

+++

### Lecture d'un fichier texte

```python
f = open('fichier.txt', mode='r')
```

Méthodes de base:

* f.read(n) : lire *n* caractères
* f.readline() : lire une ligne
* f.readlines() : tout lire

+++

### Exemple : Lecture d'un fichier texte

```python
f = open('fichier.txt', mode='r')
lignes = f.readlines()
f.close()
```

ou encore (contexte en Python)

```python
with open('fichier.txt', mode='r') as f:
    lignes = f.readlines()
```

* Fermeture automatique du fichier avec *with*
* Remarque: Chaque ligne est terminée par '\n'

+++

### Ecriture dans un fichier texte

Méthodes de base:

```python
# Ecrit une chaine dans f et retourne le nombre de caractères écrits
n = f.write(chaine)
# Autre possibilité
print(3, 'Chaine', file=f)
```

+++

### Exemple : Ecriture d'un fichier texte

```python
f = open('fichier.txt', mode='w')
n = f.write("une première ligne\n")
print("La seconde ligne", file=f)
f.close()
```

* Remarque: On peut également utiliser un *with*

+++

### Aparté: Suppression des '\n'

```python
In [1]: ch = 'Toto\n'

In [2]: ch2 = ch.rstrip()

In [3]: len(ch), len(ch2)
Out[3]: (5, 4)

In [4]: "Toto.n8.88n.8".rstrip("n8.")
Out[4]: 'Toto'
```

+++

### Format JSON

Le format **J**ava**S**cript **O**bject **N**otation permet d'échanger simplement des données entre applications.

Grossièrement, il s'agit d'une chaine de caractères structurée.

Pour nous, il permet de charger/sauvegarder simplement le contenu des variables.

Python fournit le module **json**.

+++

### Conversion d'un objet Python en JSON 1/2

```python
In [1]: import json

In [2]: Lisa = {'age': 8, 'sexe': 'F', 'prenom': 'Lisa', 'nom': 'Simpson'}

Out[3]: json.dumps(Lisa)     # chaine de caractères
Out[3]: '{"age": 8, "sexe": "F", "prenom": "Lisa", "nom": "Simpson"}'
```

Il sait convertir automatiquement :

* dict, list, tuple
* int, float, str, bool, None

+++

### Conversion d'un objet Python en JSON 2/2

```python
In [1]: import json

In [2]: Lisa = {'age': 8, 'sexe': 'F', 'prénom': 'Lisa', 'nom': 'Simpson'}

In[3]: with open('Lisa.json', mode='w') as f:
          json.dump(Lisa, f)

In[4]: with open('Lisa2.json', mode='w') as f:
          json.dump(Lisa, f, indent=4, sort_keys=True)
```

+++

### Conversion d'un objet JSON vers Python 1/2

Rarement on définit une chaine JSON directement

```python
In [1]: import json

In [2]: Lisa_json ='{"age": 8, "School": true}'

In [3]: Lisa = json.loads(Lisa_json)

In [4]: Lisa
Out[4]: {'age': 8, 'School': True}

In [5]: type(Lisa)
Out[5]: dict
```

+++

### Conversion d'un objet JSON vers Python 2/2

Chargement direct par **json.load**

```python
In [1]: import json

In [2]: with open('Lisa.json', mode='r') as f:
              Lisa = json.load(f)
In [3]: Lisa
Out[3]: {'age': 8, 'nom': 'Simpson', 'prénom': 'Lisa', 'sexe': 'F'}

In [4]: type(Lisa)
Out[4]: dict
```

+++

### Lecture d'un fichier .csv

CSV ("Comma-separated values") = des valeurs séparées par des virgules.

Exemple: [place de parking disponibles](https://opendata.larochelle.fr/dataset/stationnement-places-disponibles-en-temps-reel/)

```csv
dp_id;dp_parc_id;dp_libelle;dp_place_disponible;dp_date;dp_nb_places;dp_x;dp_y
15272676;5;VIEUX PORT OUEST;327;23-11-2020 15:51:16;375;379378.69605346315;6570179.209243104
15272677;4;ENCAN;0;04-11-2020 09:27:28;441;379864.062986826;6569682.940808346
15272678;17;VIEUX PORT SUD;339;23-11-2020 15:51:23;430;379925.9973126798;6570032.623815341
15272679;16;VERDUN;329;23-11-2020 15:51:18;430;379670.3771208469;6570946.775614928
15272680;20;MAUBEC;105;23-11-2020 15:51:25;190;380380.7833034035;6570379.618003208
15272681;21;PORT NEUF;162;23-11-2020 15:51:19;171;377155.7006404366;6570849.717103481
```

+++

### Exemple de lecture d'un fichier .csv

```python
import csv

with open('fichier.csv', newline='') as f:
   lecteur = csv.reader(f, delimiter=',', quotechar='"')
   for ligne in lecteur:
      print(ligne)
```

+++

### Exemple d'écriture d'un fichier .csv

```python
import csv

with open('sortie.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lignes)
```

---

## La documentation

Parce ce que:

* Le programmeur n'a pas une mémoire infaillible
* On peut espérer faire du code que les autres vont utiliser (éventuellement sans le lire)

On peut documenter tous les niveaux du code: fonction, ~~classe~~, ~~module~~

Il s'agit de placer une **chaine de caractères** au bon endroit ...

Règles pour la documentation: [PEP 257](https://www.python.org/dev/peps/pep-0257/)

+++

### Conventions pour la documentation simple

* On utilise des triples guillemets pour commencer et finir la ligne.
* La première lettre est en majuscule et on termine la ligne par un point.
* Indentation identique au code.
* On décrit ce que fait la fonction.

+++

### Exemple de documentation simple

```python
In [1]: def carre(x):
   ...:   """Calcul du carré d'un nombre."""
   ...:   return x * x
In [2]: print(carre.__doc__)
Calcul du carré d'un nombre.

In [2]: help(carre)
```

+++

### Pour une documentation plus longue

```python
"""La première ligne décrit la fonction.
  
   Description textuelle de la fonction.
   Description textuelle de la fonction.
   Description textuelle de la fonction.
"""
```

+++

### Exemple de documentation plus riche 1/2

```python
def monpow(a, b):
  """Calcule a à la puissance b
  
    Ici une explication longue de la puissance
    d'un nombre :math:`a^b = aa..a` b fois

    :param a: la valeur
    :param b: l'exposant
    :type a: int, float,...
    :type b: int, float,...
    :returns: a**b
    :rtype: int, float
```

+++

### Exemple de documentation plus riche 2/2

```python
"""" suite ....

    :Exemples:
    >>>nompow(2, 3)
    8
    >>>nompow(2., 2)
    4.0

    .. note:: c'est une version accélérée de la puissance par multiplication successives
    .. seealso:: pow
    .. warning:: a et b sont des nombres
    """
    return a**b
```

---

## Bilan de l'UE

Découvrir les bases de la programmation informatique.

* Maitriser les variables et leurs types
* Stocker des données dans une structure de liste
* Effectuer des calculs sur des données
* Organiser son code en fonctions et modules
* Importer des données/Exporter des résultats

+++

### A suivre en S2 (Informatique)

* Mieux comprendre la gestion des listes et leur efficacité
* Découvrir l'algorithmique en géneral:
  * Notions de preuves (correction, terminaison)
  * Comparaison d'algorithmes (rapidité mémoire)
  * Principe "Diviser pour régner"
* Nombreux algorithmes sur les tableaux:
  * Recherche d'éléments
  * Tri d'un tableau
  * Sélection d'éléments (k-ième plus grand)
  * ...
