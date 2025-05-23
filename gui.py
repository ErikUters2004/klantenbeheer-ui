import sqlite3
import tkinter as tk
from tkinter import messagebox

# Verbinding met de database
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# Zoekfunctie
def zoek_speler():
    try:
        speler_id = int(entry.get())
    except ValueError:
        messagebox.showerror("Fout", "Voer een geldig nummer in.")
        return

    cursor.execute("SELECT volledige_naam FROM SpelerTeamView WHERE speler_id = ?", (speler_id,))
    resultaat = cursor.fetchone()

    if resultaat:
        label_resultaat.config(text=f"Gevonden: {resultaat[0]}", fg="green")
    else:
        label_resultaat.config(text="Niet gevonden", fg="red")

# GUI setup
root = tk.Tk()
root.title("Speler Zoeken")
root.attributes('-fullscreen', True)  # Volledig scherm

# Stijl
root.configure(bg="#f0f0f0")
font_titel = ("Helvetica", 24, "bold")
font_input = ("Helvetica", 18)
font_resultaat = ("Helvetica", 20)

# Frame om te centreren
frame = tk.Frame(root, bg="#f0f0f0")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Widgets
titel = tk.Label(frame, text="Speler Zoeken op ID", font=font_titel, bg="#f0f0f0")
titel.pack(pady=20)

entry = tk.Entry(frame, font=font_input, width=15, justify="center")
entry.pack(pady=10)

zoek_button = tk.Button(frame, text="Zoek", font=font_input, command=zoek_speler, width=10, bg="#007acc", fg="white")
zoek_button.pack(pady=10)

label_resultaat = tk.Label(frame, text="", font=font_resultaat, bg="#f0f0f0")
label_resultaat.pack(pady=20)

# Escape om fullscreen te verlaten
def sluit_af(event):
    root.destroy()

root.bind("<Escape>", sluit_af)

root.mainloop()
