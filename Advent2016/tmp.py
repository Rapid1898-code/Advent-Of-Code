import re
s = "bot 13 gives low to bot 4 and high to bot 167"
erg = [m.start() for m in re.finditer('bot', s)]
print(erg)



