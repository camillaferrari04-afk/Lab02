class Dictionary:
    def __init__(self, dictionary:dict):
        self.dictionary=dictionary

    def addWord(self, word:list):
        da_aggiungere = [word[0]]
        for i in range(1, len(word)):
            trovato = False
            for j in self.dictionary.keys():
                if word[0].lower() ==j and word[i].lower() in self.dictionary[j]:
                    trovato=True
                elif word[0].lower() ==j:
                    self.dictionary[j].append(word[i])
                    trovato = True
                    da_aggiungere.append(word[i])
            if not trovato:
                self.dictionary[word[0].lower()]=[word[i]]
                da_aggiungere.append(word[i])

        if word is not None:
            try:
                infile = open("dictionary.txt", "a")
                for i in range(1, len(da_aggiungere)):
                    infile.write(f"\n{da_aggiungere[0].lower()} {da_aggiungere[i].lower()}")
                infile.close()
            except FileNotFoundError:
                print("File non trovato")
        return word

    def translate(self, word:str):
        translation=None
        if word in self.dictionary:
            translation=self.dictionary[word]
        return translation

    def printall(self):
        for i in self.dictionary.keys():
            print(f"{i}: {self.dictionary[i]}")

    def translateWordWildCard(self, query:str):
        cardpos=query.index("?")
        translations=[]
        for i in self.dictionary.keys():
            if len(query)==len(i):
                if query[0:cardpos] == i[0:cardpos] and query[cardpos+1:len(query)] == i[cardpos+1:len(query)]:
                        translations.append(i)
        return translations