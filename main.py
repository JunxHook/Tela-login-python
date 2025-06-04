import customtkinter as ctk
from tkinter import messagebox

# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Janela principal
janela = ctk.CTk()
janela.geometry("400x500")
janela.title("Login UI")

# --- Adicione estas linhas para o background ---
from customtkinter import CTkImage
from PIL import Image

bg_image = CTkImage(Image.open("images/vlue.png"), size=(400, 500))
bg_label = ctk.CTkLabel(janela, image=bg_image, text="")
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
# ------------------------------------------------

# Frame central
frame = ctk.CTkFrame(janela, width=350, height=1000, corner_radius=0)
frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
# Campo de e-mail
entrada_email = ctk.CTkEntry(frame, placeholder_text="👤Email ID", width=400)
entrada_email.pack(pady=(10, 10))

# Campo de senha
entrada_senha = ctk.CTkEntry(frame, placeholder_text="🔐Password", show="*", width=300)
entrada_senha.pack(pady=(0, 10))

# Linha: Remember me e Esqueceu senha?
linha_opcoes = ctk.CTkFrame(frame, fg_color="transparent")
linha_opcoes.pack(fill="x", pady=(5, 10), padx=25)



forgot_label = ctk.CTkLabel(linha_opcoes, text="Register", text_color="gray")
forgot_label.pack(side="bottom")

# Botão de login
def login():
    email = entrada_email.get()
    senha = entrada_senha.get()
    if email == "admin@example.com" and senha == "1234":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Credenciais inválidas.")

botao_login = ctk.CTkButton(frame, text="LOGIN", command=login, fg_color="#000981", hover_color="#01004d", width= )
botao_login.pack(pady=(20, 50))

# Rodar app
janela.mainloop()