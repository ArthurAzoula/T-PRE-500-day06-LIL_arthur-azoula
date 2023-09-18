# task 00

def funA(s: str, n: int):
    count = 0
    for char in s:
        if char.islower():
            count += 1
    return n == count

print(funA("Oui", 2))

def funB(s: str, n: int):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return n == count

print(funB("Oui", 1))

def funC(s: str, n: int):
    return len(s) == n

print(funC('Oui', 3))

def funD(s: str, n:int):
    count = 0
    for char in s:
        if not char.isalpha():
            count += 1
    return count == n

print(funD('Oui%¹^!:', 5))

def funE(s: str, n: int):
    count = 0
    for char in s:
        if char in '0123456789':
            count += 1
    return count == n

print(funE('1Oui3', 2))

# task 01

def check_password(command, count: int, password: str) -> bool:
    
    return command(password, count)


print("Check password : ", check_password ( funA , 4 , " MyseZaJH " ) and check_password ( funD, 2, 'Mypass%¨'))