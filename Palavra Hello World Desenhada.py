import tkinter as tk

# Função para criar a interface
def criar_interface():
    # Janela principal
    janela = tk.Tk()
    janela.title("Hello World em Grande Estilo")
    janela.geometry("800x400")  # Define o tamanho da janela
    janela.configure(bg="lightblue")  # Cor de fundo da janela

    # Texto em destaque
    label = tk.Label(
        janela, 
        text="HELLO WORLD", 
        font=("Arial", 48, "bold"),  # Fonte grande e em negrito
        fg="white",  # Cor do texto
        bg="purple",  # Fundo do texto
        padx=20,  # Espaçamento horizontal
        pady=20  # Espaçamento vertical
    )
    label.pack(pady=50)  # Centraliza o texto na janela com espaçamento vertical

    # Inicia o loop principal
    janela.mainloop()

# Executa o programa
if __name__ == "__main__":
    criar_interface()
