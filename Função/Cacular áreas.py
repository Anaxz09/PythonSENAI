def areas():
    print("Área do circulo, digite 1 ")
    print("Área do retangulo, digite 2 ")
    print("Área do quadrado, digite 3 ")
    print("Área do triângulo equilátero, digite 4 ")
    print("Área do hexágono, digite 5 ")
   
def perimetros():
    print("Perímetro do circulo, digite 6 ")
    print("Perímetro do retângulo, digite 7 ")
    print("Perímetro do quadrado, digite 8 ")
    print("Perímetro do triângulo equílatero, digite 9 ")
    print("Perímetro do hexágono, digite 10 ")
     

def circulo(raio):
    area= 3.14*raio**2
    return area
   
def retangulo(base,altura):
    area=base*altura
    return area
   
def quadrado(lado):
    area=lado*lado
    return area

def triangulo_equiatero (lado):
    area= lado**2*1.7/4
    return area

def hexagono (lado):
    area= 6*lado**2*1.7/4
    return area

def circulo2 (raio):
    perimetro= 2*1.7*raio
    return perimetro
   
def retangulo2 (lado):
    perimetro= lado+lado+lado+lado
    return perimetro
   
def quadrado2 (lado):
    perimetro=lado+lado+lado+lado
    return perimetro

def triangulo_equilatero2 (lado):
    perimetro= lado+lado+lado
    return perimetro

def hexagono2 (lado):
    perimetro= lado+lado+lado+lado+lado+lado
    return area

a_p=int(input("Você quer área ou perímetro? Se for área digite 1, se for perímetro digite 2 "))

if a_p == 1:
    print("áreas")

    areas()
    forma=int(input("Digite qual forma você deseja: "))
    if forma == 1:
        raio=int(input("Digite o raio do circulo: "))
        print("A área do circulo é", circulo(raio))
    elif forma==2:
         base=int(input("Digite a base do retângulo: "))
         altura=int(input("Digite a altura do retângulo: "))
         print("A área do retângulo é", retangulo(base,altura))
    elif forma==3:
        lado=int(input("Digite o lado do quadrado: "))
        print("A área do quadrado é", quadrado(lado))
    elif forma==4:
        lado=int(input("Digite a base do triângulo "))
        altura=int(input("Digite a altura do triângulo "))
        print("A área do triângulo é:", triangulo_equilatero(lado))
    elif forma==5:
        lado=int(input("Digite o lado do triângulo "))
        print("A área do hexágono é", hexagono(lado))
    else:
        print("Opção não identificada, escolha somente as opções exibidas")
else:
    a_p == 2
    print("Perímetro")
   
    perimetros()
    forma=int(input("Digite qual forma você quer? "))
    if forma==6:
        raio=int(input("Digite o raio do circulo "))
        print("O perímetro do circulo é", circulo2(raio))
    elif forma==7:
        lado=int(input("Digite o lado do retângulo "))
        print("O perímetro do retângulo é", retangulo2(lado))
    elif forma==8:
        lado=int(input("Digite o lado do quadrado "))
        print("O perímetro do quadrado é", quadrado2(lado))
    elif forma==9:
        lado=int(input("Digite o lado do triângulo equilátero "))
        print("O perímetro do triângulo equilâtero é", triangulo_equilatero2(lado))
    elif forma==10:
        lado=int(input("Digite o lado do hexágono "))
        print("O perímetro do hexágono é", hexagono2(lado))
