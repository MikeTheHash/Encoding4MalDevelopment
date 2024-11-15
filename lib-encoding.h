#ifndef ENCODING_H
#define ENCODING_H

#include <string>
#include <map>
#include <algorithm>

// Encoding map
const std::map<char, std::string> encoding_map = {
    {'a', ";EDDAI"}, {'b', ";FROCIO"}, {'c', ";skks"}, {'d', ";stocazzum"},
    {'e', ";miau"}, {'f', ";gatto"}, {'g', ";shell"}, {'h', ";cazzarola"},
    {'i', ";azzo"}, {'j', ";bau"}, {'k', ";MaNonLoSoHoFinitoLeParoleRandomicheDaMettere"},
    {'l', ";gronc"}, {'m', ";releone"}, {'n', ";fuckmepls"}, {'o', ";milliseconds"},
    {'p', ";mare"}, {'q', ";lago"}, {'r', ";straykids"}, {'s', ";alfabeto"},
    {'t', ";droga"}, {'u', ";eldenring"}, {'v', ";hollowknight"}, {'w', ";hollow"},
    {'x', ";yz"}, {'y', ";gattinibellissimi"}, {'z', ";sigmeyer"},
    {'A', ";elikoper"}, {'B', ";JELIKOPETER"}, {'C', ";wlattrocca"}, {'D', ";wigattini"},
    {'E', ";hex"}, {'F', ";GGH"}, {'G', ";Lll"}, {'H', ";miuwww"},
    {'I', ";motard"}, {'J', ";patate"}, {'K', ";figosaLaCappa"}, {'L', ";nonsoaltreparolepercodificare"},
    {'M', ";pippo"}, {'N', ";PippoBaudo"}, {'O', ";letteraStramba"}, {'P', ";pIsForPoppe"},
    {'Q', ";quaderno"}, {'R', ";baubaubaumiao"}, {'S', ";StandsForStrunz"},
    {'T', ";voglioungatto"}, {'U', ";wleCANNE"}, {'V', ";FR"}, {'W', ";ProtocolloTCP"},
    {'X', ";mutande"}, {'Y', ";hofinitoleparole"}, {'Z', ";eStatoUnPartoTirareCosiTanteParoleRandomiche"},
    {' ', "_"}, {'=', ";FUNZIONA"}, {'.', ";DAJECAZZOVAI"}, {'[', ";LeonardoEGAY"},
    {']', ";TantoGay"}, {':', ";Gayone"}, {';', ";<>"}, {'!', ";HoFinitoLeIdeeLOL"},
    {'|', ";QuantiCaratteriMancano?"}, {'$', ";NonStoDelirandoGiuro"}, {'#', ";OkayForse"},
    {'\'', ";CreareStaCodifica_èStataUnaSfida"}, {'"', ";UnaSfidaControLaMiaSaluteMentaleLOL"},
    {'/', ";SoRetardato"}, {'\\', ";WlaFiga"}, {'<', ";boh_nonSoCheScrivere"},
    {'>', ";meowMEOW_BITCH"}, {')', ";miuw"}, {'(', ";alfa"}, {'&', ";SIUMTATTICOSO"},
    {'%', ";NoAllAlcolismo"}, {'1', ";KkA"}, {'2', ";aAa"}, {'3', ";hhH"},
    {'4', ";meOWWWWWW"}, {'5', ";AAAAAAAA"}, {'6', ";SEX"}, {'7', ";SIVENSTEVEN"},
    {'8', ";NumberOfStrayKids"}, {'9', ";CazzumNine"}, {'0', ";PaliNonPresiDaLeonardo"}
};

// Decoding map
const std::map<std::string, char> decoding_map = [] {
    std::map<std::string, char> temp;
    for (const auto& pair : encoding_map) {
        temp[pair.second] = pair.first;
    }
    return temp;
}();

// Function to encode a string
std::string encode(const std::string& text) {
    std::string encoded_text;
    for (const char& c : text) {
        auto it = encoding_map.find(c);
        encoded_text += (it != encoding_map.end()) ? it->second : std::string(1, c);
    }
    return encoded_text;
}

// Function to decode a string
std::string decode(const std::string& encoded_text) {
    std::string decoded_text = encoded_text;
    for (const auto& pair : decoding_map) {
        size_t pos = 0;
        while ((pos = decoded_text.find(pair.first, pos)) != std::string::npos) {
            decoded_text.replace(pos, pair.first.length(), 1, pair.second);
            pos += 1;
        }
    }
    return decoded_text;
}

#endif // ENCODING_H
