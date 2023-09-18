# task 01

def f ( x ) :
    return 2 * x + 1 # function that return this calcul
def g () :
    return 7
y = f (2) # y = 2 * 2 + 1 = 5
print ( y )
y = f (5) + g () # 2 * 5 + 1 = 11 + 7 = 18 (reolace the default value 5)
print ( y )

# task 02 

def bread () :
    print ( " <////////// > " )
def lettuce () :
    print ( " ~~~~~~~~~~~~ " )
def tomato () :
    print ( " O O O O O O " )
def ham () :
    print ( " ============ " )

for i in range(42):
    bread(), lettuce(), tomato(), ham()

# task 03 

def displayBurgers(nb):
    if nb > 0:
        for i in range(nb):
            bread(), lettuce(), tomato(), ham()
    else:
        print("I can't do this")

displayBurgers(10)

# task 04

def commande():
    sandwich = input("Votre commande : ")
    if sandwich == 'double vegetables and no ham':
        bread() , lettuce(), tomato(), bread()
    else:
        bread(), lettuce(), tomato(), ham(), bread()

commande()