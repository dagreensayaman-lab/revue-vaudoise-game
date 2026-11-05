# La Revue Vaudoise - jeu

Jeu pixel art autour du Magic Mirror de Territet. Un seul fichier : `index.html`.

## QR des cartes

Chaque carte ouvre le jeu avec son perso pre-selectionne :

- `?perso=jenny`, `?perso=keumart`, `?perso=lea`, `?perso=pierre`, `?perso=david`, `?perso=olivier`, `?perso=karim`, `?perso=catherine`, `?perso=veronique`
- Places libres avec nom pre-rempli : `?perso=prod&nom=Prenom`, `?perso=tech&nom=Prenom`, `?perso=guest&nom=Prenom`

## Vrais sprites

Mettre les PNG (fond transparent, meme taille, de face) dans `sprites/` et les lister dans `REAL_FILES` en haut de la partie persos de `index.html`, par exemple `{ jenny: 'sprites/jenny.png' }`.

Plusieurs costumes pour un meme perso : une liste, par exemple `{ jenny: ['sprites/jenny.png', 'sprites/jenny-pompier.png'] }`. Toucher le perso sur l'ecran de choix passe au costume suivant.

## Multijoueur en ligne (Firebase)
- Base : Realtime Database `revue-vaudoise-2b13c` (europe-west1), accès REST + sondage toutes les 0,8 s, sans SDK.
- MULTI → CRÉER UNE SALLE (code à 4 lettres) / REJOINDRE (taper le code) / JOUER SEUL (bots).
- Lien direct avec salle : `?perso=<id>&salle=ABCD`.
- Le maître du jeu (celui qui crée la salle) lance avec OK et fait avancer les questions ; s'il part, le plus ancien joueur reprend.
- Structure : `rooms/CODE/{h, st, p, g, v, res}`.
- Règles de sécurité à publier dans la console Firebase : voir `firebase-rules.json`.
