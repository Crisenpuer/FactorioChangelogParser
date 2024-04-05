import tkinter, sys
import customtkinter as ctk

version_range = 'all'

def versionrangeRadioButtonClickEvent():
    global version_range
    version_range = versionrangeRadioVar.get()
    if version_range == 'range':
        versionrangeEntry.configure(state='normal')
    else:
        versionrangeEntry.configure(state='disabled')

# CustomTkinter main init
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# root setup
root = ctk.CTk()
root.geometry('480x640')
root.title('Factorio Changelog Parser by Crisenpuer')
root.resizable(False,False)

# Global variables
version_header_style:str = None

# 460x620
MainFrame = ctk.CTkFrame(master=root)
MainFrame.pack(pady=10, padx=10, fill='both', expand=True)

# Title
titleFrame = ctk.CTkFrame(MainFrame, 440, 200)
titleFrame.pack(pady=10, anchor='n')
titleLabel = ctk.CTkLabel(titleFrame, text='Factorio Changelog Parser'.upper(), font=('Calibri',32))
titleLabel.pack(anchor='c', pady=10, padx=10)

# Input path
inputpathFrame = ctk.CTkFrame(MainFrame, 215, 200)
inputpathFrame.pack(pady=2.5, padx=0, anchor='n')
inputpathLabel = ctk.CTkLabel(inputpathFrame, text='Input file (changelog.txt)', font=('Calibri', 16))
inputpathLabel.pack(anchor='w', pady=5, padx=10)
inputpathEntry = ctk.CTkEntry(inputpathFrame, state='normal', width=420, placeholder_text="ex. C:/absolute/path/to/changelog.txt or relative/path/to/changelog.txt")
inputpathEntry.pack(anchor='n', pady=10, padx=10)

# Output path
outputpathFrame = ctk.CTkFrame(MainFrame, 215, 200)
outputpathFrame.pack(pady=10, padx=0, anchor='n')
outputpathLabel = ctk.CTkLabel(outputpathFrame, text='Output file (.md)', font=('Calibri', 16))
outputpathLabel.pack(anchor='w', pady=5, padx=10)
outputpathEntry = ctk.CTkEntry(outputpathFrame, state='normal', width=420, placeholder_text="ex. C:/absolute/path/to/CHANGELOG.md or relative/path/to/CHANGELOG.md")
outputpathEntry.pack(anchor='n', pady=10, padx=10)

# Version range chooser
versionrangeFrame = ctk.CTkFrame(MainFrame, 215, 240)
versionrangeFrame.pack(padx=10, pady=10, anchor='n')
versionrangeLabel = ctk.CTkLabel(versionrangeFrame, text='Version Range'.upper(), font=('Calibri', 16))
versionrangeLabel.pack(anchor='n', pady=10, padx=10)
versionrangeRadioVar = tkinter.StringVar(value='all')
versionrangeRadioButton1 = ctk.CTkRadioButton(versionrangeFrame, text="All Versions", command=versionrangeRadioButtonClickEvent, variable=versionrangeRadioVar, value='all', font=('Calibri',12), radiobutton_height=16, radiobutton_width=16, border_width_checked=4, border_width_unchecked=2)
versionrangeRadioButton2 = ctk.CTkRadioButton(versionrangeFrame, text="Latest Version", command=versionrangeRadioButtonClickEvent, variable=versionrangeRadioVar, value='latest', font=('Calibri',12), radiobutton_height=16, radiobutton_width=16, border_width_checked=4, border_width_unchecked=2)
versionrangeRadioButton3 = ctk.CTkRadioButton(versionrangeFrame, text="Version Range (X.X.X-X.X.X)", command=versionrangeRadioButtonClickEvent, variable=versionrangeRadioVar, value='range', font=('Calibri',12), radiobutton_height=16, radiobutton_width=16, border_width_checked=4, border_width_unchecked=2)
versionrangeRadioButton1.pack(anchor='w', pady=0, padx=10)
versionrangeRadioButton2.pack(anchor='w', pady=0, padx=10)
versionrangeRadioButton3.pack(anchor='w', pady=0, padx=10)
versionrangeEntry = ctk.CTkEntry(versionrangeFrame, state='disabled', placeholder_text='X.X.X-X.X.X')
versionrangeEntry.pack(anchor='n', pady=10, padx=10)

# Version header style
versionheaderstyleStringVar = ctk.StringVar()
versionheaderstyleFrame = ctk.CTkFrame(MainFrame, 215, 200)
versionheaderstyleFrame.pack(pady=2.5, padx=0, anchor='n')
versionheaderstyleComboBox = ctk.CTkComboBox(versionheaderstyleFrame, width=420, font=('Calibri', 16), variable=versionheaderstyleStringVar, values=["Title (#)", "Subtitle (##)"])


versionrangeRadioButton1.select()

root.mainloop()