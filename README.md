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
- **Jeu de l'A9** (ex rond-point) : 3 niveaux (Montreux facile, Lausanne avec travaux et une petite fente, Genève avec plus de flashs et la police qui arrive par derrière). Ligne d’arrivée à atteindre ; 8 pièces bleues par niveau = régulateur à 50 km/h pendant 15 s ; les camions à rampe permettent de sauter par-dessus voitures et barrières ; en duel, le premier arrivé gagne.
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


## Records par jeu
Menu ARCADE → RECORDS : classement mondial par jeu (Arkanoid, Taupes, Foot Argentin = victoires contre le bot, L'A9 = un classement par niveau), avec le personnage et le nom du joueur. Les scores sont envoyés dans `hs/<jeu>/<id appareil>` : il faut republier `firebase-rules.json` (bloc `hs`) dans la console Firebase → Realtime Database → Règles.

**Jeu de l'A9 : score final** = 500 (arrivée) + points ramassés + bonus de temps (25 pts par seconde sous le temps de référence 60 / 75 / 90 s) + 3 × l’argent restant − 60 par amende. En duel, le plus haut score gagne.

## Le Concert (jeu de rythme beatbox)
Arcade → LE CONCERT. Les morceaux de Marc jouent SANS batterie : le joueur fait la batterie. Trois colonnes : B (kick), PF (caisse claire), TS (charley), tirées de la vraie batterie du morceau. Jamais deux sons en même temps : kick d'abord, puis caisse claire, le charley se place entre les deux.
Niveaux : 1 Les Sardines (facile, B + PF), 2 Ces soirées-là (moyen), 3 La Tribu de Dana (dur). À la fin, « We Are the Champions ».
Deux modes : PAD (on touche les colonnes, ou A S D) et MICRO (vrai beatbox). Le mode micro reprend le principe de Beatbox Hero : détection des attaques par flux spectral en 3 bandes (grave = B, medium = PF, aigu = TS), calibrage du silence au départ, un seul son par 45 ms. Casque conseillé ; écran TEST MICRO avant le jeu (B PF TS s'allument, niveau du micro, SENS, recalibrage) ; réglage DECAL (latence) dans le menu. Micro seulement sur GitHub Pages (https). Sons du mode pad : vrais échantillons de Marc (kick, pf, charley). Records séparés PAD / MICRO (onglet BEAT, retoucher l'onglet pour changer).

## Déblocages (persos et skins)
Le niveau du joueur monte avec les points gagnés en jouant (STAT_LV). Un perso avec `lvl: N` dans ROSTER est débloqué au niveau N (Cuche : niveau 3 ARTISTE). Jean-Luc reste débloqué en finissant un vote. Les skins : `SKIN_LV = { idperso: [0, niveau skin 2, niveau skin 3] }` (le premier est toujours libre) ; toucher le perso à l'écran de choix passe au skin suivant débloqué. Un toast annonce « X DEBLOQUE ! ». L'écran de choix a 6 colonnes (18 persos sur 3 rangées).

- **Ivo** (ingénieur lumière, débloqué au niveau 2 ARTISTE) et **Tommy** (gérant du Contretemps et du bar de la Revue, niveau 4 STAR) : nouveaux persos avec sprites perso.
- **Skins Keumart** : casquette de face (niv. 1), sans casquette (niv. 2), huissier (niv. 4, STAR).
- Le lien perso de Keumart (`...#keumart`) a tout débloqué d'office (persos, skins, Jean-Luc). Les autres débloquent selon leur niveau, chacun sur son téléphone.
- **Cases groupées** (TECHNIQUE, CONTRETEMPS…) : un skin = une personne, le nom et le rôle changent avec le skin (`grp` dans ROSTER, un niveau par skin dans SKIN_LV). Pour ajouter quelqu'un : un sprite de plus dans REAL_FILES + une entrée dans `grp` + un niveau dans SKIN_LV. Pas encore dans le vote « C'EST QUI ? ».
- **Arkanoid, bonus** (chute de 20 % à chaque brique cassée, 9 types) : 3 billes, vitesse, têtes chercheuses (3 cibles différentes), boule fragmentée (10 fragments qui visent chacun une brique), rayon laser, bille perforante (6 s), super laser (3,5 s, traverse tout), la fée (voeu au hasard), croix suisse (efface une ligne + une colonne). Score : combo (x1 à x3,5, remis à 0 quand la balle touche la raquette) + bonus de temps par niveau (400 pts max, 0 après 50 s) + 50 pts par vie restante à la victoire.
- **Arkanoid, suite** : raquette géante (10 s), raquette minuscule (malus, 8 s), bille ralentie (malus, 7 s), bouclier (sauve la bille une fois, 15 s). Les malus ont une icône violette. La fée donne n'importe quel objet au hasard, quel que soit le niveau. 13 objets au total.
- **Arkanoid, niveaux** : 10 niveaux. La couleur d'une brique = son nombre de coups (gris 1, bleu 2, violet 3, rouge 4, avec des points blancs en bas) ; niveau 1 tout gris, puis un dégradé de plus en plus dur. Les objets se débloquent au fil des niveaux (`BONUS_LV` : malus à partir du niveau 4, fée au niveau 2). La chance de chute monte à chaque brique cassée sans objet (environ un objet toutes les 5 à 6 briques), 2,5 s minimum entre deux, jamais deux fois le même d'affilée. Bille perforante, super laser et croix suisse cassent tout, même une brique à 4 coups.
- **Skin huissier** (niveau 4, STAR) pour Keumart (refait), Olivier, David (Mc Roger), Pierre, Léa et Karim. La case PRODUCTION reprend le sprite de Séhalia.
- **Ben Kiki** : skin ultime d'Olivier (bébé en poussette), niveau 5 LÉGENDE. Le nom de famille affiché change avec le skin (`SKIN_LAST`) : OLIVIER / BEN KIKI.
