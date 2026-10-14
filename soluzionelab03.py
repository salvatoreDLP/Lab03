class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"{self.codice}, {self.tipo}, {self.marca}, {self.anno_acquisto}, {self.valore:.2f} euro"


class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.codice}, {self.data}, {self.id_strumento}, {self.cognome_allievo}"


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []
        self.prossimo_strumento = 1
        self.prossimo_prestito = 1

    def carica_file_strumenti(self, file_path):
        self.strumenti = []
        self.prossimo_strumento = 1

        file = open(file_path, "r", encoding="utf-8")

        for riga in file:
            dati = riga.strip().split(",")

            if len(dati) != 5:
                continue

            codice = dati[0]
            tipo = dati[1]
            marca = dati[2]
            anno = int(dati[3])
            valore = float(dati[4])

            strumento = Strumento(codice, tipo, marca, anno, valore)
            self.strumenti.append(strumento)

            numero = int(codice[1:])
            if numero >= self.prossimo_strumento:
                self.prossimo_strumento = numero + 1

        file.close()

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        codice = "S" + str(self.prossimo_strumento)
        self.prossimo_strumento += 1

        strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(strumento)

        return strumento

    def strumenti_ordinati_per_marca(self):
        return sorted(self.strumenti, key=lambda strumento: strumento.marca.lower())

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        trovato = False

        for strumento in self.strumenti:
            if strumento.codice == id_strumento:
                trovato = True
                break

        if not trovato:
            raise Exception("Strumento non presente")

        # controllo se e' gia in prestito
        for prestito in self.prestiti:
            if prestito.id_strumento == id_strumento:
                raise Exception("Strumento gia in prestito")

        codice = "P" + str(self.prossimo_prestito)
        self.prossimo_prestito += 1

        prestito = Prestito(codice, data, id_strumento, cognome_allievo)
        self.prestiti.append(prestito)

        return prestito

    def termina_prestito(self, id_prestito):
        for prestito in self.prestiti:
            if prestito.codice == id_prestito:
                self.prestiti.remove(prestito)
                return

        raise Exception("Prestito non trovato")
