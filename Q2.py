palavra = "TestePalAvrA"
contador_de_a= 0
for letra in palavra:
    if letra == 'A' or letra =='a':
        contador_de_a += 1
if contador_de_a>0:
    print(f"A letra A aparece {contador_de_a} na palavra.")
else:
    print("Não contém 'A' na palavra.")
        