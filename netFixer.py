import subprocess  
import tkinter as tk  
from tkinter import messagebox
from tkinter import ttk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def atualizar_barra(valor):
    barra['value'] = valor
    app.update_idletasks()

def executar_manutencao():
    # Função que executa os comandos de rede no CMD
    try:
        atualizar_barra(0)

        subprocess.run("ipconfig /release", shell=True, check=True)
        atualizar_barra(33)

        subprocess.run("ipconfig /flushdns", shell=True, check=True)
        atualizar_barra(66)

        subprocess.run("ipconfig /renew", shell=True, check=True)
        atualizar_barra(100)

        label_status["text"] = f"""Rede restaurada com sucesso!"""
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}\n\nLembre-se de rodar como Administrador!")

# Janela tkinter
app = tk.Tk()
app.title("NetFixer 1.5")

app.geometry("400x250")
app.resizable(False, False)
center_window(app)

label = tk.Label(app, text="Clique no botão para resetar as configurações de rede", wraplength=300).pack(pady=20)
botao = tk.Button(app, text="Restaurar Internet", command=executar_manutencao, 
bg="#0088f8", fg="white", font=("helvetica", 12, "bold"), padx=20, pady=10).pack(pady=10)

# Barra de progresso TTK
barra = ttk.Progressbar(app, orient="horizontal", length=200, mode='determinate')
barra.pack(pady=20)

label_status = tk.Label(app, text=" ", wraplength=300)
label_status.pack(pady=20)

app.mainloop()
