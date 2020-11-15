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