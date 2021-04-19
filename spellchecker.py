from spellchecker import SpellChecker

spell = SpellChecker()

misspelled = spell.unknown(['thdis','pogram','checck','misspelled','wrd'])

for word in misspelled:
    print(spell.correction(word))
