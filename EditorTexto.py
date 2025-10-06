import tkinter as tk
from tkinter import filedialog, messagebox

def novo_arquivo():
    texto.delete(1.0, tk.END)

def abrir_arquivo():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if caminho_arquivo:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, conteudo)

def salvar_arquivo():
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
    if caminho_arquivo:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            conteudo = texto.get(1.0, tk.END)
            arquivo.write(conteudo.strip())
        messagebox.showinfo("Salvar", "Arquivo salvo com sucesso!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Editor de Texto")

# Área de texto
texto = tk.Text(janela, wrap="word", font=("Arial", 12))
texto.pack(expand=True, fill="both")

# Barra de menus
menu_barra = tk.Menu(janela)
menu_arquivo = tk.Menu(menu_barra, tearoff=0)
menu_arquivo.add_command(label="Novo", command=novo_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)
menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)

janela.config(menu=menu_barra)

# Iniciar o loop da interface
janela.mainloop()
