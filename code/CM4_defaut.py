
import datetime

année = int(input("Année ? "))

# si l'année est divisible par 4 et non divisible par 100, ou
# si l'année est divisible par 400.

C4 = année % 4 == 0
C100 = année % 100 == 0
C400 = année % 400 == 0

bissextile = (C4 and not C100) or C400

now = datetime.datetime.now()
print(now.year)


