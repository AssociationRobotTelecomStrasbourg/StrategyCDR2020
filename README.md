# StrategyCDR2020

---

## Liste des tâches

- [ ] Liste des objectifs
  - [x] Position
  - [x] Calculs des distances par rapport au robot
- [ ] Choix des objectifs
  - [x] Basique
  - [] Avancé
- [ ] Déplacements
- [ ] Prise en compte des obstacles

## Résumé des règles

Première version pour la stratégie : coût = distance

_On pourra ensuite réfléchir à quelque chose de plus poussé, par exemple avec un ratio gain de points/temps nécessaire_

Liste des tâches possibles :

* **GOBELETS** : récupérer des gobelets (pas la priorité) (il y en a "à la dérive" dans l'aire de jeu, d'autres sur des "écueils" à l'arrière de l'air de jeu (ordre des bouées alétaoire), et d'autres le long des bordures latérales et réservées à l'équipe qui a la zone de départ la plus proche (l'ordre des gobelets y est fixe))
  * 1 point par bouée dans le port (dans n’importe quel position)
  * 1 point supp par bouée si elle touche la ligne du chenal et qu’elle est debout (à l’envers ou à l’endroit)
  * 2 pts supp par couple de bouées valides sur les lignes


* **MANCHES A AIR** : relever les manches à air _de son équipe_
  * 5 points pour 1
  * 15 points pour les 2


* **PHARE** : allumer le phare
  * 3 points pour l'activation
  * 10 points supp s'il se déploit correctement avant la fin du match
  * (+ 2 points pour déposer le phare pendant la phase de préparation)


* **GIROUETTE** :après 25 secondes de match, vérifier la position de la girouette
  * 10 points si le robot est dans la bonne zone de mouillage à la fin du match (5 points si dans la mauvaise zone)


* **PAVILLONS** : Entre la 95 et la 100e seconde (PAS AVANT), hisser au moins 2 pavillons valides selon le code international des signaux maritimes, avec une surface utile de 30cm² minimum, à une altitude supérieure à 35 cm
  * 10 points


* **AFFICHAGE DU SCORE** : Soit écrit par l'équipe avant le match, soit dynamiquement affiché sur le robot ou le phare
  * Bonus : (0.3 x Score) -  Écart


/!\ ne pas entrer dans les ports de l'équipe adverse
