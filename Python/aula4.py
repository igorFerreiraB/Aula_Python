def titulo(txt):
    tam = len(txt) + 4
    print("-" * tam)
    print(f"  {txt}")
    print("-" * tam)

def area(a, b):
    a = float(input ("LARGURA (m): "))
    b = float(input ("COMPRIMENTO (m): "))

    total = a * b

    print (f"AREA DO TERRENO: {a} {b} = {total}m²")
    

titulo("↓↓↓ CALCULO DO TERRENO ↓↓↓")
area(a=0, b=0)