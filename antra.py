# Antra užduotis
# Sukurti funkciją, kuri priimtų tuple ir grąžintų kitą tuple,
# tik su pašalintais dublikatais. Eiliškumas elementų turi išlikti toks pats:
# Pvz: jeigu funkcija priima (1, 2, 3, 4, 3, 2, 1) tuple, tai turėtų grąžinti (1, 2, 3, 4)
# Paduoti tuple į funkciją (reikšmes sugalvokite patys) ir išspausdinti funkcijos rezultatą


def funkcija(tuples):
 nesikartojantys = tuple(set(tuples))
 return nesikartojantys


sarasas = (1, 2, 3, 4, 4, 4, 4, 6, 6, 6, 6, 3, 2, 1)
result = funkcija(sarasas)
print(result)