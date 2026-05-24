import customtkinter as ctk

from scripts.decoder import decode as dc
from scripts.encoder import encode as ec

app = ctk.CTk()
app.geometry("600x350")
app.title("panzerWar json editor v0.0.2")


button1 = ctk.CTkButton(app, text="decode", command=dc)
button1.grid(row=0, column=0, padx=75, pady=280)

button2 = ctk.CTkButton(app, text="encode", command=ec)
button2.grid(row=0, column=1, padx=75, pady=280)

app.mainloop()
