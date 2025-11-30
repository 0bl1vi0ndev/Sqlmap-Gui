import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import subprocess
import threading
import os

def lancer_sqlmap():
    url = entry_url.get().strip()

    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL.")
        return

    command = [
        "sqlmap.bat",
        "-u", url,
        "--batch",
        "--random-agent",
        "--risk=3",
        "--level=5",
        "--threads=10",
        "--dbs",
        "--forms",
        "--crawl=3",
        "--flush-session",
        "--output-dir=./sqlmap_output"
    ]

    text_output.insert("end", "Commande lancée :\n")
    text_output.insert("end", " ".join(command) + "\n")
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

            text_output.insert("end",
                "\nScan terminé. Résultats dans le dossier sqlmap_output.\n"
            )
            text_output.see("end")

        except FileNotFoundError:
            messagebox.showerror(
                "Fichier introuvable",
                "Impossible de lancer sqlmap.bat.\n"
                "Vérifiez que SQLMap est bien installé ou est dans le path (suivre tutoriel)."
            )

    threading.Thread(target=executer_sqlmap, daemon=True).start()


root = tk.Tk()
root.title("SQLMap GUI by oblivion")
root.geometry("1100x750")
root.configure(bg="#121212")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=12, font=("Segoe UI", 10, "bold"))

top = tk.Frame(root, bg="#121212")
top.pack(pady=15, padx=20, fill="x")

tk.Label(
    top,
    text="URL à analyser :",
    font=("Consolas", 14, "bold"),
    bg="#121212",
    fg="#00ff41"
).pack(side="left")

entry_url = tk.Entry(
    top,
    font=("Consolas", 14),
    width=80,
    relief="flat",
    bg="#1e1e1e",
    fg="#00ff41",
    insertbackground="#00ff41"
)
entry_url.pack(side="left", padx=(10, 0), fill="x", expand=True)
entry_url.insert(0, "http://testphp.vulnweb.com/listproducts.php?cat=1")

btn = ttk.Button(top, text="LANCER SQLMAP", command=lancer_sqlmap)
btn.pack(side="right", padx=(15, 0))

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
text_output.pack(fill="both", expand=True, padx=20, pady=(0, 20))

message_accueil = """
SQLMAP GUI – Info rapide :

Commande utilisée :
sqlmap.bat -u "URL" --batch --random-agent --risk=3 --level=5 --threads=10 --dbs --forms --crawl=3 --flush-session --output-dir=./sqlmap_output

Options principales :
- risk 3 / level 5 : tests complets
- forms : test des formulaires
- crawl 3 : exploration modérée
- threads 10 : un peu plus rapide

Options avancées possibles :
--tamper=space2comment,randomcase
--proxy=http://127.0.0.1:8080
--dump-all
--os-shell

"""

text_output.insert("end", message_accueil)
text_output.insert("end", "=" * 130 + "\n")

root.mainloop()
