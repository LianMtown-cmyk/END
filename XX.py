import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

# --- CONFIG (Hier kannst du deine Texte und die URL anpassen) ---
TitleText = "! UNDER CONTROLL !"
BodyText  = "This device is under controll by KaynixTeam !"
FooterText = "Kaynix Team - Fsoceity V0"

# Deine Bild-URL
ImageUrl  = "https://i.ibb.co/jsg95Lp/666.png"
# -----------------------------------------------------------------

# Hauptfenster erstellen
root = tk.Tk()
root.title("Fullscreen")
root.attributes("-fullscreen", True)
root.configure(background='black')

# Funktion, um das Fenster zu schließen
def on_escape(event):
    root.destroy()

# Escape-Taste zum Schließen hinzufügen
root.bind('<Escape>', on_escape)

# Titeltext (rot, größer)
title_label = tk.Label(
    root, 
    text=TitleText, 
    font=("Arial", 72, "bold"), 
    fg="#FF3232", 
    bg="black", 
    pady=10
)
title_label.pack(pady=(40, 10))

# Bodytext (weiß, mittelgroß)
body_label = tk.Label(
    root, 
    text=BodyText, 
    font=("Arial", 24), 
    fg="white", 
    bg="black", 
    pady=10
)
body_label.pack(pady=(0, 20))

# Bild laden
response = urlopen(ImageUrl)
image_data = response.read()
image = Image.open(BytesIO(image_data))
image = image.resize((450, 450), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# --- ZENTRIERTER CONTAINER FÜR BILD, TEXT & BUTTON ---
center_frame = tk.Frame(root, bg="black")
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# Bild anzeigen
image_label = tk.Label(center_frame, image=photo, bg="black")
image_label.pack()

# Neuer Hinweistext (direkt unter dem Bild)
instruction_label = tk.Label(
    center_frame,
    text="To return to your pc press the button below",
    font=("Arial", 18),
    fg="white",
    bg="black"
)
instruction_label.pack(pady=(25, 15)) # Abstand nach oben zum Bild und nach unten zum Button

# "I Agree" Button
agree_button = tk.Button(
    center_frame,
    text="I Agree",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#FF3232",
    activebackground="#B22222",
    activeforeground="white",
    relief="flat",
    padx=35,
    pady=10,
    command=root.destroy
)
agree_button.pack(pady=(0, 0))
# -----------------------------------------------------

# Footertext (grau, klein)
footer_label = tk.Label(
    root, 
    text=FooterText, 
    font=("Arial", 14), 
    fg="gray", 
    bg="black", 
    pady=10
)
footer_label.pack(side="bottom", pady=(0, 50))

# Hauptschleife starten
root.mainloop()