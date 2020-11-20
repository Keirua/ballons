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
time python3 gen_hand_structure.py -p 5 -b 5 -i 1000000
{'5': 79, '14': 9387, '23': 37784, '11111': 58973, '113': 140978, '122': 282434, '1112': 470365}

real	0m19,588s
user	0m19,587s
sys	0m0,000s

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

47% des mains sont des 1112
96% des mains sont des 1112, 122, 113, 11111

![](./notes/piechart.png)

# Heatmap avec les probabilités de victoire en fonction des différentes rencontres de mains ?

Certaines rencontres sont impossibles:
 - 5 vs 11111
Certaines sont très peu probables, donc il faut aider le destin pour en avoir:
 - 5 vs 11111

Dans une première approche, on génère

On récupère les comptes de rencontres et de victoires:

```bash
time python3 gen_hand_heatmap.py -p 5 -b 5 -i 10000000
{'1112': {'1112': [1096634, 2264360], '122': [534765, 1316073], '113': [199703, 633220], '11111': [169968, 292299], '23': [43289, 163734], '14': [5431, 37203], '5': [7, 314]}, '122': {'1112': [748418, 1317176], '122': [387001, 793237], '113': [159508, 408524], '11111': [108201, 163988], '23': [36298, 109777], '14': [5929, 30139], '5': [30, 379]}, '113': {'1112': [420634, 632480], '122': [242647, 409511], '113': [106885, 217067], '11111': [54222, 72753], '23': [26445, 61486], '14': [4603, 16608], '5': [21, 175]}, '11111': {'1112': [112353, 292343], '122': [51235, 163561], '113': [17070, 72373], '11111': [18536, 38556], '23': [3447, 18062], '14': [292, 2964], '5': [0, 0]}, '23': {'1112': [118097, 163429], '122': [71744, 109826], '113': [34123, 61269], '11111': [14407, 18205], '23': [9059, 18273], '14': [1761, 5487], '5': [11, 75]}, '14': {'1112': [31439, 37283], '122': [24018, 30261], '113': [11879, 16574], '11111': [2688, 3042], '23': [3644, 5433], '14': [765, 1513], '5': [6, 25]}, '5': {'1112': [306, 318], '122': [318, 344], '113': [170, 184], '11111': [0, 0], '23': [69, 80], '14': [15, 17], '5': [0, 0]}}

real	9m57,285s
user	9m57,191s
sys	0m0,032s
```
on met ça dans plot_hand_heatmap.py:

![](notes/heatmap.png)

Le problème de cette approche, c’est qu’elle génère beaucoup de parties probables, mais les parties peu probables sont mal représentées (cf les chiffres dans `heatmap-naive.json`).
Sur ces types de parties, il y a donc moins de parties simulées, et donc les chiffres de probabilités de victoires sont moins précis.

Il faut un meilleur algorithme de génération de parties.

Cependant, pour les parties fréquentes (carré avec '1112', '122' et '113'), on a déja pas mal de parties simulées et on pourrait déjà regarder les chiffres.

Maintenant, il n’est pas nécessaire de générer tous les matchs ; seuls la moitié supérieure de la matrice des rencontres est nécessaire, l’autre peut être déduite (si a rencontre b et gagen dans x% des cas, lors de la rencontre b contre a la victoire aura lieu dans 100-x % des cas).


# Génération de toutes les mains possibles


## Nombre de mains par types de mains

il se trouve qu’il y a beaucoup de symétries et qu’il y a au final assez peu de mains différents.

Voici le nombre de mains par types de mains:

```
$ time python3 gen_every_hands.py 
11111 	1
5 		5
41 		20
32 		20
311 	60
221 	60
2111 	120
```

Au total, 286 mains différentes, réparties sur 7 structures différentes, existent

 - genération de toutes les mains
 - genération de toutes les rencontres possibles
 - création d’une partie à 2 joueurs avec des mains sélectionnées


## Régénération des chiffres de probabilités de victoire, avec plus de chiffres pour les rencontres peu fréquentes

```bash
 time python3 gen_hand_heatmap_uniform.py --nb_iterations 10000
{'11111': {'11111': [4753, 10000], '5': [0, 0], '41': [1081, 10000], '32': [1946, 10000], '311': [2444, 10000], '221': [3111, 10000], '2111': [3815, 10000]}, '5': {'11111': [0, 0], '5': [4945, 10000], '41': [7750, 10000], '32': [8633, 10000], '311': [8956, 10000], '221': [9323, 10000], '2111': [9529, 10000]}, '41': {'11111': [8790, 10000], '5': [2229, 10000], '41': [4888, 10000], '32': [6680, 10000], '311': [7164, 10000], '221': [7926, 10000], '2111': [8386, 10000]}, '32': {'11111': [7912, 10000], '5': [1232, 10000], '41': [3352, 10000], '32': [4963, 10000], '311': [5653, 10000], '221': [6520, 10000], '2111': [7218, 10000]}, '311': {'11111': [7383, 10000], '5': [979, 10000], '41': [2808, 10000], '32': [4244, 10000], '311': [4839, 10000], '221': [5949, 10000], '2111': [6602, 10000]}, '221': {'11111': [6675, 10000], '5': [637, 10000], '41': [2025, 10000], '32': [3394, 10000], '311': [4024, 10000], '221': [4804, 10000], '2111': [5714, 10000]}, '2111': {'11111': [5808, 10000], '5': [461, 10000], '41': [1533, 10000], '32': [2636, 10000], '311': [3208, 10000], '221': [4080, 10000], '2111': [4886, 10000]}}

real	0m36,663s
user	0m36,661s
sys	0m0,000s
```

En fusionnant les résultats précédents afin de ne pas avoir à recalculer trop les parties très fréquentes qui ont déjà beaucoup de chiffres:

```bash
time python3 gen_hand_heatmap_uniform.py --nb_iterations 100000
{'2111': {'2111': [1096634, 2264360], '221': [534765, 1316073], '311': [199703, 633220], '11111': [169968, 292299], '32': [69997, 263734], '41': [21130, 137203], '5': [4297, 100314]}, '221': {'2111': [748418, 1317176], '221': [387001, 793237], '311': [159508, 408524], '11111': [108201, 163988], '32': [70114, 209777], '41': [25779, 130139], '5': [6455, 100379]}, '311': {'2111': [420634, 632480], '221': [242647, 409511], '311': [106885, 217067], '11111': [128528, 172753], '32': [69617, 161486], '41': [32812, 116608], '5': [9761, 100175]}, '11111': {'2111': [112353, 292343], '221': [82382, 263561], '311': [40647, 172373], '11111': [66401, 138556], '32': [22986, 118062], '41': [11305, 102964], '5': [0, 0]}, '32': {'2111': [118097, 163429], '221': [136920, 209826], '311': [89716, 161269], '11111': [93415, 118205], '32': [58034, 118273], '41': [35266, 105487], '5': [12623, 100075]}, '41': {'2111': [115177, 137283], '221': [103424, 130261], '311': [83104, 116574], '11111': [90862, 103042], '32': [69726, 105433], '41': [50588, 101513], '5': [22455, 100025]}, '5': {'2111': [95782, 100318], '221': [93662, 100344], '311': [90142, 100184], '11111': [0, 0], '32': [87187, 100080], '41': [77193, 100017], '5': [49855, 100000]}}

real	4m42,866s
user	4m42,708s
sys	0m0,056s
```