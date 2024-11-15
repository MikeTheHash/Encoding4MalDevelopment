# Author: MikeTheHash
# Date: 22/08/2024

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

            "!": ";HoFinitoLeIdeeLOL",
            "|": ";QuantiCaratteriMancano?",
            "$": ";NonStoDelirandoGiuro",
            "#": ";OkayForse",
            "'": ";CreareStaCodifica_èStataUnaSfida",
            "\"": ";UnaSfidaControLaMiaSaluteMentaleLOL", 
            "/": ";SoRetardato",
            "\\": ";WlaFiga",
            "<": ";boh_nonSoCheScrivere",
            ">": ";meowMEOW_BITCH",
            ")": ";miuw", 
            "(": ";alfa",
            "&": ";SIUMTATTICOSO", 
            "%": ";NoAllAlcolismo", # ho più birra che sangue in corpo btw

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

            ";HoFinitoLeIdeeLOL": "!",
            ";QuantiCaratteriMancano?": "|",
            ";NonStoDelirandoGiuro": "$",
            ";OkayForse": "#",
            ";CreareStaCodifica_èStataUnaSfida": "'",
            ";UnaSfidaControLaMiaSaluteMentaleLOL": "\"",
            ";SoRetardato": "/",
            ";WlaFiga": "\\",
            ";boh_nonSoCheScrivere": "<",
            ";meowMEOW_BITCH": ">",
            ";miuw": ")",
            ";alfa": "(",
            ";SIUMTATTICOSO": "&",
            ";NoAllAlcolismo": "%" # ho più birra che sangue in corpo btw

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
