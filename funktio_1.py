def toinenFunktio():
    print("Ollaan toisessa funktiossa")

def tervehdi():
    print("Moi!")
    toinenFunktio()
    print("Tämä on tervehdys funktiosta")
    return

print("Ollaan pääohjelmassa")
tervehdi()
print("Ollaan takaisin pääohjelmassa")
tervehdi()
tervehdi()
print("No nyt lopulta lopetellaan")
