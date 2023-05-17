# Trečia užduotis
#
# Sukurti programą, kuri saugotų duomenis apie darbuotojus Pickle faile bei atliktų su duomenimis įvairius
# veiksmus:
# Sukurti funkciją, kuri sukuria darbuotoją (vardas, amžius, darbo pozicija) ir jį grąžina
# Sukurti funkciją, kuri išsaugo darbuotojus į failą (pickle)
# Sukurti funkciją, kuri užkrauna darbuotojus iš failo ir juos grąžina (pickle)
# Panaudoti sukūrimo funkciją kelis kartus su kokiomis norite reikšmėmis
# Panaudoti išsaugojimą į failą funkciją
# Panaudoti užkrovimo iš failo funkciją
# Atspausdinkite užkrautus iš failo duomenis


def sukurtas(vardas , amzius , pareigos):
    darbuotojas = {"vardas" : vardas , "amzius" : amzius , "pareigos" : pareigos}
    return darbuotojas


darbuotojas1 = sukurtas ("Pyteris" , 33 , "vadybininkas ")
darbuotojas2 =  sukurtas ("Ruunis" , 43 , "administratorius ")
darbuotojas3 =  sukurtas ("Petras" , 30 , "mechanikas ")
darbuotojas4 =  sukurtas ("Jonas" , 18 , "budelis")

# print(darbuotojas1)
# print(darbuotojas2)
# print(darbuotojas3)
# print(darbuotojas4)


darbuotojai = [darbuotojas1, darbuotojas2, darbuotojas3, darbuotojas4]


import pickle



"""????????? darbuotojas = sukurtas ????????"""

with open("darbuotojai.pkl", "wb") as pickle_out:
    pickle.dump(darbuotojai, pickle_out)

    with open("darbuotojai.pkl", "rb") as pickle_in:
       darbuotojai = pickle.load(pickle_in)

print(darbuotojai)

""" NEGALIU ATIDARYTI DABUOTOJAI.PKL NET RANKINIU BUDU """


