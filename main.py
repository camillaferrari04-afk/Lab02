import translator as tr

t = tr.Translator()


while True:

    txtIn=t.printMenu()

    if int(txtIn) == 5:
        break
    else:
        dictionary=t.loadDictionary("dictionary.txt")

        if int(txtIn) == 1:
            print("Ok, quale parola devo aggiungere?")
            while True:
                txtIn = input()
                words=txtIn.split()
                if len(words)>=2 and [words[i].isalpha() for i in range(len(words))]:
                    words=t.handleAdd(words, dictionary)
                    break
                else:
                    print("Parola non valida")

            for i in range(1,len(words)):
                print(f"Aggiunta parola '{words[0]}' con traduzione '{words[i]}'")

        elif int(txtIn) == 2:
            print("Ok, quale parola devo cercare?")
            while True:
                txtIn = input()
                if txtIn.isalpha():
                    translation = t.handleTranslate(txtIn, dictionary)
                    break
                else:
                    print("Parola non valida")

            if translation is None:
                print("Parola non presente nel dizionario")
            else:
                print(f"La traduzione della parola è '{translation}'")
        elif int(txtIn) == 3:
            print("Ok, quale parola devo cercare?")
            while True:
                txtIn = input()
                query=txtIn.lower()
                if len(query.split("?"))==2:
                    translation = t.handleWildCard(query, dictionary)
                    break
                else:
                    print("Parola non valida")

            if len(translation)==0:
                print("Parola non presente nel dizionario")
            else:
                for i in translation:
                    print(f"La traduzione della parola {i} è '{t.handleTranslate(i, dictionary)}'")
        elif int(txtIn) == 4:
            dictionary.printall()