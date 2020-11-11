from datetime import datetime

def bissextile(année):
    C4 = année % 4 == 0
    C100 = année % 100 == 0
    C400 = année % 400 == 0
    return (C4 and not C100) or C400

def bissextile_def(année=2020):
    C4 = année % 4 == 0
    C100 = année % 100 == 0
    C400 = année % 400 == 0
    return (C4 and not C100) or C400

def bissextile_def2(année=datetime.now().year):
    C4 = année % 4 == 0
    C100 = année % 100 == 0
    C400 = année % 400 == 0
    return (C4 and not C100) or C400

def bissextile_def3(année=None):
    if année is None:
        année = datetime.now().year
    C4 = année % 4 == 0
    C100 = année % 100 == 0
    C400 = année % 400 == 0
    return (C4 and not C100) or C400


année = 1900
print(bissextile(année))
print(bissextile_def(année))
print(bissextile_def())
print(bissextile_def2(année))
print(bissextile_def2())
print(bissextile_def3(année))
print(bissextile_def3())


