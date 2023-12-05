import datetime
import locale
import sys

# Imposta la localizzazione italiana
locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')

# Lista delle festività italiane (da aggiornare per gli anni successivi)
festività_italiane = [
    (1, 1),    # Capodanno
    (6, 1),    # Epifania
    (4, 4),    # Pasqua
    (4, 5),    # Pasquetta
    (5, 1),    # Festa dei Lavoratori
    (6, 2),    # Festa della Repubblica
    (8, 15),   # Assunzione di Maria
    (11, 1),   # Tutti i Santi
    (12, 8),   # Immacolata Concezione
    (12, 25),  # Natale
    (12, 26),  # Santo Stefano
]

def calcola_giorni_lavorativi(inizio, giorni_da_aggiungere):
    giorni_lavorativi = []
    giorno_corrente = inizio

    while giorni_da_aggiungere >= 1:
        giorno_corrente += datetime.timedelta(days=1)

        # Controlla se il mese e il giorno corrente sono presenti nella lista delle festività italiane
        if giorno_corrente.weekday() < 5 and (giorno_corrente.month, giorno_corrente.day) not in festività_italiane:
            giorni_lavorativi.append(giorno_corrente)
            giorni_da_aggiungere -= 1

    return giorni_lavorativi

def calcola_giorni_lavorativi_passati(inizio, giorni_da_sottrarre):
    giorni_lavorativi = []
    giorno_corrente = inizio

    while giorni_da_sottrarre >= 1:
        giorno_corrente -= datetime.timedelta(days=1)

        # Controlla se il mese e il giorno corrente sono presenti nella lista delle festività italiane
        if giorno_corrente.weekday() < 5 and (giorno_corrente.month, giorno_corrente.day) not in festività_italiane:
            giorni_lavorativi.insert(0, giorno_corrente)  # Inserisci in testa per mantenere l'ordine cronologico
            giorni_da_sottrarre -= 1

    return giorni_lavorativi

if __name__ == "__main__":
    while True:
        while True:
            try:
                # Chiedi all'utente di inserire la data
                data_str = input("Inserisci la data (DD/MM/YYYY): ")
                data = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
                break  # Esci dal loop interno se la data è stata inserita correttamente
            except ValueError:
                print("Errore nel formato della data.")
                print("Arrivederci.")
                sys.exit()

        # Chiedi all'utente se vuole aggiungere o sottrarre giorni lavorativi
        operazione = input("Vuoi aggiungere o sottrarre giorni lavorativi? (1/2): ").lower()

        if operazione == "1":
            giorni_da_aggiungere = int(input("Quanti giorni lavorativi vuoi aggiungere? "))
            giorni_lavorativi = calcola_giorni_lavorativi(data, giorni_da_aggiungere)
        elif operazione == "2":
            giorni_da_sottrarre = int(input("Quanti giorni lavorativi vuoi sottrarre? "))
            giorni_lavorativi = calcola_giorni_lavorativi_passati(data, giorni_da_sottrarre)
        else:
            print("Operazione non valida. Arrivederci.")
            sys.exit()

        print(f"Risultato dopo {operazione} {abs(giorni_da_aggiungere if operazione == '1' else giorni_da_sottrarre)} giorni lavorativi da {data.strftime('%d/%m/%Y')}:")
        for giorno in giorni_lavorativi:
            print(giorno.strftime('%d/%m/%Y'))
