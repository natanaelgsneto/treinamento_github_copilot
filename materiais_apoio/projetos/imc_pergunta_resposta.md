# Pergunta
Como programador Python SR, implemente uma interface visual básica com Tkinter para capturar informações do IMC e apresentar a classificação?

# Resposta

A solução foi criar uma interface simples com Tkinter, onde o usuário digita o peso em quilogramas e a altura em metros. Ao clicar em "Calcular IMC", o programa valida os dados, calcula o índice e mostra a classificação correspondente.

## Estrutura da solução

- `calcular_imc(peso, altura)`: calcula o IMC com a fórmula:

  \[
  IMC = \frac{peso}{altura^2}
  \]

- `classificar_imc(imc)`: retorna a faixa de classificação:
  - Abaixo do peso
  - Peso normal
  - Sobrepeso
  - Obesidade

- `calcular()`: lê os campos da interface, valida se os valores são válidos e atualiza o resultado na tela.

- `limpar()`: limpa os campos e o resultado.

## Código da interface

```python
import tkinter as tk
from tkinter import ttk, messagebox


def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


def calcular():
    try:
        peso = float(campo_peso.get().replace(",", "."))
        altura = float(campo_altura.get().replace(",", "."))

        if peso <= 0:
            raise ValueError("O peso deve ser maior que zero.")

        imc = calcular_imc(peso, altura)
        categoria = classificar_imc(imc)

        resultado_var.set(f"IMC: {imc:.2f}\nClassificação: {categoria}")
    except ValueError as erro:
        messagebox.showerror("Dados inválidos", f"Erro: {erro}")
        resultado_var.set("Informe peso e altura válidos.")


def limpar():
    campo_peso.delete(0, tk.END)
    campo_altura.delete(0, tk.END)
    resultado_var.set("")
    campo_peso.focus()


janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("420x320")
janela.resizable(False, False)

estilo = ttk.Style()
estilo.theme_use("clam")

frame = ttk.Frame(janela, padding=20)
frame.pack(fill="both", expand=True)

lbl_titulo = ttk.Label(frame, text="Calculadora de IMC", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=(0, 15))

lbl_peso = ttk.Label(frame, text="Peso (kg):")
lbl_peso.pack(anchor="w")
campo_peso = ttk.Entry(frame, width=30)
campo_peso.pack(fill="x", pady=(0, 10))

lbl_altura = ttk.Label(frame, text="Altura (m):")
lbl_altura.pack(anchor="w")
campo_altura = ttk.Entry(frame, width=30)
campo_altura.pack(fill="x", pady=(0, 10))

btn_calcular = ttk.Button(frame, text="Calcular IMC", command=calcular)
btn_calcular.pack(fill="x", pady=(5, 8))

btn_limpar = ttk.Button(frame, text="Limpar", command=limpar)
btn_limpar.pack(fill="x", pady=(0, 10))

resultado_var = tk.StringVar()
resultado_label = ttk.Label(
    frame,
    textvariable=resultado_var,
    foreground="#0b3d91",
    font=("Arial", 11, "bold"),
    wraplength=300,
    justify="center",
)
resultado_label.pack(fill="x", pady=(5, 0))

campo_peso.focus()
janela.mainloop()
```

## O que essa interface faz

- captura peso e altura
- valida entradas do usuário
- calcula o IMC
- classifica o resultado
- exibe a resposta na interface gráfica

## Relevância do IMC para a saúde

O IMC é útil como indicador simples de peso em relação à altura e ajuda a identificar possíveis riscos para a saúde, como:

- doenças cardiovasculares
- diabetes tipo 2
- pressão alta
- problemas articulares
- excesso ou falta de peso que pode afetar o bem-estar

Importante: o IMC é uma ferramenta de triagem, não um diagnóstico definitivo. Ele deve ser interpretado junto com outros fatores, como idade, sexo, atividade física, massa muscular e avaliação profissional.

## Conclusão

Essa interface em Tkinter é uma versão simples, funcional e didática de um programa de cálculo de IMC. Ela combina lógica em Python com interação visual, o que facilita a utilização por pessoas sem conhecimento de programação.
