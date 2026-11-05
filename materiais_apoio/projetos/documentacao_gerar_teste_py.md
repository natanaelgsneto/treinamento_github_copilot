# Documentação para gerar o arquivo `teste.py`

## 1. Objetivo

O arquivo `teste.py` deve calcular o Índice de Massa Corporal (IMC) com base no peso e na altura informados pelo usuário, classificar o resultado e exibir a mensagem final na tela.

O cálculo do IMC segue a fórmula:

`IMC = peso / (altura ** 2)`

Onde:
- peso em quilogramas (kg)
- altura em metros (m)

---

## 2. Requisitos do programa

O script precisa:

1. Ler o peso digitado pelo usuário.
2. Ler a altura digitada pelo usuário.
3. Validar se a altura é maior que zero.
4. Calcular o IMC.
5. Classificar o valor em categorias.
6. Exibir o resultado com duas casas decimais.
7. Tratar erros de entrada com mensagens claras.

---

## 3. Estrutura lógica do programa

### 3.1 Função para calcular o IMC

A função deve receber:
- `peso`
- `altura`

E retornar:
- o valor do IMC calculado

Pseudoestruturas:

```python
def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return peso / (altura ** 2)
```

### 3.2 Função para classificar o IMC

A função deve receber:
- `imc`

E retornar:
- uma string com a categoria

Faixas sugeridas:

- menor que 18.5 → "Abaixo do peso"
- entre 18.5 e 24.9 → "Peso normal"
- entre 25 e 29.9 → "Sobrepeso"
- 30 ou mais → "Obesidade"

Pseudoestrutura:

```python
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
```

### 3.3 Função principal

A função `main()` deve:

- solicitar o peso
- solicitar a altura
- converter os valores para `float`
- chamar `calcular_imc()`
- chamar `classificar_imc()`
- imprimir o resultado

Pseudoestrutura:

```python
def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError as e:
        print(f"Erro: {e}")
```

---

## 4. Bloco de execução

Para garantir que o programa execute apenas quando o arquivo for rodado diretamente, usamos:

```python
if __name__ == "__main__":
    main()
```

Isso é importante porque permite reutilizar funções em outros arquivos Python sem executar automaticamente o código principal.

---

## 5. Código final do `teste.py`

```python
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
    Função principal que solicita ao usuário o peso e altura,
    calcula o IMC e exibe a classificação.
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
```

---

## 6. Exemplo de execução

Entrada:

```text
Digite seu peso em kg: 70
Digite sua altura em metros: 1.75
```

Saída esperada:

```text
Seu IMC é: 22.86
Classificação: Peso normal
```

---

## 7. Considerações importantes

- A altura deve ser maior que zero para evitar divisão por zero.
- A conversão com `float()` permite aceitar números decimais.
- O IMC é uma referência simples para avaliação do peso em relação à altura, mas não substitui avaliação médica.
- O programa pode ser expandido no futuro para incluir:
  - validação de peso também maior que zero;
  - interface gráfica com Tkinter;
  - armazenamento do histórico de resultados;
  - cálculo para várias pessoas;

---

## 8. Dicas para desenvolvimento

- Mantenha as funções pequenas e com responsabilidade única.
- Use docstrings para documentar o propósito de cada função.
- Faça validações antes de realizar operações matemáticas.
- Teste com valores positivos e negativos para validar o comportamento.

---

## 9. Conclusão

Para gerar o arquivo `teste.py`, basta criar uma estrutura com:

- função de cálculo do IMC;
- função de classificação;
- função principal do programa;
- bloco `if __name__ == "__main__":`;
- tratamento de exceções para entradas inválidas.

Esse conjunto é suficiente para construir um programa simples, funcional e fácil de entender.
