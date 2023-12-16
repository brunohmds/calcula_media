import tkinter as tk
from tkinter import ttk

def calcular_media(nota1, nota2, nota3):
    media = (nota1+nota2+nota3)/3
    return media

def exibir_classificacao_final(media):
    if media < 4:
        return "Reprovado por média"
    elif media >= 4 and media < 7:
        return "Prova final"
    else:
        return "Aprovado por média"
    
def cadastrar_pessoa():
    nome = nome_entry.get()
    matricula = int(matricula_entry.get())
    nota1 = float(nota1_entry.get())
    nota2 = float(nota2_entry.get())
    nota3 = float(nota3_entry.get())

    media = calcular_media(nota1,nota2,nota3)
    classificacao = exibir_classificacao_final(media)

# Exibe o resultado das variaveis digitadas nos widgets

    resultado_label.config(text=f" Nome: {nome} \n Matrícula: {matricula} \n Primeira nota: {nota1:.2f} "
                                f"\n Segunda nota: {nota2:.2f} \n Terceira nota: {nota3:.2f}")
    classificacao_label.config(text=f" A média do aluno foi: {media:.2f}. \n O resultado final foi: {classificacao}.")

# Cria a janela principal
root = tk.Tk()
root.geometry("320x350")
root.title("Calculadora de Média")
root.configure(bg="Grey")
fonte = ("Arial", 10)

# Cria os widgets
nome_label = ttk.Label(root, text="Nome:")
nome_entry = ttk.Entry(root)

matricula_label = ttk.Label(root, text="Matrícula:")
matricula_entry = ttk.Entry(root)

nota1_label = ttk.Label(root, text="Primeira nota:")
nota1_entry = ttk.Entry(root)

nota2_label = ttk.Label(root, text="Segunda nota:")
nota2_entry = ttk.Entry(root)

nota3_label = ttk.Label(root, text="Terceira nota:")
nota3_entry = ttk.Entry(root)

calcular_button = ttk.Button(root, text="Calcular média", command=cadastrar_pessoa)

resultado_label = ttk.Label(root, text="")
classificacao_label = ttk.Label(root, text="")

# Posiciona os widgets
nome_label.grid(row=0, column=0, padx=10, pady=5)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

matricula_label.grid(row=1, column=0, padx=10, pady=5)
matricula_entry.grid(row=1, column=1, padx=10, pady=5)

nota1_label.grid(row=2, column=0, padx=10, pady=5)
nota1_entry.grid(row=2, column=1, padx=10, pady=5)

nota2_label.grid(row=3, column=0, padx=10, pady=5)
nota2_entry.grid(row=3, column=1, padx=10, pady=5)

nota3_label.grid(row=4, column=0, padx=10, pady=5)
nota3_entry.grid(row=4, column=1, padx=10, pady=5)

calcular_button.grid(row=5, column=0, columnspan=2, pady=10)

resultado_label.grid(row=6, column=0, columnspan=2, pady=5)
classificacao_label.grid(row=7, column=0, columnspan=2, pady=5)

# Inicia o loop principal da interface grafica
root.mainloop()
