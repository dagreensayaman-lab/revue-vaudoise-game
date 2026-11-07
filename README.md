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

## Nouveaux tours et mini-jeux
- **Menteur** : chacun raconte une anecdote sur un thème, l'app désigne un menteur (secret) ; la salle vote pour le démasquer. Il faut au moins 3 joueurs.
- **Rapidité et pari** (questions « Qui… ? ») : répondre dans les 4 premières secondes rapporte +60 pts, dans les 8 premières +30 (seulement si ta réponse est dans la majorité). Le bouton PARI engage un pourcentage : 50 %+ (+50 / −30), 70 %+ (+100 / −50) ou 100 % (+200 / −80). Le score ne descend jamais sous 0.
- **Duel de taps** : deux joueurs tapent le plus vite possible pendant 10 s (ou jusqu'à 28 taps d'avance).
- **Roue des gages** : chaque joueur propose un gage anonyme au salon (bouton « MON GAGE ») ; la roue désigne un joueur et révèle un gage au hasard.
- **ARCADE** : Arkanoid (3 niveaux) et Pousse ton adversaire (contre un bot) ; **VERSUS** : Pousse à deux sur le même téléphone.

## Nouveautés
- Manches TAUPES (marteau, taper sa propre tête fait perdre des points) et ARKANOID (tout le monde joue, le premier qui finit gagne).
- Roue des gages avec les gages écrits par les joueurs (bouton GAGE dans le salon).
- Bouton QUESTION dans le salon : chaque joueur propose « QUI… » ; 2 questions sont tirées au sort dans la partie.
- Skins : touche le grand perso pour changer (Virginie, public, techniciens, prod).

- Musique : « Les Sardines » (8 bits, en boucle) par défaut ; la petite note en bas à droite change de morceau (Phase 1 / Les Sardines).
- Fin de partie : « We Are the Champions » (8 bits) joue pendant l'annonce des gagnants, puis la musique reprend.
- Écran d'accueil : accompagnement 8 bits de « Ces soirées-là » (1er toucher = musique, 2e toucher = entrer).
- Choix des persos : « La Tribu de Dana » (8 bits, en boucle). Le morceau de chaque écran se règle dans `MUSIC_PLAN` (en haut de `trackWatch` dans `index.html`).

## Duel en ligne
VERSUS → DUEL EN LIGNE ouvre la salle. Dans la salle, touche le perso d un joueur puis INVITER : il reçoit une invitation (OUI/NON) et vous jouez au POUSSE en 1 contre 1, chacun sur son téléphone.

Duel en ligne : au choix POUSSE ou TAUPES (même graine pour les deux joueurs, meilleur score gagne).
Arkanoid : bonus qui tombent (casserole, fée, drapeau suisse, micro) = 3 billes, vitesse, 3 têtes chercheuses, boule collante, rayon laser.

## Loup-Garou (en ligne)
Dans une salle, le maître du jeu appuie sur LOUP-GAROU, règle les rôles (auto selon le nombre de joueurs) et lance. Chacun reçoit son rôle en secret sur son téléphone ; nuits, votes et morts sont gérés automatiquement (loups, villageois, voyante, sorcière, chasseur, Cupidon). Minimum 4 joueurs.

## Cartes de stats
Chaque joueur a une carte (niveau, points, parties solo / susceptible / loup-garou / duels, titres comme « le plus voté »). Stockée sur l'appareil (localStorage) et partagée dans la salle : touche un joueur → VOIR LA CARTE, ou touche ton propre perso.

## Classement général
Menu SALLE DE JEU → CLASSEMENT (points, duels, loups, votés). Les stats sont envoyées dans `stats/<id appareil>` : il faut les règles de `firebase-rules.json` (bloc `stats`) dans la console Firebase → Realtime Database → Règles → Publier.
