def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso", "Grau 0"
    elif imc < 25:
        return "Peso normal", "Grau 0"
    
    elif imc < 30:
        return "Sobrepeso", "Grau I"
    
    elif imc < 35:
        return "Obesidade Grau I", "Grau I"
    
    elif imc < 40:
        return "Obesidade Grau II", "Grau II"
    
    else:
        return "Obesidade Grau III", "Grau III"
     
print("Calculadora de IMC")
try:

    altura = float(input("Digite sua altura (ex: 1.75): ").replace( "," , "."))
    peso = float(input("Digite seu peso (ex: 70.5): ").replace("," ,".")) 

    imc = calcular_imc(peso, altura)
    classificação, grau = classificar_imc(imc)

    print(f"\n Seu IMC é: {imc: .2f}") 
    print(f" Classificação: {classificação}")
    print(f"Grau de obesidade: {grau}") 

except ValueError:
    print("Erro: Digite valores válidos para altura e peso.")