🟦 1) Télécharger SQLMap

Téléchargez SQLMap depuis le dépôt officiel :
https://github.com/sqlmapproject/sqlmap

Placez le dossier dans un emplacement simple, par exemple :

C:\Users\votre_nom\sqlmap\


Le dossier doit contenir un fichier important :

sqlmap.py

🟦 2) déplacer le fichier sqlmap.bat (INDISPENSABLE SUR WINDOWS)

Windows ne sait pas exécuter SQLMap directement, car c’est un fichier Python.
Donc on déplace un petit fichier .bat qui servira de lanceur déja préparé par moi.

👉 Dans le dossier où se trouve sqlmap.py, déplacer le fichier "sqlmap.bat" déposé que j'ai deja préparé
dans le projet (y suffit juste de le deplacer dans le chemin de sqlmap) :


Ce fichier dit simplement à Windows :

"Quand quelqu’un tape sqlmap, exécute python sqlmap.py automatiquement."

🎉 Après ça, la commande sqlmap devient utilisable comme un vrai programme.

🟦 3) Ajouter SQLMap dans le PATH Windows

Le PATH sert à dire à Windows :
➡️ “Voici un dossier où tu peux trouver des programmes exécutables.”

Faites EXACTEMENT ceci :

Appuyez sur Windows + R

Tapez :

sysdm.cpl


Allez dans l’onglet Avancé

Cliquez sur Variables d’environnement

Dans Variables système, trouvez :

Path


Cliquez sur Modifier

Cliquez sur Nouveau

Ajoutez le dossier où se trouve SQLMap, par exemple :

C:\Users\votre_nom\sqlmap\


Cliquez OK partout pour enregistrer.

🎉 Windows sait maintenant où chercher la commande sqlmap.

🟦 4) Vérifier que tout fonctionne

Ouvrez un nouveau CMD
(pas un ancien déjà ouvert)

Tapez :

sqlmap --version


Si tout est bien configuré, vous verrez une version, par exemple :

1.7.9#dev


✔️ Si une version s’affiche → SQLMap est installé correctement
❌ Si une erreur apparaît → le PATH n'est pas bien configuré

🟦 5) SQLMap est maintenant prêt pour SQLMap GUI il ne suffit plus que de lancer le sql map gui