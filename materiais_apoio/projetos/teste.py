def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.

    Parâmetros:
    peso (float): Peso em quilogramas.
    altura (float): Altura em metros.

    Retorna:
    float: O valor do IMC calculado.
    """
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC em categorias de acordo com os valores padrão.

    Parâmetros:
    imc (float): O valor do IMC a ser classificado.

    Retorna:
    str: A categoria correspondente ao IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    """
    Função principal que solicita ao usuário o peso e altura, calcula o IMC e exibe a classificação.
    """
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()