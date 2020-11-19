Génération des données:

La génération prend moins d'une minute pour 

```bash
(.env) clem@mobius:~/dev/ballons$ time python gen_data.py --nb_parents 5 -f data/2-5-5-100000.dat 
real	0m33,494s
user	0m1,752s
sys	0m1,377s
clem@mobius:~/dev/ballons$ python gen_data.py --nb_parents 4 --nb_iterations 1000000 > data/2-4-5-1000000.dat
clem@mobius:~/dev/ballons$ python gen_data.py --nb_parents 3 --nb_iterations 1000000 > data/2-3-5-1000000.dat
clem@mobius:~/dev/ballons$ python gen_data.py --nb_parents 2 --nb_iterations 1000000 > data/2-2-5-1000000.dat
```

Génération des figures séparées:

```bash
(.env) clem@mobius:~/dev/ballons$ python mkplot.py -f data/2-5-5-1000000.dat
(.env) clem@mobius:~/dev/ballons$ python mkplot.py -f data/2-4-5-1000000.dat
(.env) clem@mobius:~/dev/ballons$ python mkplot.py -f data/2-3-5-1000000.dat
(.env) clem@mobius:~/dev/ballons$ python mkplot.py -f data/2-2-5-1000000.dat
```

Génération de la comparison:

```bash
python mkstacked_plots.py
```




# Rust version

```
cargo build
./target/release/multiple_games --nb_players 2  --nb_parents 5 --nb_cards 5 --nb_iterations 10000000 > data2/2-5-5-10000000.json
source .env/bin/activate
(.env) clem@mobius:~/dev/ballons$ python3 mk_rs_plot.py -f /home/clem/dev/ballons/data2/2-5-5-100000.json
```


Énumération manuelle des mains possibles:

11111
2111
311
41
5
221
32

Dénombrement des différentes mains:

https://perso.univ-rennes1.fr/philippe.roux/enseignement/proba1/exo762sol.pdf
