# une partie avec les règles de base:

```
cargo build
./target/release/multiple_games --nb_players 2  --nb_parents 5 --nb_cards 5 --nb_iterations 10000000 > data2/2-5-5-10000000.json
source .env/bin/activate
(.env) clem@mobius:~/dev/ballons$ python3 mk_rs_plot.py -f /home/clem/dev/ballons/data2/2-5-5-100000.json
```

![](./notes/2-5-5-10000000.png)

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

most frequent hands:
'1112', '122', '113', '11111', '23', '14', '5'