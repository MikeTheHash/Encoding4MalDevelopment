package main

import (
	"fmt"
	"strings"
)

func encode(text string) string {
	encodingMap := map[string]string{
		"a": ";EDDAI", "b": ";FROCIO", "c": ";skks", "d": ";stocazzum", "e": ";miau",
		"f": ";gatto", "g": ";shell", "h": ";cazzarola", "i": ";azzo", "j": ";bau",
		"k": ";MaNonLoSoHoFinitoLeParoleRandomicheDaMettere", "l": ";gronc", "m": ";releone",
		"n": ";fuckmepls", "o": ";milliseconds", "p": ";mare", "q": ";lago", "r": ";straykids",
		"s": ";alfabeto", "t": ";droga", "u": ";eldenring", "v": ";hollowknight", "w": ";hollow",
		"x": ";yz", "y": ";gattinibellissimi", "z": ";sigmeyer",

		"A": ";elikoper", "B": ";JELIKOPETER", "C": ";wlattrocca", "D": ";wigattini", "E": ";hex",
		"F": ";GGH", "G": ";Lll", "H": ";miuwww", "I": ";motard", "J": ";patate",
		"K": ";figosaLaCappa", "L": ";nonsoaltreparolepercodificare", "M": ";pippo", "N": ";PippoBaudo",
		"O": ";letteraStramba", "P": ";pIsForPoppe", "Q": ";quaderno", "R": ";baubaubaumiao",
		"S": ";StandsForStrunz", "T": ";voglioungatto", "U": ";wleCANNE", "V": ";FR",
		"W": ";ProtocolloTCP", "X": ";mutande", "Y": ";hofinitoleparole", "Z": ";eStatoUnPartoTirareCosiTanteParoleRandomiche",

		" ": "_", "=": ";FUNZIONA", ".": ";DAJECAZZOVAI", "[": ";LeonardoEGAY", "]": ";TantoGay",
		":": ";Gayone", ";": ";<>", "!": ";HoFinitoLeIdeeLOL", "|": ";QuantiCaratteriMancano?",
		"$": ";NonStoDelirandoGiuro", "#": ";OkayForse", "'": ";CreareStaCodifica_èStataUnaSfida",
		"\"": ";UnaSfidaControLaMiaSaluteMentaleLOL", "/": ";SoRetardato", "\\": ";WlaFiga",
		"<": ";boh_nonSoCheScrivere", ">": ";meowMEOW_BITCH", ")": ";miuw", "(": ";alfa",
		"&": ";SIUMTATTICOSO", "%": ";NoAllAlcolismo",

		"1": ";KkA", "2": ";aAa", "3": ";hhH", "4": ";meOWWWWWW", "5": ";AAAAAAAA",
		"6": ";SEX", "7": ";SIVENSTEVEN", "8": ";NumberOfStrayKids", "9": ";CazzumNine",
		"0": ";PaliNonPresiDaLeonardo",
	}

	var encodedText strings.Builder

	for _, char := range text {
		if encoded, found := encodingMap[string(char)]; found {
			encodedText.WriteString(encoded)
		} else {
			encodedText.WriteRune(char)
		}
	}

	return encodedText.String()
}

func decode(encodedText string) string {
	decodingMap := map[string]string{
		";EDDAI": "a", ";FROCIO": "b", ";skks": "c", ";stocazzum": "d", ";miau": "e",
		";gatto": "f", ";shell": "g", ";cazzarola": "h", ";azzo": "i", ";bau": "j",
		";MaNonLoSoHoFinitoLeParoleRandomicheDaMettere": "k", ";gronc": "l", ";releone": "m",
		";fuckmepls": "n", ";milliseconds": "o", ";mare": "p", ";lago": "q", ";straykids": "r",
		";alfabeto": "s", ";droga": "t", ";eldenring": "u", ";hollowknight": "v", ";hollow": "w",
		";yz": "x", ";gattinibellissimi": "y", ";sigmeyer": "z",

		";elikoper": "A", ";JELIKOPETER": "B", ";wlattrocca": "C", ";wigattini": "D", ";hex": "E",
		";GGH": "F", ";Lll": "G", ";miuwww": "H", ";motard": "I", ";patate": "J",
		";figosaLaCappa": "K", ";nonsoaltreparolepercodificare": "L", ";pippo": "M", ";PippoBaudo": "N",
		";letteraStramba": "O", ";pIsForPoppe": "P", ";quaderno": "Q", ";baubaubaumiao": "R",
		";StandsForStrunz": "S", ";voglioungatto": "T", ";wleCANNE": "U", ";FR": "V",
		";ProtocolloTCP": "W", ";mutande": "X", ";hofinitoleparole": "Y", ";eStatoUnPartoTirareCosiTanteParoleRandomiche": "Z",

		"_": " ", ";FUNZIONA": "=", ";DAJECAZZOVAI": ".", ";LeonardoEGAY": "[", ";TantoGay": "]",
		";Gayone": ":", ";<>": ";", ";HoFinitoLeIdeeLOL": "!", ";QuantiCaratteriMancano?": "|",
		";NonStoDelirandoGiuro": "$", ";OkayForse": "#", ";CreareStaCodifica_èStataUnaSfida": "'",
		";UnaSfidaControLaMiaSaluteMentaleLOL": "\"", ";SoRetardato": "/", ";WlaFiga": "\\",
		";boh_nonSoCheScrivere": "<", ";meowMEOW_BITCH": ">", ";miuw": ")", ";alfa": "(",
		";SIUMTATTICOSO": "&", ";NoAllAlcolismo": "%",

		";KkA": "1", ";aAa": "2", ";hhH": "3", ";meOWWWWWW": "4", ";AAAAAAAA": "5",
		";SEX": "6", ";SIVENSTEVEN": "7", ";NumberOfStrayKids": "8", ";CazzumNine": "9",
		";PaliNonPresiDaLeonardo": "0",
	}

	sortedKeys := make([]string, 0, len(decodingMap))
	for key := range decodingMap {
		sortedKeys = append(sortedKeys, key)
	}
	// Sort keys by length descending
	sort.Slice(sortedKeys, func(i, j int) bool {
		return len(sortedKeys[i]) > len(sortedKeys[j])
	})

	decodedText := encodedText
	for _, key := range sortedKeys {
		decodedText = strings.ReplaceAll(decodedText, key, decodingMap[key])
	}

	return decodedText
}
