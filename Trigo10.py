from fractions import Fraction
import math
from math import cos,sin,tan,atan,asin,sqrt
import sympy
import sympy as sp
from sympy import pi,acos
print("1. Determiner les coordonnes exactes d'un point trigonometrique qui a fait plus d'un tour OU  point exacte")
print("2. Determiner si un point est un point trigonometrique")
print("3. Trouver la valeur exacte de l'abscisse ou l'ordonnee")
print("4. Tables de valeur et infos sur fonction cos ou sin")
choix = input("Choix: ")

if choix == "1":
    n = float(input("Nominateur sans le signe Pi: "))
    d = float(input("Denominateur: "))
    if n < 0: 
        n2 = abs(n)
        div = 2 * d
        res = n2 % div 
        res1 = n2 // div
        res11 = int(res1)
        if (res/d) == (1/4):
            print("point: 7pi/4")
            print("Donc dans le quatrieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (sqrt(2)/2, -sqrt(2)/2)" )
        elif (res/d) == (1/6):
            print("point: 11pi/6")
            print("Donc dans le quatrieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (sqrt(3)/2, -1/2)" )
        elif (res/d) == (1/3):
            print("point: 5pi/3")
            print("Donc dans le quatrieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (1/2, -sqrt(3)/2 )" )
        elif (res/d) == (1/2):
            print("point: 5pi/3")
            print("Donc entre le troisieme et quatrieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (0, -1 )" )
        elif (res/d) == (2/3):
            print("point: 4pi/3")
            print("Donc dans le troisieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (-1/2, -sqrt(3)/2 )" )
        elif (res/d) == (3/4):
            print("point: 5pi/4")
            print("Donc dans le troisieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (-sqrt(2)/2, -sqrt(2)/2 )" )
        elif (res/d) == (5/6):
            print("point: 7pi/6")
            print("Donc dans le troisieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (-sqrt(3)/2, -1/2 )" )
        elif (res/d) == (7/6):
            print("point: 5pi/6")
            print("Donc dans le deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (-sqrt(3)/2, 1/2)" )
        elif (res/d) == (5/4):
            print("point: 3pi/4")
            print("Donc dans le deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (-sqrt(2)/2, sqrt(2)/2)" )
        elif (res/d) == (4/3):
            print("point: 2pi/3")
            print("Donc dans le deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (-1/2, sqrt(3)/2)" )
        elif (res/d) == (3/2):
            print("point: pi/2")
            print("Donc entre le premier et deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (0, 1)" )
        elif (res/d) == (5/3):
            print("point: pi/3")
            print("Donc dans le premier quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (1/2, sqrt(3)/2)" )
        elif (res/d) == (7/4):
            print("point: pi/4")
            print("Donc dans le premier quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (sqrt(2)/2, sqrt(2)/2)" )
        elif (res/d) == (11/6):
            print("point: pi/6")
            print("Donc dans le premier quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (sqrt(3)/2, 1/2 )" )
        

    else:
        div = 2 * d
        res = n % div
        res1 = n // div
        resint = int(res)
        res11 = int(res1)
        dint = int(d)
        if (res/d) == (1/4):
            print("point: pi/4")
            print("Donc dans le premier")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (sqrt(2)/2, sqrt(2)/2)" )
        elif (res/d) == (1/6):
            print("point: pi/6")
            print("Donc dans le premier quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (sqrt(3)/2, 1/2 )" )
        elif (res/d) == (1/3):
            print("point: pi/3")
            print("Donc dans le premier quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (1/2, sqrt(3)/2)" )
        elif (res/d) == (1/2):
            print("point: pi/2")
            print("Donc entre le premier et deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (0, 1)" )
        elif (res/d) == (2/3):
            print("point: 2pi/3")
            print("Donc dans le deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (-1/2, sqrt(3)/2)" )
        elif (res/d) == (3/4):
            print("point: 3pi/4")
            print("Donc dans le deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (-sqrt(2)/2, sqrt(2)/2)" )
        elif (res/d) == (5/6):
            print("point: 5pi/6")
            print("Donc dans le deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (-sqrt(3)/2, 1/2)" )
        elif (res/d) == (7/6):
            print("point: 7pi/6")
            print("Donc dans le troisieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (-sqrt(3)/2, -1/2 )" )
        elif (res/d) == (5/4):
            print("point: 5pi/4")
            print("Donc dans le troisieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (-sqrt(2)/2, -sqrt(2)/2 )" )
        elif (res/d) == (4/3):
            print("point: 4pi/3")
            print("Donc dans le troisieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (-1/2, -sqrt(3)/2 )" )
        elif (res/d) == (3/2):
            print("point: 2pi/3")
            print("Donc dans le deuxieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (-1/2, sqrt(3)/2)" )
        elif (res/d) == (5/3):
            print("point: 5pi/3")
            print("Donc entre le troisieme et quatrieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (0, -1 )" )
        elif (res/d) == (7/4):
            print("point: 7pi/4")
            print("Donc dans le quatrieme quadrant")
            print("Il a fait", res11 , " tours dans le sens anti horaire" )
            print("Les coordonnees sont (sqrt(2)/2, -sqrt(2)/2)" )
        elif (res/d) == (11/6):
            print("point: 11pi/6")
            print("Donc dans le quatrieme quadrant")
            print("Il a fait", res11 , " tours dans le sens horaire" )
            print("Les coordonnees sont (sqrt(3)/2, -1/2)" )

