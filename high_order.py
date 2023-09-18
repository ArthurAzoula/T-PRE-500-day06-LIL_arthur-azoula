# task 00

def funA(s: str, n: int):
    count = 0
    for char in s:
        if char.islower():
            count += 1
    res = True if n >= count else f'/!\ Error : contains {count} lower characters, check for {n} lower characters'
    return res

print(funA("Oui", 2))

def funB(s: str, n: int):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    res = True if n >= count else f'/!\ Error : contains {count} upper characters, check for {n} upper characters'
    return res

print(funB("Oui", 1))

def funC(s: str, n: int):
    return True if n >= len(s) else f'/!\ Error : contains {len(s)} characters, check for {n} characters'

print(funC('Oui', 3))

def funD(s: str, n:int):
    count = 0
    for char in s:
        if not char.isalpha():
            count += 1
    res = True if n >= count else f'/!\ Error : contains {count} specials characters, check for {n} specials characters'
    return res

print(funD('Oui%¹^!:', 5))

def funE(s: str, n: int):
    count = 0
    for char in s:
        if char in '0123456789':
            count += 1
    res = True if n >= count else f'/!\ Error : contains {count} lower characters, check for {n} characters'
    return res

print(funE('1Oui3', 2))

# task 01 and 02

def check_password(command, count: int, password: str) -> bool or str:
    
    return command(password, count)


print("Check password : ", check_password ( funA , 2, " MyseZaJH" ))