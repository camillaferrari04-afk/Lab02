from dictionary import Dictionary

class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        action=input("-------------------------- \n "
              "Translator Alien-Italian \n"
              "--------------------------\n"
              "1. Aggiungi nuova parola \n"
              "2. Cerca una traduzione\n"
              "3. Cerca con wildcard\n"
              "4. Stampa tutto il Dizionario\n"
              "5. Exit\n"
              "--------------------------\n"
              "\n")
        if action.isdigit():
            if 1 <= int(action) <= 5:
                return int(action)
        print("Valore non valido")
        return None

    #crea dizionario parola_aliena:traduzione
    def loadDictionary(self, dicti:str) ->Dictionary:
        dictionary=dict()
        try:
            infile=open(dicti,"r")
            for line in infile:
                line=line.strip().split()
                if dictionary.get(line[0], None) != None:
                    dictionary[line[0]].append(line[1])
                else:
                    dictionary[line[0].lower()]=[line[1].lower()]

        except FileNotFoundError:
            print("File non trovato")

        dictionary_object=Dictionary(dictionary)
        return dictionary_object

    def handleAdd(self, entry:list, dictionary:Dictionary):
        words=dictionary.addWord(entry)
        return words


    def handleTranslate(self, entry:str, dictionary:Dictionary):
        translation=dictionary.translate(entry.lower())
        return translation

    def handleWildCard(self,query:str, dictionary:Dictionary):
        translation = dictionary.translateWordWildCard(query)
        return translation