if choix == "2":
    x = float(Fraction(input("Quelle est la valeur de x: ")))
    y = float(Fraction(input("Quelle est la valeur de y: ")))

    tota = x**2 + y**2

    if tota == 1:
        print("Ce point fait partit du cercle trigonometrique!")
    else:
        print("Ce point ne fait partit du cercle trigonometrique")
if choix == "3":
    choixeta3 = input("Abscisse (x) ou ordonnee (y): ")
    if choixeta3 == "x":
        y = float(Fraction(input("Que vaut y: ")))
        y2 = Fraction(y)
        x = Fraction(1-y**2)
        x2 = sympy.simplify(sympy.sqrt(x)) 
        x3 = -(x2)
        print("x =", x2, " et x =",x3)
    else: 
        xx = float(Fraction(input("Que vaut le x: ")))
        xx2 = Fraction(xx)
        xx3 = 1-xx2**2
        yy = sympy.simplify(sympy.sqrt(xx3))
        yy2 = -(yy)
        print("y =",yy, "y =",yy2)
if choix == "4":
    cosin = input("La fonction est t'elle sinus(1) ou cosinus(2): ")
    if cosin == "2":
        bpi = input("Y a t'il un pi dans le b (o/n) : ")
        a = Fraction(input("a = "))
        b = Fraction(input("b = "))
        h = Fraction(input("h = "))
        k = Fraction(input("k = "))
        if a > 0:
            if bpi == "o":
                nv = abs(b)
                p = Fraction(2/nv)
                quartp = Fraction(p/4)
                premierx = h
                premiery = k + a
                print("     Tables de valeurs       ")
                print("_"*30)
                print(f"{premierx:<15}{premiery:<15}")
                deuxiemex = Fraction(h + quartp)
                deuxiemey = k
                print(f"{deuxiemex: <15}{deuxiemey:<15}")
                troisiemex = Fraction(h + 2*quartp)
                troisiemey = k - a
                print(f"{troisiemex:<15}{troisiemey:<15}")
                quatriemex = Fraction(h + 3*quartp)
                quatriemey = k
                print(f"{quatriemex:<15}{quatriemex:<15}")
                cinquiemex = Fraction(h + 4*quartp)
                cinquiemey = k + a
                print(f"{cinquiemex:<15}{cinquiemey:<15}")
                sixiemex = Fraction(h + 5*quartp)
                sixiemey = k
                print(f"{sixiemex:<15}{sixiemey:<15}")
                setiemex = Fraction(h + 6*quartp)
                setiemey = k - a
                print(f"{setiemex:<15}{setiemey:<15}")
                huitiemex = Fraction(h + 7*quartp)
                huitiemey = k
                print(f"{huitiemex:<15}{huitiemey:<15}")
                neuviemex = Fraction(h + 8*quartp)
                neuviemey = k + a
                print(f"{neuviemex:<15}{neuviemey:<15}")
                print("_"*30)

                #LES ZEROS
                
                zeroc1 = 0 - k
                zeroc2 = Fraction(zeroc1/a)
                if zeroc2 == (1/2):
                    bap = abs(b)
                    periode = 2/bap
                    z1 = 1/3
                    zeroc1 = Fraction(z1/bap)
                    zeroc2 = Fraction(zeroc1 + h).limit_denominator()
                    zeroc3 = Fraction((-1/3)/bap)
                    zeroc4 = Fraction(zeroc3 + h).limit_denominator() 
                    print(f"x ∈ R | x = {zeroc2} + {periode}n et x = {zeroc4} + {periode}n , n ∈ Z")
                if zeroc2 == (-1/2):
                    bap = abs(b)
                    periode = 2/bap
                    z1 = (2/3)
                    zeroc1 = Fraction(z1/bap).limit_denominator()
                    zeroc2 = Fraction(zeroc1 + h).limit_denominator()
                    z2 = 4/3
                    zeroc3 = Fraction(z2/bap).limit_denominator()
                    zeroc4 = Fraction(zeroc3 + h).limit_denominator()
                    print(f"x ∈ R | x = {zeroc2} + {periode}n et x = {zeroc4} + {periode}n , n ∈ Z")
                else: 
                    bap = abs(b)
                    periode = 2/bap
                    zero1 = 0 - k
                    zero2 = zero1/a
                    zero3 = acos(zero2)
                    z2 = zero3/bap
                    zero4 = z2 + h
                    zero21 = round(sp.Rational(-(acos(zero2))),4)
                    z3 = zero21/bap
                    zero22 = z3 + h
                    print(f"x ∈ R | x = {zero4} + {periode}n et x = {zero22} + {periode}n , n ∈ Z")



            if bpi == "n":
                nv = abs(b)
                hpi = input("Est-ce-que le h a un π (o/n) : ")
                if hpi == "o":
                    p = Fraction(2/nv)
                    quartp = Fraction(p/4)
                    premierx = h
                    premiery = k + a
                    print("     Tables de valeurs       ")
                    print("_"*30)
                    print(f"{str(premierx) + "π" :<15}{premiery:<15}")
                    deuxiemex = Fraction(h + quartp)
                    deuxiemey = k
                    print(f"{str(deuxiemex) + "π": <15}{deuxiemey:<15}")
                    troisiemex = Fraction(h + 2*quartp)
                    troisiemey = k - a
                    print(f"{str(troisiemex) + "π":<15}{troisiemey:<15}")
                    quatriemex = Fraction(h + 3*quartp)
                    quatriemey = k
                    print(f"{str(quatriemex) + "π":<15}{quatriemey:<15}")
                    cinquiemex = Fraction(h + 4*quartp)
                    cinquiemey = k + a
                    print(f"{str(cinquiemex) + "π":<15}{cinquiemey:<15}")
                    sixiemex = Fraction(h + 5*quartp)
                    sixiemey = k
                    print(f"{str(sixiemex) + "π":<15}{sixiemey:<15}")
                    setiemex = Fraction(h + 6*quartp)
                    setiemey = k - a
                    print(f"{str(setiemex) + "π":<15}{setiemey:<15}")
                    huitiemex = Fraction(h + 7*quartp)
                    huitiemey = k
                    print(f"{str(huitiemex) + "π":<15}{huitiemey:<15}")
                    neuviemex = Fraction(h + 8*quartp)
                    neuviemey = k + a
                    print(f"{str(neuviemex) + "π":<15}{neuviemey:<15}")
                    print("_"*30)
                    print("Les zeros:")
                    zero1 = 0 - k
                    zero2 = Fraction(zero1/a).limit_denominator()
                    periode = Fraction(2/nv)
                    if zero2 == (1/2):
                        zero11 = Fraction((1/3)/nv).limit_denominator()
                        zero12 = Fraction(zero11 - h).limit_denominator()
                        zero13 = Fraction((-1/3)/nv).limit_denominator()
                        zero14 = Fraction(zero13 - h).limit_denominator()
                        print(f"x ∈ R | x = {zero12} + {periode}n et x = {zero22} + {periode}n , n ∈ Z")


                else: 
                    p = Fraction(2/nv)
                    quartp = Fraction(p/4)
                    quartpapr = float(pi * quartp)
                    premierx = h
                    premiery = k + a
                    premierxx = round(premierx, 4)
                    print("     Tables de valeurs       ")
                    print("_"*30)
                    print(f"{premierxx:<15}{premiery:<15}")
                    deuxiemex = float(h + quartpapr)
                    deuxiemexx = round(deuxiemex, 4)
                    deuxiemey = k
                    print(f"{deuxiemexx: <15}{deuxiemey:<15}")
                    troisiemex = float(h + 2*quartpapr)
                    troisiemey = k - a
                    troisiemexx = round(troisiemex, 4)
                    print(f"{troisiemexx:<15}{troisiemey:<15}")
                    quatriemex = float(h + 3*quartpapr)
                    quatriemey = k
                    quatriemexx = round(quatriemex, 4)
                    print(f"{quatriemexx:<15}{quatriemey:<15}")
                    cinquiemex = float(h + 4*quartpapr)
                    cinquiemey = k + a
                    cinquiemexx = round(cinquiemex, 4)
                    print(f"{cinquiemexx:<15}{cinquiemey:<15}")
                    sixiemex = float(h + 5*quartpapr)
                    sixiemey = k
                    sixiemexx = round(sixiemex, 4)
                    print(f"{sixiemexx:<15}{sixiemey:<15}")
                    setiemex = float(h + 6*quartpapr)
                    setiemey = k - a
                    setiemexx = round(setiemex, 4)
                    print(f"{setiemexx:<15}{setiemey:<15}")
                    huitiemex = float(h + 7*quartpapr)
                    huitiemey = k
                    hutiemexx = round(huitiemex, 4)
                    print(f"{hutiemexx:<15}{huitiemey:<15}")
                    neuviemex = float(h + 8*quartpapr)
                    neuviemey = k + a
                    neuviemexx = round(neuviemex, 4)
                    print(f"{neuviemexx:<15}{neuviemey:<15}")
                    print("_"*30)
        if a < 0:
            if bpi == "o":
                nv = abs(b)
                na = abs(a)
                p = Fraction(2/nv)
                quartp = Fraction(p/4)
                print("     Tables de valeurs       ")
                print("_"*30)
                premierx = h
                premiery = k - na
                print(f"{premierx:<15}{premiery:<15}")
                deuxiemex = Fraction(h + quartp)
                deuxiemey = k
                print(f"{deuxiemex:<15}{deuxiemey:<15}")
                troisiemex = Fraction(h + 2*quartp)
                troisiemey = k + na
                print(f"{troisiemex:<15}{troisiemey:<15}")
                quatriemex = Fraction(h + 3*quartp)
                quatriemey = k
                print(f"{quatriemex:<15}{quatriemey:<15}")
                cinquiemex = Fraction(h + 4*quartp)
                cinquiemey = k - na
                print(f"{cinquiemex:<15}{cinquiemey:<15}")
                sixiemex = Fraction(h + 5*quartp)
                sixiemey = k 
                print(f"{sixiemex:<15}{sixiemey:<15}")
                setiemex = Fraction(h + 6*quartp)
                setiemey = k + na
                print(f"{setiemex:<15}{setiemey:<15}")
                huitiemex = Fraction(h + 7*quartp)
                huitiemey = k
                print(f"{huitiemex:<15}{huitiemey:<15}")
                neuviemex = Fraction(h + 8*quartp)
                neuviemey = k - na
                print(f"{neuviemex:<15}{neuviemey:<15}")
            if bpi == "n":
                hpi = input("Est-ce-que le h a un pi (o/n) : ")
                if hpi == "o":
                    nv = abs(b)
                    na = abs(a)
                    p = Fraction(2/b)
                    quartp = Fraction (p/4)
                    premierx = h
                    premiery = k - na
                    print("     Tables de valeurs       ")
                    print("_"*30)
                    print(f"{str(premierx) + "pi":<15}{premiery:<15}")
                    deuxiemex = Fraction(h + quartp)
                    deuxiemey = k
                    print(f"{str(deuxiemex) + "pi":<15}{deuxiemey:<15}")
                    troisiemex = Fraction(h + 2*quartp)
                    troisiemey = k + na
                    print(f"{str(troisiemex) + "pi":<15}{troisiemey:<15}")
                    quatriemex = Fraction(h + 3*quartp)
                    quatriemey = k
                    print(f"{str(quatriemex) + "pi":<15}{quatriemey:<15}")
                    cinquiemex = Fraction(h + 4*quartp)
                    cinquiemey = k - na
                    print(f"{str(cinquiemex) + "pi":<15}{cinquiemey:<15}")
                    sixiemex = Fraction(h + 5*quartp)
                    sixiemey = k
                    print(f"{str(sixiemex) + "pi":<15}{sixiemey:<15}")
                    setiemex = Fraction(h + 6*quartp)
                    setiemey = k + na
                    print(f"{str(setiemex) + "pi":<15}{setiemey:<15}")
                    huitiemex = Fraction(h + 7*quartp)
                    huitiemey = k + na
                    print(f"{str(huitiemex) + "pi":<15}{huitiemey:<15}")
                    neuviemex = Fraction(h + 8*quartp)
                    neuviemey = k - na
                    print(f"{str(neuviemex) + "pi":<15}{neuviemey:<15}")
                    print("_"*30)
                else: 
                    na = abs(a)
                    nv = abs(b)
                    p = float((2*pi)/b)
                    quartp = float(p/4)
                    premierx = h
                    premiery = k - na
                    print("     Tables de valeurs       ")
                    print("_"*30)
                    print(f"{str(premierx) + "pi":<15}{premiery:<15}")
                    deuxiemex = round((h + quartp),4)
                    deuxiemey = k
                    print(f"{deuxiemex:<15}{deuxiemey:<15}")
                    troisiemex = round((h + 2*quartp), 4)
                    troisiemey = k + na
                    print(f"{troisiemex:<15}{troisiemey:<15}")
                    quatriemex = round((h + 3*quartp), 4)
                    quatriemey = k 
                    print(f"{quatriemex:<15}{quatriemey:<15}")
                    cinquiemex = round((h + 4*quartp), 4)
                    cinquiemey = k - na
                    print(f"{cinquiemex:<15}{cinquiemey:<15}")
                    sixiemex = round((h + 4*quartp), 4)
                    sixiemey = k
                    print(f"{sixiemex:<15}{sixiemey:<15}")
                    setiemex = round((h + 6*quartp), 4)
                    setiemey = k + na
                    print(f"{setiemex:<15}{setiemey:<15}")
                    huitiemex = round((h + 7*quartp), 4)
                    huitiemey = k
                    print(f"{huitiemex:<15}{huitiemey:<15}")


                        


