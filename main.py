import customtkinter as ctk
from tkinter import *
import os #dir das images

def tabClick(tab):
    if tab == 'home':
        homeFrame.grid(row=0, column=1, sticky='nswe')
        homeButton.configure(fg_color='#1b1b1b')
    else:
        homeFrame.grid_forget()
        homeButton.configure(fg_color='transparent')
    if tab == 'list':
        listFrame.grid(row=0, column=1, sticky='nswe')
        listButton.configure(fg_color='#1b1b1b')
    else:
        listFrame.grid_forget()
        listButton.configure(fg_color='transparent')
    if tab == 'insert':
        insertFrame.grid(row=0, column=1, sticky='nswe')
        insertButton.configure(fg_color='#1b1b1b')
    else:
        insertFrame.grid_forget()
        insertButton.configure(fg_color='transparent')
#theme
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('dark-blue')

#config window
window = ctk.CTk()
window.title('Painel de Cadastro')
window.geometry('700x450')
window.resizable(width=False, height=False)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

#frames
sidebarFrame = ctk.CTkFrame(window, corner_radius=0, height=400, fg_color='#2b2b2b')
sidebarFrame.grid(row=0, column=0, sticky='nsew')
sidebarFrame.grid_rowconfigure(4, weight=1)

homeFrame = ctk.CTkFrame(window, corner_radius=0, height=400, fg_color='#1b1b1b')
homeFrame.grid(row=0, column=1, sticky='nswe')
listFrame = ctk.CTkFrame(window, corner_radius=0, height=400, fg_color='#1b1b1b')
insertFrame = ctk.CTkFrame(window, corner_radius=0, height=400, fg_color='#1b1b1b')

title = ctk.CTkLabel(sidebarFrame, text='SISTEMA DE\nCADASTRO', font=ctk.CTkFont(size=15, weight='bold'))
title.grid(row=0, column=0, padx=20, pady=20)

homeButton = ctk.CTkButton(sidebarFrame, hover_color='#3b3b3b', corner_radius=0, height=40, border_spacing=10, text='Página Inicial', fg_color='#1b1b1b', text_color='#fff', anchor='wns', command=lambda: tabClick('home'))
homeButton.grid(row=1, column=0, sticky='ew')

listButton = ctk.CTkButton(sidebarFrame, hover_color='#3b3b3b', corner_radius=0, height=40, border_spacing=10, text='Lista de Cadastros', fg_color='transparent', text_color='#fff', anchor='wns', command=lambda: tabClick('list'))
listButton.grid(row=2, column=0, sticky='ew')

insertButton = ctk.CTkButton(sidebarFrame, hover_color='#3b3b3b', corner_radius=0, height=40, border_spacing=10, text='Novos Cadastros', fg_color='transparent', text_color='#fff',anchor='wns', command=lambda: tabClick('insert'))
insertButton.grid(row=3, column=0, sticky='ew')

#widgets

#home
homeFrame.columnconfigure(0, weight=1)
homeFrame.rowconfigure(0, weight=1)
homeFrame.rowconfigure(1, weight=1)
homeFrame.rowconfigure(2, weight=1)
homeFrame.rowconfigure(3, weight=1)

titleHome = ctk.CTkLabel(homeFrame, text='Bem-vindo(a)!', font=ctk.CTkFont(size=25, weight='bold'))
titleHome.grid(row=0, column=0, padx=0, pady=0, sticky='swe')

captionHome = ctk.CTkLabel(homeFrame, text='Aproveite nosso sistema e tenha mais controle sobre seus clientes', font=ctk.CTkFont(size=15, weight='normal'))
captionHome.grid(row=1, column=0, padx=0, pady=0, sticky='nwe')

ramoHome = ctk.CTkLabel(homeFrame, text='Projeto desenvolvido pelo RAMO IEEE IFPB', font=ctk.CTkFont(size=16, weight='bold'))
ramoHome.grid(row=2, column=0, padx=0, pady=0, sticky='swe')

teamHome = ctk.CTkLabel(homeFrame, text='Samuel Medeiros\nMiguel Galvão\nErika\nJardson\nFelipe', font=ctk.CTkFont(size=15, weight='normal'))
teamHome.grid(row=3, column=0, padx=0, pady=0, sticky='nwe')



#list
listFrame.columnconfigure(0, weight=1)
listFrame.rowconfigure(0, weight=1)

titleList = ctk.CTkLabel(listFrame, text='Lista de Cadastros', font=ctk.CTkFont(size=25, weight='bold'))
titleList.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')



#insert
insertFrame.columnconfigure(0, weight=1)
insertFrame.rowconfigure(0, weight=1)

insertList = ctk.CTkLabel(insertFrame, text='Cadastrar', font=ctk.CTkFont(size=25, weight='bold'))
insertList.grid(row=0, column=0, padx=0, pady=0, sticky='nswe')



#end loop
window.mainloop()