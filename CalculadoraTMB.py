def calculadora_tmb():
    print("\n\t[Calculadora de TMB]\n")

    sexo = input("Digite o seu sexo (M para masculino, F para feminino): ").strip().upper()
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em cm: "))
    idade = int(input("Digite sua idade: "))

    if sexo == "M":
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)

    elif sexo == "F":
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    
    else: 
        print("insira um sexo válido!")
        return
    
    print(f"\nSua Taxa Metabólica Basal (TMB) é: {tmb:.2f} calorias/dia.")
calculadora_tmb()
input("\nPressione Enter para sair...")