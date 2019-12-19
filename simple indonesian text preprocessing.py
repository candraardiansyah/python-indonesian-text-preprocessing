import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def main():
    datatest='Kalimat 4 kata ini   adalah sebagai contoh!!!'
    result=preprocessing(datatest)
    print(result)

def preprocessing(d):
    d = d.lower()     
    d = re.sub(r'[^A-Za-z]', ' ', d)    
    d = d.split()    
    stoplist = (open('tala-stopword.txt', 'r').read().replace('\n', ' ')).split(" ")
    d = [i for i in d if i not in stoplist]    
    d = [i for i in d if len(i)>1]    
    d = [stemmer.stem(i) for i in d]
    return d

if __name__ == "__main__":
    main()