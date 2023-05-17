# Pirma užduotis
#
# Sukurti funkciją, kuri iš vardų sąrašo sudarytų sąrašą tik iš vardų pirmų raidžių ir tą sąrašą grąžintų:
# Pvz: paduodamas sąrašas į funkciją: [‘Jonas’, ‘Petras’, ‘Linas’], tai grąžinamas turėtų būti [‘J’, ‘P’, ‘L’]
# Paduoti vardų sąrašą į funkciją (vardus galite sugalvoti patys) ir atspausdinti funkcijos rezultatą



def funckija(sarasas):
    vardai = ['Linas', 'Petras', 'Kestas', 'Mykolas']
    naujas_sarasas = []

    for vardas in vardai:
        naujas_sarasas.append(vardas[0])

    print(naujas_sarasas)

sarasas = []
funckija(sarasas)