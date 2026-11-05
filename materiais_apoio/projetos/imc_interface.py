
import tkinter as tk
from tkinter import ttk, messagebox


def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")

    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


def calcular():
    try:
        peso = float(campo_peso.get().replace(",", "."))
        altura = float(campo_altura.get().replace(",", "."))

        if peso <= 0:
            raise ValueError("O peso deve ser maior que zero.")

        if altura <= 0:
            raise ValueError("A altura deve ser maior que zero.")

        imc = calcular_imc(peso, altura)
        categoria = classificar_imc(imc)

        imc_var.set(f"IMC: {imc:.2f}")
        classificacao_var.set(
            f"Classificação: {categoria}"
        )

    except ValueError as erro:
        messagebox.showerror(
            "Dados inválidos",
            f"Erro: {erro}"
        )

        imc_var.set("")
        classificacao_var.set("")


def limpar():
    campo_peso.delete(0, tk.END)
    campo_altura.delete(0, tk.END)

    imc_var.set("")
    classificacao_var.set("")

    campo_peso.focus()


# Janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("420x380")
janela.resizable(False, False)

# Estilo
estilo = ttk.Style()
estilo.theme_use("clam")

# Frame principal
frame = ttk.Frame(janela, padding=20)
frame.pack(fill="both", expand=True)

frame.columnconfigure(0, weight=1)

# Título
lbl_titulo = ttk.Label(
    frame,
    text="Calculadora de IMC",
    font=("Arial", 16, "bold"),
    anchor="center"
)
lbl_titulo.grid(
    row=0,
    column=0,
    sticky="ew",
    pady=(0, 15)
)

# Campo Peso
lbl_peso = ttk.Label(frame, text="Peso (kg):")
lbl_peso.grid(row=1, column=0, sticky="w")

campo_peso = ttk.Entry(frame, width=30)
campo_peso.grid(
    row=2,
    column=0,
    sticky="ew",
    pady=(0, 10)
)

# Campo Altura
lbl_altura = ttk.Label(frame, text="Altura (m):")
lbl_altura.grid(row=3, column=0, sticky="w")

campo_altura = ttk.Entry(frame, width=30)
campo_altura.grid(
    row=4,
    column=0,
    sticky="ew",
    pady=(0, 10)
)

# Botão Calcular
btn_calcular = ttk.Button(
    frame,
    text="Calcular IMC",
    command=calcular
)
btn_calcular.grid(
    row=5,
    column=0,
    sticky="ew",
    pady=(5, 8)
)

# Botão Limpar
btn_limpar = ttk.Button(
    frame,
    text="Limpar",
    command=limpar
)
btn_limpar.grid(
    row=6,
    column=0,
    sticky="ew",
    pady=(0, 10)
)

# Variáveis de resultado
imc_var = tk.StringVar()
classificacao_var = tk.StringVar()

# Área de resultado centralizada
resultado_frame = ttk.Frame(frame)

resultado_frame.grid(
    row=7,
    column=0,
    sticky="ew",
    pady=(15, 0)
)

resultado_frame.columnconfigure(0, weight=1)

# Resultado IMC
imc_label = tk.Label(
    resultado_frame,
    textvariable=imc_var,
    foreground="#0b3d91",
    font=("Arial", 12, "bold"),
    anchor="left",
    justify="center"
)
imc_label.grid(
    row=0,
    column=0,
    sticky="ew"
)

# Classificação
classificacao_label = tk.Label(
    resultado_frame,
    textvariable=classificacao_var,
    foreground="#0b3d91",
    font=("Arial", 12, "bold"),
    anchor="center",
    justify="center"
)
classificacao_label.grid(
    row=1,
    column=0,
    sticky="ew"
)

# Foco inicial
campo_peso.focus()

# Executar aplicação
janela.mainloop()
