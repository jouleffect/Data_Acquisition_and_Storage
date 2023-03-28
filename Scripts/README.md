# Documentazione



#### Questa cartella contiene:

- La sottocartella "***htm***", con i file htm.
- Lo script python "***parser_dati_sulla_procedura.py***", che acquisisce il contenuto relativo dai file della cartella *htm* e lo salva nel file csv "*Dati sulla procedura.csv*".
- Lo script python "***parser_dati_generali_del_lotto.py***",  che acquisisce il contenuto relativo dai file della cartella *htm* e lo salva nel file csv "*Dati generali del lotto.csv*".
- Lo script python "***geo.py***", che rileva le coordinate geografiche degli indirizzi contenuti nel file *parser_dati_generali_del_lotto.py*, mediante le API *Nominatim*, salvandole nel file csv "*coordinate.csv*".
- Lo script python "***arricchimento.py***", che unisce al contenuto dei file *Dati generali del lotto.csv* i rispettivi dati del file *coordinate.csv*, salvando tutto nel file "*Dati generali del lotto con coordinate.csv*" e nel file sqlite "*dati_generali.db*".
- Lo script bash "***start.sh***", che avvia tutti gli script menzionati sopra. (richiede i permessi di esecuzione).
- Questo file README.
