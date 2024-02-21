import random

def vali_sõna():
    with open("sõnad.txt", "r", encoding="utf-8") as fail:
        sõnad = fail.readlines()
    return random.choice(sõnad).strip().lower()

def näita_sõna(sõna, arvatud_tähed):
    kuvatav = ""
    for täht in sõna:
        if täht in arvatud_tähed:
            kuvatav += täht + " "
        else:
            kuvatav += "_ "
    return kuvatav.strip()

def kontrolli_arvamust(sõna, arvatud_täht):
    positsioonid = []
    for i in range(len(sõna)):
        if sõna[i] == arvatud_täht:
            positsioonid.append(i)
    return positsioonid

def main():
    sõna = vali_sõna()
    arvatud_tähed = []
    katseid = 6

    print("Tere tulemast sõnamängu!")
    print("Teil on 6 katset sõna arvamiseks.")
    print(näita_sõna(sõna, arvatud_tähed))

    while katseid > 0:
        arvamus = input("Sisestage täht: ").lower()
        if len(arvamus) != 1 or not arvamus.isalpha():
            print("Palun sisestage üks täht.")
            continue

        if arvamus in arvatud_tähed:
            print("Te olete selle tähe juba arvanud.")
            continue

        arvatud_tähed.append(arvamus)
        positsioonid = kontrolli_arvamust(sõna, arvamus)

        if positsioonid:
            print(f"Täht '{arvamus}' on sõnas!")
            for pos in positsioonid:
                print(f"Täht '{arvamus}' on positsioonil {pos + 1}.")
        else:
            print(f"Täht '{arvamus}' ei ole sõnas.")
            katseid -= 1

        if set(arvatud_tähed) == set(sõna):
            print("Palju õnne! Te arvasite sõna ära:", sõna)
            break

        print("Katseid jäänud:", katseid)
        print(näita_sõna(sõna, arvatud_tähed))

    else:
        print("Vabandust, te jooksite katsetest välja. Sõna oli:", sõna)

if __name__ == "__main__":
    main()



