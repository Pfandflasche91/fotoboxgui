import os
import tkinter as tk
import random
import ttkbootstrap as ttk  # Modernes Styling für Tkinter

class FullscreenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moderne GUI mit zufälligen Zahlen")
        self.root.attributes("-fullscreen", True)  # Vollbildmodus aktivieren

        # Style-Objekt erstellen
        style = ttk.Style()
        style.theme_use("superhero")  # Windows 11-ähnliches Theme setzen

        # Label erstellen
        self.label = ttk.Label(root, text="Willkommen!", font=("Segoe UI", 32, "bold"), anchor="center", width=20)
        self.label.grid(row=0, column=0, columnspan=3, pady=40)

        # Buttons in einem 2x3-Raster (2 Zeilen, 3 Spalten)

        # Button zum Anzeigen einer zufälligen Zahl
        self.random_number_button_1 = ttk.Button(root, text="Zufallszahl 1", command=self.show_random_number, style="modern.TButton")
        self.random_number_button_1.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Button zum Anzeigen einer zufälligen Zahl
        self.random_number_button_2 = ttk.Button(root, text="Zufallszahl 2", command=self.show_random_number, style="modern.TButton")
        self.random_number_button_2.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

        # Button zum Anzeigen einer zufälligen Zahl
        self.random_number_button_3 = ttk.Button(root, text="Zufallszahl 3", command=self.show_random_number, style="modern.TButton")
        self.random_number_button_3.grid(row=1, column=2, padx=20, pady=10, sticky="nsew")

        # Button zum Anzeigen einer zufälligen Zahl
        self.random_number_button_4 = ttk.Button(root, text="Zufallszahl 4", command=self.show_random_number, style="modern.TButton")
        self.random_number_button_4.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # Button zum Anzeigen einer zufälligen Zahl
        self.random_number_button_5 = ttk.Button(root, text="Zufallszahl 5", command=self.show_random_number, style="modern.TButton")
        self.random_number_button_5.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

        # Beenden-Button (Zufallszahl 6)
        self.random_number_button_6 = ttk.Button(root, text="Zufallszahl 6", command=self.show_random_number, style="modern.TButton")
        self.random_number_button_6.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")

        # Escape-Taste zum Beenden
        self.root.bind("<Escape>", lambda event: self.close_app())

        # Handle das Schließen des Fensters, wenn das X in der Ecke gedrückt wird
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

        # Anpassen der Gewichtung für Spalten und Zeilen
        self.root.grid_rowconfigure(0, weight=1)  # Erste Zeile (Label)
        self.root.grid_rowconfigure(1, weight=1)  # Zweite Zeile (Buttons)
        self.root.grid_rowconfigure(2, weight=1)  # Dritte Zeile (Buttons)
        self.root.grid_columnconfigure(0, weight=1)  # Erste Spalte (Buttons)
        self.root.grid_columnconfigure(1, weight=1)  # Zweite Spalte (Buttons)
        self.root.grid_columnconfigure(2, weight=1)  # Dritte Spalte (Buttons)

    def show_random_number(self):
        # Zeige eine zufällige Zahl zwischen 1 und 100
        random_number = random.randint(1, 100)
        self.label.config(text=f"Zufallszahl: {random_number}")

    def close_app(self):
        # Stoppe das GUI und schließe das Fenster
        self.root.quit()  # Beendet die mainloop und schließt das Fenster
        self.root.destroy()  # Zerstört das GUI-Fenster

if __name__ == "__main__":
    os.environ["DISPLAY"] = ":0"  # DISPLAY-Variable für Raspberry Pi setzen
    root = ttk.Window()  # Modernes Fenster
    app = FullscreenApp(root)
    root.mainloop()
