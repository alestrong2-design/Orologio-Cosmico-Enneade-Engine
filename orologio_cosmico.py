"""
==========================================================================
                     🌎 OROLOGIO COSMICO - ENNEADE ENGINE 🌍
==========================================================================
 SPDX-License-Identifier: MIT
 Copyright (c) 2026 alestrong2-design
==========================================================================
"""

import math
import tkinter as tk
from datetime import datetime
from tkinter import ttk


class OrologioCosmicoOpenSource:

    def __init__(self, root):
        self.root = root
        self.root.title(
            "OROLOGIO COSMICO - ENNEADE ENGINE (OPEN SOURCE VERSION)"
        )
        self.root.geometry("1100x780")
        self.root.configure(bg="#0D0D13")

        self.data_pivot = datetime(1985, 1, 1)
        self.vel_cupola = 395.6337 / 365.2422
        self.spicchio_13 = 360.0 / 13.0

        self.spicchi = [
            "Ariete",
            "Toro",
            "Gemelli",
            "Cancro",
            "Leone",
            "Vergine",
            "Bilancia",
            "Scorpione",
            "Sagittario",
            "Capricorno",
            "Acquario",
            "Pesci",
            "Ofiuco",
        ]

        self.config_enneade = {
            "MERCURIO": {
                "giro_gg": 87.969,
                "scatto_freno": 13,
                "offset": 185.50,
                "colore": "#E5E5E5",
            },
            "MARTE": {
                "giro_gg": 686.980,
                "scatto_freno": 12,
                "offset": 48.30,
                "colore": "#FF4444",
            },
            "VENERE": {
                "giro_gg": 224.701,
                "scatto_freno": 11,
                "offset": 222.10,
                "colore": "#44FF44",
            },
            "GIOVE": {
                "giro_gg": 4332.589,
                "scatto_freno": 10,
                "offset": 298.15,
                "colore": "#FFCC00",
            },
            "SATURNO": {
                "giro_gg": 10759.22,
                "scatto_freno": 9,
                "offset": 115.60,
                "colore": "#FFAA00",
            },
            "NETTUNO": {
                "giro_gg": 60189.00,
                "scatto_freno": 8,
                "offset": 272.40,
                "colore": "#00FFFF",
            },
            "URANO": {
                "giro_gg": 30685.40,
                "scatto_freno": 7,
                "offset": 240.20,
                "colore": "#00AAFF",
            },
            "CHIRONE": {
                "giro_gg": 18429.00,
                "scatto_freno": 6,
                "offset": 98.40,
                "colore": "#CC00FF",
            },
            "PLUTONE": {
                "giro_gg": 90560.00,
                "scatto_freno": 5,
                "offset": 212.80,
                "colore": "#FF00AA",
            },
        }

        self.costruisci_ui()
        self.esegui_calcolo("2026-10-19")

    def costruisci_ui(self):
        top_frame = tk.Frame(self.root, bg="#161622", height=75)
        top_frame.pack(fill=tk.X, side=tk.TOP)

        tk.Label(
            top_frame,
            text="📅 INSERISCI DATA CIVILE (YYYY-MM-DD):",
            font=("Consolas", 11, "bold"),
            fg="#8F92A1",
            bg="#161622",
        ).pack(side=tk.LEFT, padx=20, pady=20)

        self.input_data = tk.Entry(
            top_frame,
            font=("Consolas", 12, "bold"),
            width=12,
            bg="#1F1F2E",
            fg="#00FF00",
            bd=0,
            justify=tk.CENTER,
        )
        self.input_data.insert(0, "2026-10-19")
        self.input_data.pack(side=tk.LEFT, padx=5, pady=20)

        btn = tk.Button(
            top_frame,
            text="🎡 ATTIVA INGRANAGGIO COSMICO",
            font=("Consolas", 10, "bold"),
            bg="#0088FF",
            fg="white",
            bd=0,
            padx=20,
            command=lambda: self.esegui_calcolo(self.input_data.get()),
        )
        btn.pack(side=tk.LEFT, padx=20, pady=20)

        main_frame = tk.Frame(self.root, bg="#0D0D13")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        left_frame = tk.Frame(main_frame, bg="#0D0D13")
        left_frame.pack(side=tk.LEFT, padx=10)

        self.canvas = tk.Canvas(
            left_frame,
            width=500,
            height=460,
            bg="#0D0D13",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.cal_frame = tk.Frame(left_frame, bg="#161622", bd=1, relief=tk.SOLID)
        self.cal_frame.pack(fill=tk.X, pady=10, ipady=10)

        self.lbl_cal_titolo = tk.Label(
            self.cal_frame,
            text="CALENDARIO GEOMETRICO A 13 MESI PERFETTI",
            font=("Consolas", 10, "bold"),
            fg="#00FF00",
            bg="#161622",
        )
        self.lbl_cal_titolo.pack(pady=2)

        self.lbl_cal_data = tk.Label(
            self.cal_frame,
            text="CARICAMENTO...",
            font=("Consolas", 14, "bold"),
            fg="#FFFFFF",
            bg="#161622",
        )
        self.lbl_cal_data.pack(pady=5)

        self.tabella = ttk.Treeview(
            main_frame, columns=("Corpo", "Spicchio", "Gradi"), show="headings"
        )
        self.tabella.heading("Corpo", text="LUMINARE / ASTRO")
        self.tabella.heading("Spicchio", text="SPICCHIO CONTINENTALE")
        self.tabella.heading("Gradi", text="GRADI INTERNI")
        self.tabella.column("Corpo", width=110, anchor=tk.CENTER)
        self.tabella.column("Spicchio", width=190, anchor=tk.CENTER)
        self.tabella.column("Gradi", width=140, anchor=tk.CENTER)
        self.tabella.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

        self.lbl_gft = tk.Label(
            self.root,
            text="🛡️ LICENZA MIT OPEN SOURCE | VALVOLA GFT REIMPOSTA DRIFT CPU HARDWARE A: 0.0000000",
            font=("Consolas", 9, "bold"),
            fg="#00FF00",
            bg="#0D0D13",
        )
        self.lbl_gft.pack(pady=10, side=tk.BOTTOM)

    def calcola_nuovo_calendario(self, data_t):
        giorno_anno = data_t.timetuple().tm_yday
        mesi_13 = [
            "Primavera Prima",
            "Primavera Seconda",
            "Primavera Terza",
            "Estate Prima",
            "Estate Seconda",
            "Estate Terza",
            "Autunno Primo",
            "Autunno Secondo",
            "Autunno Terzo",
            "Inverno Primo",
            "Inverno Secondo",
            "Inverno Terzo",
            "Mese Tredicesimo",
        ]
        giorni_settimana = [
            "Lunedì",
            "Martedì",
            "Mercoledì",
            "Giovedì",
            "Venerdì",
            "Sabato",
            "Domenica",
        ]

        giorno_gft = 172

        if giorno_anno == giorno_gft:
            return "🛡️ GIORNO FUORI DAL TEMPO (VALVOLA GFT ATTIVA)"

        giorno_effettivo = giorno_anno
        if giorno_anno > giorno_gft:
            giorno_effettivo = giorno_anno - 1

        if giorno_effettivo > 364:
            return "🛡️ SECONDO GIORNO INTERCALARE (RESET BISESTILE)"

        indice_mese = (giorno_effettivo - 1) // 28
        giorno_mese = ((giorno_effettivo - 1) % 28) + 1
        nome_giorno = giorni_settimana[(giorno_mese - 1) % 7]

        return f"{nome_giorno.upper()} {giorno_mese} - {mesi_13[indice_mese].upper()}"

    def disegna_orologio(self, posizioni):
        self.canvas.delete("all")
        cx, cy, r = 250, 220, 180

        for i, nome in enumerate(self.spicchi):
            ang = i * (360.0 / 13.0) - 90
            rad = math.radians(ang)
            self.canvas.create_line(
                cx,
                cy,
                cx + r * math.cos(rad),
                cy + r * math.sin(rad),
                fill="#1F1F2E",
                width=1.5,
            )

            rad_t = math.radians(ang + (360.0 / 26.0))
            self.canvas.create_text(
                cx + (r + 20) * math.cos(rad_t),
                cy + (r + 20) * math.sin(rad_t),
                text=nome.upper()[:3],
                fill="#565676",
                font=("Consolas", 8, "bold"),
            )

        self.canvas.create_oval(
            cx - r, cy - r, cx + r, cy + r, outline="#2D2D3A", width=2
        )

        self.canvas.create_line(
            cx, cy - r - 5, cx, cy + r + 5, fill="#FF4444", width=1, dash=(2, 4)
        )
        self.canvas.create_line(
            cx - r - 5, cy, cx + r + 5, cy, fill="#4488FF", width=1, dash=(2, 4)
        )

        self.canvas.create_text(
            cx,
            cy - r - 12,
            text="NORD",
            fill="#FF4444",
            font=("Consolas", 8, "bold"),
        )
        self.canvas.create_text(
            cx,
            cy + r + 12,
            text="SUD",
            fill="#FFFFFF",
            font=("Consolas", 8, "bold"),
        )
        self.canvas.create_text(
            cx + r + 18,
            cy,
            text="EST",
            fill="#FFFFFF",
            font=("Consolas", 8, "bold"),
        )
        self.canvas.create_text(
            cx - r - 22,
            cy,
            text="OVEST",
            fill="#FFFFFF",
            font=("Consolas", 8, "bold"),
        )

        r_dinamico = 160
        for corpo in self.config_enneade.keys():
            long_zod = posizioni[corpo]
            col = self.config_enneade[corpo]["colore"]

            rad_p = math.radians(long_zod - 90)
            px = cx + r_dinamico * math.cos(rad_p)
            py = cy + r_dinamico * math.sin(rad_p)

            self.canvas.create_line(cx, cy, px, py, fill=col, width=1.5)
            self.canvas.create_oval(
                px - 4, py - 4, px + 4, py + 4, fill=col, outline="#FFFFFF", width=1
            )
            self.canvas.create_text(
                px,
                py - 12,
                text=corpo[:3],
                fill="#FFFFFF",
                font=("Consolas", 8, "bold"),
            )
            r_dinamico -= 14

    def esegui_calcolo(self, data_str):
        try:
            data_t = datetime.strptime(data_str, "%Y-%m-%d")
        except ValueError:
            return
        
        testo_cal = self.calcola_nuovo_calendario(data_t)
        self.lbl_cal_data.configure(text=testo_cal)
        
        giorni = (data_t - self.data_pivot).days
        for item in self.tabella.get_children():
            self.tabella.delete(item)
            
        posizioni_attuali = {}
        for p, par in self.config_enneade.items():
            giri = giorni // par["giro_gg"]
            pos_ciclo = giorni % par["giro_gg"]
            gradi_persi = (giri * par["scatto_freno"]) + (
                (pos_ciclo / par["giro_gg"]) * par["scatto_freno"]
            )
            long_zod = ((giorni * self.vel_cupola) + par["offset"] - gradi_persi) % 360.0
            posizioni_attuali[p] = long_zod
            ind_spicchio = int(long_zod // self.spicchio_13) % 13
            gradi_interni = long_zod % self.spicchio_13
            
            self.tabella.insert(
                "",
                tk.END,
                values=(
                    p,
                    self.spicchi[ind_spicchio].upper(),
                    f"{gradi_interni:.2f}° / {self.spicchio_13:.2f}°",
                ),
            )
            
        self.disegna_orologio(posizioni_attuali)


if __name__ == "__main__":
    root = tk.Tk()
    app = OrologioCosmicoOpenSource(root)
    root.mainloop()
