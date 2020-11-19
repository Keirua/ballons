# une partie avec les règles de base:

```
cargo build
./target/release/multiple_games --nb_players 2  --nb_parents 5 --nb_cards 5 --nb_iterations 10000000 > data2/2-5-5-10000000.json
source .env/bin/activate
(.env) clem@mobius:~/dev/ballons$ python3 mk_rs_plot.py -f /home/clem/dev/ballons/data2/2-5-5-10000000.json
```

![](./notes/2-5-5-10000000.png)

# Comparaison de l’influence du nombre de cartes "parent" sur la longueur des parties à 2 joueurs:

On sort les chiffres

```bash
./target/release/multiple_games --nb_players 2  --nb_parents 5 --nb_cards 5 --nb_iterations 10000000 > data2/2-5-5-10000000.json
./target/release/multiple_games --nb_players 2  --nb_parents 4 --nb_cards 5 --nb_iterations 10000000 > data2/2-4-5-10000000.json
./target/release/multiple_games --nb_players 2  --nb_parents 3 --nb_cards 5 --nb_iterations 10000000 > data2/2-3-5-10000000.json
./target/release/multiple_games --nb_players 2  --nb_parents 2 --nb_cards 5 --nb_iterations 10000000 > data2/2-2-5-10000000.json
```

On sort quelques graphiques
```bash
python3 mk_rs_plot.py -f /home/clem/dev/ballons/data2/2-2-5-10000000.json
python3 mk_rs_plot.py -f /home/clem/dev/ballons/data2/2-3-5-10000000.json
python3 mk_rs_plot.py -f /home/clem/dev/ballons/data2/2-4-5-10000000.json
python3 mk_rs_plot.py -f /home/clem/dev/ballons/data2/2-5-5-10000000.json
```

# Énumération manuelle des mains possibles:

11111
2111
311
41
5
221
32

## Dénombrement des différentes mains:

https://perso.univ-rennes1.fr/philippe.roux/enseignement/proba1/exo762sol.pdf

## Probabilité d’avoir les différentes mains

raw hand count with 1000000 hands:
{'5': 100, '14': 9426, '23': 37340, '11111': 58588, '113': 141093, '122': 283629, '1112': 469824}
{'5': 94,  '14': 9519, '23': 37610, '11111': 59149, '113': 141198, '122': 281279, '1112': 471151}
problem = quadratic convergence: having 1 more digit = 100 times more iterations

# most frequent hands
```
python3 gen_hand_structure_pie.py
```

'1112', '122', '113', '11111', '23', '14', '5'

probabilité de les rencontrer:

5, 0.0079
14, 0.9387
23, 3.7784
11111, 5.8973
113, 14.0978
122, 28.2434
1112, 47.0365

![](./notes/piechart.png)

# Heatmap avec les probabilités de victoire en fonction des différentes rencontres de mains ?