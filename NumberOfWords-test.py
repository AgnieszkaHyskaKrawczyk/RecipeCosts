vstup = open('praha.txt', encoding='utf-8')
radky = [radek.split('\t') for radek in vstup]
vstup.close()
for radek in radky:
  print(radek)
#print(radky)