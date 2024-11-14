#shellcode = "\xfc\x48\x83\xe4\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48\x01\xd0\x8b\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01\xd0\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56\x48\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x48\x01\xd0\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48\x8b\x12\xe9\x57\xff\xff\xff\x5d\x48\xba\x01\x00\x00\x00\x00\x00\x00\x00\x48\x8d\x8d\x01\x01\x00\x00\x41\xba\x31\x8b\x6f\x87\xff\xd5\xbb\xf0\xb5\xa2\x56\x41\xba\xa6\x95\xbd\x9d\xff\xd5\x48\x83\xc4\x28\x3c\x06\x7c\x0a\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00\x59\x41\x89\xda\xff\xd5\x63\x61\x6c\x63\x2e\x65\x78\x65\x00"

def encode(text):
    try:
        encoding_map = {
            "a": ";EDDAI",
            "b": ";FROCIO",
            "c": ";skks",
            "d": ";stocazzum",
            "e": ";miau",
            "f": ";gatto",
            "g": ";shell",
            "h": ";cazzarola",
            "i": ";azzo",
            "j": ";bau",
            "k": ";MaNonLoSoHoFinitoLeParoleRandomicheDaMettere",
            "l": ";gronc",
            "m": ";releone",
            "n": ";fuckmepls",
            "o": ";milliseconds",
            "p": ";mare",
            "q": ";lago",
            "r": ";straykids",
            "s": ";alfabeto",
            "t": ";droga",
            "u": ";eldenring",
            "v": ";hollowknight",
            "w": ";hollow",
            "x": ";yz",
            "y": ";gattinibellissimi",
            "z": ";sigmeyer",

            "A":";elikoper",
            "B":";JELIKOPETER",
            "C":";wlattrocca",
            "D":";wigattini",
            "E":";hex",
            "F":";GGH",
            "G":";Lll",
            "H":";miuwww",
            "I":";motard",
            "J":";patate",
            "K":";figosaLaCappa",
            "L":";nonsoaltreparolepercodificare",
            "M":";pippo",
            "N":";PippoBaudo",
            "O":";letteraStramba",
            "P":";pIsForPoppe",
            "Q":";quaderno",
            "R":";baubaubaumiao",
            "S":";StandsForStrunz",
            "T":";voglioungatto",
            "U":";wleCANNE",
            "V":";FR",
            "W":";ProtocolloTCP",
            "X":";mutande",
            "Y":";hofinitoleparole",
            "Z":";eStatoUnPartoTirareCosiTanteParoleRandomiche",

            " ": "_",
            "=": ";FUNZIONA",
            ".": ";DAJECAZZOVAI",
            "[": ";LeonardoEGAY",
            "]": ";TantoGay",
            ":": ";Gayone",
            ";": ";<>",

            "1": ";KkA",
            "2": ";aAa", 
            "3": ";hhH", 
            "4": ";meOWWWWWW",
            "5": ";AAAAAAAA",
            "6": ";SEX",
            "7": ";SIVENSTEVEN",
            "8": ";NumberOfStrayKids",
            "9": ";CazzumNine",
            "0": ";PaliNonPresiDaLeonardo"
        }

        encoded_text = ""
        for char in text:
            encoded_text += encoding_map.get(char, char)  

        return encoded_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def decode(encoded_text):
    try:
        # Define a dictionary mapping each encoded string to its original character
        decoding_map = {
            ";EDDAI": "a",
            ";FROCIO": "b",
            ";skks": "c",
            ";stocazzum": "d",
            ";miau": "e",
            ";gatto": "f",
            ";shell": "g",
            ";cazzarola": "h",
            ";azzo": "i",
            ";bau": "j",
            ";MaNonLoSoHoFinitoLeParoleRandomicheDaMettere": "k",
            ";gronc": "l",
            ";releone": "m",
            ";fuckmepls": "n",
            ";milliseconds": "o",
            ";mare": "p",
            ";lago": "q",
            ";straykids": "r",
            ";alfabeto": "s",
            ";droga": "t",
            ";eldenring": "u",
            "hollowknight": "v",
            "hollow": "w",
            ";yz": "x",
            ";gattinibellissimi": "y",
            ";sigmeyer": "z",

            ";elikoper": "A",
            ";JELIKOPETER": "B",
            ";wlattrocca": "C",
            ";wigattini": "D",
            ";hex": "E",
            ";GGH": "F",
            ";Lll": "G",
            ";miuwww": "H",
            ";motard": "I",
            ";patate": "J",
            ";figosaLaCappa": "K",
            ";nonsoaltreparolepercodificare": "L",
            ";pippo": "M",
            ";PippoBaudo": "N",
            ";letteraStramba": "O",
            ";pIsForPoppe": "P",
            ";quaderno": "Q",
            ";baubaubaumiao": "R",
            ";StandsForStrunz": "S",
            ";voglioungatto": "T",
            ";wleCANNE": "U",
            ";FR": "V",
            ";ProtocolloTCP": "W",
            ";mutande": "X",
            ";hofinitoleparole": "Y",
            ";eStatoUnPartoTirareCosiTanteParoleRandomiche": "Z",

            "_": " ",
            ";FUNZIONA": "=",
            ";DAJECAZZOVAI": ".",
            ";LeonardoEGAY": "[",
            ";TantoGay": "]",
            ";Gayone": ":",
            ";<>": ";",

            ";KkA": "1",
            ";aAa": "2",
            ";hhH": "3",
            ";meOWWWWWW": "4",
            ";AAAAAAAA": "5",
            ";SEX": "6",
            ";SIVENSTEVEN": "7",
            ";NumberOfStrayKids": "8",
            ";CazzumNine": "9",
            ";PaliNonPresiDaLeonardo": "0"
        }

        # Ensure longer encoded strings are checked first
        sorted_keys = sorted(decoding_map.keys(), key=len, reverse=True)
        
        # Start decoding the encoded text
        decoded_text = encoded_text

        for key in sorted_keys:
            decoded_text = decoded_text.replace(key, decoding_map[key])

        return decoded_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

print("Encode: 1\nDecode: 2")
var = input("Select >>> ")
if(var == "1"):
    ivar = input("text >>> ")
    print(encode(ivar))
else:
    ivar1 = input("text >>> ")
    print(decode(ivar1))
