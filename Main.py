import random


alphabet = ""

def add_letter(n, t):
    global alphabet
    for k in range(t):
        alphabet = alphabet + n

#or k in range(27):
#    print("add_letter(\"dbb\", 1)")

add_letter("a", 1)
add_letter("b", 1)
add_letter("c", 31)
add_letter("d", 1)
add_letter("e", 42)
add_letter("f", 3)
add_letter("g", 0)
add_letter("h", 11)
add_letter("i", 9)
add_letter("j", 8)
add_letter("k", 6)
add_letter("l", 4)
add_letter("m", 4)
add_letter("n", 4)
add_letter("o", 23)
add_letter("p", 0)
add_letter("q", 0)
add_letter("r", 9)
add_letter("s", 9)
add_letter("t", 1)
add_letter("u", 7)
add_letter("v", 1)
add_letter("w", 6)
add_letter("x", 31)
add_letter("y", 1)
add_letter("z", 1)

np = "wscgflbxq"

def not_first_letter(l, index):
    r = True
    
    if l in np and index == 0:
        r = False
    return r

def first_valid_letter(config):
    r = " "
    for i in range(100):
        m = config[random.randint(0, len(config)-1)]
        
        if not_first_letter(m, 0) == True:
            r = m
            
    return r

def compatible_con(k,v):
    a = v
    l = k
    r = True
    if a == "w" and l == "c":
        r = False
    if a == "w" and l == "h":
        r = False
    if a == "h" and l == "c":
        r = False
    if a == "f" and l == "s":
        r = False
    if a == "h" and l == "r":
        r = False
    if a == "f" and l == "w":
        r = False
    if a == "w" and l == "b":
        r = False
    if a == "b" and l == "h":
        r = False
    if a == "w" and l == "c":
        r = False
    if a == "r" and l == "p":
        r = False
    if a == "h" and l == "a":
         r = False
    if a == "h" and l == "d":
        r = False
    if a == "v" and l == "w":
        r = False
    if a == "d" and l == "z":
        r = False
    if a == "r" and l == "p":
        r = False
    if a == "h" and l == "v":
        r = False
    if a == "d" and l == "w":
        r = False
    if a == "w" and l == "h":
        r = False
    if a == "w" and l == "l":
        r = False
    if a == "h" and l == "c":
        r = False
    if a == "h" and l == "c":
        r = False
    if a == "w" and l == "s":
        r = False
    if a == "e" and l == "w":
        r = False
    if a == "h" and l == "c":
        r = False
    if a == "c" and l == "z":
        r = False
    if a == "s" and l == "z":
        r = False
    if a == "w" and l == "r":
        r = False
    if a == "j" and l == "c":
        r = False
    if a == "j" and l == "r":
        r = False
    if a == "c" and l == "f":
        r = False
    if a == "c" and l == "h":
        r = False
    if a == "w" and l == "l":
        r = False
    if a == "h" and l == "p":
        r = False
    if a =="w" and l == "x":
        r = False
    if a == "s" and l == "c":
        r = False
    if a == "c" and l == "w":
        r = False
    if a == "h" and l == "s":
        r = False
    #print(a, l)
    return r

def generate_word(config, size):
    r = "" + first_valid_letter(config)
        
    last_letter = ""
    
    for i in range(size):
        rl = config[random.randint(0, len(config)-1)]
        
        #print(r[len(r)-1])
        if rl not in r and not_first_letter(rl, i) and compatible_con(rl, r[len(r)-1]):
            r = r + rl
            last_letter = rl
            
   
    return r



random.seed(6314)


def translate_seed(word):
    r = ""
    rn = 6314
    
    global alphabet
    
    for k in word:
        rn = rn + ord(k)
    
    random.seed(rn)
    return generate_word(alphabet, 6)

print(translate_seed("ar"))

def translate_sentence(text):
    
    r = ""
    
    for word in text.split(" "):
        r = r + translate_seed(word) + " ";
    
    return r
    
    
    
    
# cheio             Ec
# perfeito         Herans
# vazio             Hixwne
# imperfeito    Ejhxna
# escrito          Juoeix
# falar              Joeslx
# falar              Joeslx
# disse             Eomcs
# dito               Joxcer
# em                 Hnec
# vivo               Ejowm
# morto            Hec
# vi                    Hoxe
# visto              Hecox
# ar                   Exukb
# fazer              Eomcs
# usar               Erxij
# mover            Hixwne
# andar             Kecxj
# parar              Rjxoi
# parado           Uxoj
# atirar              Rohxc
# estou             Kujec
# oi                   He
# tchau             Ixce
# isso               Enxhwk
# aqui               Joxcer
# la                   Exicor
# de                  Oexisf
# da                  icuwk
# dos                Eowu
# das                Okcixe
# nos                Merxn
# nas                Vocefd
# no                  Excu
# na                  Efh
# em                 Hnec
# estando        Ensj
# é                    Kesnix
# ê                    Ohlcn   ou   Jecy
# foi                  Ecxr
# ar                   Exkb


resp = translate_sentence("uma doce raposa foi veleiar em um campo verde cheio de rosas camponeses")

print()
print("texto: uma doce raposa foi veleiar em um campo verde cheio de rosas camponeses")
print("")

print("traduzido: " + resp)

#print(translate_sentence("ola mundo"))
