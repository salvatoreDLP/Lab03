from deposito_strumenti import DepositoStrumenti
from datetime import datetime


def menu():
    print("\n--- MENU DEPOSITO STRUMENTI ---")
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento (da tastiera)")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Esci")
    return input("Scegli un'opzione >> ")


def main():
    deposito = DepositoStrumenti("Deposito Strumenti Civico", "Alessandro Visconti")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ")
            deposito.responsabile = nuovo_responsabile
            print("Responsabile modificato")

        elif scelta == "2":
            file_path = input("Inserisci il path del file da caricare: ").strip()

            try:
                deposito.carica_file_strumenti(file_path)
                print("Strumenti caricati")
            except FileNotFoundError:
                print("File non trovato")
            except ValueError:
                print("Errore nei dati del file")

        elif scelta == "3":
            tipo = input("Tipo di strumento: ")
            marca = input("Marca: ")

            try:
                anno = int(input("Anno di acquisto: "))
                valore = float(input("Valore: "))
            except ValueError:
                print("Anno o valore non valido")
                continue

            strumento = deposito.aggiungi_strumento(tipo, marca, anno, valore)
            print("Strumento aggiunto:", strumento)

        elif scelta == "4":
            lista = deposito.strumenti_ordinati_per_marca()

            for strumento in lista:
                print(strumento)

        elif scelta == "5":
            id_strumento = input("ID strumento: ")
            cognome = input("Cognome allievo: ")
            data = datetime.now().date()

            try:
                prestito = deposito.nuovo_prestito(data, id_strumento, cognome)
                print("Prestito creato:", prestito)
            except Exception as errore:
                print(errore)

        elif scelta == "6":
            id_prestito = input("ID prestito da terminare: ")

            try:
                deposito.termina_prestito(id_prestito)
                print("Prestito terminato")
            except Exception as errore:
                print(errore)

        elif scelta == "7":
            print("Uscita dal programma")
            break

        else:
            print("Scelta non valida")


if __name__ == "__main__":
    main()
