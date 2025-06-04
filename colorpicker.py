import customtkinter as ctk
from tkinter import colorchooser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Color Picker Example")
janela.geometry("400x200")

def escolher_cor():
    cor = colorchooser.askcolor(title="Escolha uma cor")[1]
    if cor:
        cor_label.configure(text=f"Cor escolhida: {cor}", text_color=cor)

botao_cor = ctk.CTkButton(janela, text="Escolher Cor", command=escolher_cor)
botao_cor.pack(pady=30)
cor_label = ctk.CTkLabel(janela, text="Nenhuma cor escolhida", text_color="black")
cor_label.pack()

janela.mainloop()