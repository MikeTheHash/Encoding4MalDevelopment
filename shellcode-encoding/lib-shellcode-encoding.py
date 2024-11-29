#DISCLAIMER: I dont take any responsability of how you're gonna use it
#its created only for fun, educational purposes, and --->certificated<--- penetration testing things

def encode(text):
    try:
        encoding_map = {
            "\x00": "LL", "\x01": "meow", "\x02": "kK", "\x03": "Kk", "\x04": "mM",
            "\x05": "Mm", "\x06": "sK", "\x07": "kS", "\x08": "MN", "\x09": "%M",
            "\x0A": "#", "\x0B": "£", "\x0C": "$", "\x0D": "!!!", "\x0E": "pQ",
            "\x0F": "<", "\x10": ">", "\x11": "(>.<)", "\x12": "(T.T)", "\x13": "(-.-)",
            "\x14": "(*^-^*)", "\x15": "^_^", "\x16": "=)", "\x17": "=(",
            "\x18": "(^o^)", "\x19": ":-)", "\x1A": ">:(", "\x1B": "<3", "\x1C": "(^-^)",
            "\x1D": ":3", "\x1E": ">:3", "\x1F": ">:-3", "\x20": ":-3", "\x21": "(-.-) .-=iii===-",
            "\x22": "kL", "\x23": "Maps-Maroon5", "\x24": "fhsdS", "\x25": "6t", "\x26": "fff",
            "\x27": "I", "\x28": "Wanna", "\x29": "die", "\x2A": "lol_jk", "\x2B": "m__-",
            "\x2C": "pqoO", "\x2D": "qWwWm", "\x2E": "iI._.", "\x2F": ".-.", "\x30": "._.",
            "\x31": ";-;", "\x32": "jJk", "\x33": "mLLnPo", "\x34": "sWa0", "\x35": "(UwU)",
            "\x36": "(OwO)", "\x37": ">:D", "\x38": ":-O", "\x39": "x_x", "\x3A": "zzz",
            "\x3B": "brb", "\x3C": "<==", "\x3D": "==>", "\x3E": "|||", "\x3F": "???",
            "\x40": "@_@", "\x41": "A_A", "\x42": "(b-b)", "\x43": "<o_o>", "\x44": "dD",
            "\x45": "so_o", "\x46": "(╯°□°）╯", "\x47": "UwUs", "\x48": "T_T", "\x49": "(¬_¬)",
            "\x4A": "O_O", "\x4B": "(ಥ_ಥ)", "\x4C": "(☞ﾟヮﾟ)☞", "\x4D": "(ノಠ益ಠ)ノ",
            "\x4E": "YOLO", "\x4F": "XD", "\x50": ":P", "\x51": ":V", "\x52": "-_-",
            "\x53": ";_;", "\x54": "T^T", "\x55": "^o^", "\x56": "owo", "\x57": "(Q_Q)",
            "\x58": "(ಥ﹏ಥ)", "\x59": "(¬‿¬)", "\x5A": ">:|", "\x5B": "(≧ω≦)", "\x5C": "ʕ•ᴥ•ʔ",
            "\x5D": "(✿◕‿◕)", "\x5E": "(*≧ω≦)", "\x5F": "¯\\_(ツ)_/¯", "\x60": "(ノಥ益ಥ)ノ彡┻━┻",
            "\x61": "(✧ω✧)", "\x62": "QAQ", "\x63": "UwU", "\x64": "o_o", "\x65": "OwO",
            "\x66": "(っ◔◡◔)っ", "\x67": "(ง'̀-'́)ง", "\x68": "(๑•̀ㅂ•́)و", "\x69": "(￣ω￣)",
            "\x6A": "ヽ(°◇° )ノ", "\x6B": "(ノ´∀｀)ノ", "\x6C": "≧◡≦", "\x6D": "(´｡• ω •｡`)",
            "\x6E": "(>w<)", "\x6F": "ᕦ(ò_óˇ)ᕤ", "\x70": "(╬ಠ益ಠ)", "\x71": "(⊙_⊙)",
            "\x72": "(。_。)", "\x73": "(>_<)", "\x74": "(￣▽￣)ノ", "\x75": "ヽ(´ー` )┌",
            "\x76": "(•_•) ( •_•)>⌐■-■ (⌐■_■)", "\x77": "(ᵔᴥᵔ)", "\x78": "(≧◡≦)",
            "\x79": "(๑‾᷅⍨‾᷅๑)", "\x7A": "(✿´‿`)", "\x7B": "(⌒▽⌒)", "\x7C": "(✧ω✧)-",
            "\x7D": "( ͡° ͜ʖ ͡°)", "\x7E": "＼(°o°)／", "\x7F": "(ಥ﹏ಥ)"
        }

        encoded_text = ""
        for char in text:
            encoded_text += encoding_map.get(char, char)  # Default to original character if no mapping exists
        return encoded_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def decode(encoded_text):
    try:
        decoding_map = {
            "LL": "\x00", "meow": "\x01", "kK": "\x02", "Kk": "\x03", "mM": "\x04",
            "Mm": "\x05", "sK": "\x06", "kS": "\x07", "MN": "\x08", "%M": "\x09",
            "#": "\x0A", "£": "\x0B", "$": "\x0C", "!!!": "\x0D", "pQ": "\x0E", "<": "\x0F",
            ">": "\x10", "(>.<)": "\x11", "(T.T)": "\x12", "(-.-)": "\x13", "(*^-^*)": "\x14",
            "^_^": "\x15", "=)": "\x16", "=(" : "\x17", "(^o^)": "\x18", ":-)": "\x19",
            ">:(": "\x1A", "<3": "\x1B", "(^-^)": "\x1C", ":3": "\x1D", ">:3": "\x1E",
            ">:-3": "\x1F", ":-3": "\x20", "(-.-) .-=iii===-": "\x21", "kL": "\x22",
            "Maps-Maroon5": "\x23", "fhsdS": "\x24", "6t": "\x25", "fff": "\x26", "I": "\x27",
            "Wanna": "\x28", "die": "\x29", "lol_jk": "\x2A", "m__-": "\x2B", "pqoO": "\x2C",
            "qWwWm": "\x2D", "iI._.": "\x2E", ".-.": "\x2F", "._.": "\x30", ";-;": "\x31",
            "jJk": "\x32", "mLLnPo": "\x33", "sWa0": "\x34", "(UwU)": "\x35", "(OwO)": "\x36",
            ">:D": "\x37", ":-O": "\x38", "x_x": "\x39", "zzz": "\x3A", "brb": "\x3B", "<==": "\x3C",
            "==>": "\x3D", "|||": "\x3E", "???": "\x3F", "@_@": "\x40", "A_A": "\x41",
            "(b-b)": "\x42", "<o_o>": "\x43", "dD": "\x44", "so_o": "\x45", "(╯°□°）╯": "\x46",
            "UwUs": "\x47", "T_T": "\x48", "(¬_¬)": "\x49", "O_O": "\x4A", "(ಥ_ಥ)": "\x4B",
            "(☞ﾟヮﾟ)☞": "\x4C", "(ノಠ益ಠ)ノ": "\x4D", "YOLO": "\x4E", "XD": "\x4F",
            ":P": "\x50", ":V": "\x51", "-_-": "\x52", ";_;": "\x53", "T^T": "\x54",
            "^o^": "\x55", "owo": "\x56", "(Q_Q)": "\x57", "(ಥ﹏ಥ)": "\x58", "(¬‿¬)": "\x59",
            ">:|": "\x5A", "(≧ω≦)": "\x5B", "ʕ•ᴥ•ʔ": "\x5C", "(✿◕‿◕)": "\x5D",
            "(*≧ω≦)": "\x5E", "¯\\_(ツ)_/¯": "\x5F", "(ノಥ益ಥ)ノ彡┻━┻": "\x60", "(✧ω✧)": "\x61",
            "QAQ": "\x62", "UwU": "\x63", "o_o": "\x64", "OwO": "\x65", "(っ◔◡◔)っ": "\x66",
            "(ง'̀-'́)ง": "\x67", "(๑•̀ㅂ•́)و": "\x68", "(￣ω￣)": "\x69", "(ヽ(°◇° )ノ)": "\x6A",
            "(ノ´∀｀)ノ": "\x6B", "≧◡≦": "\x6C", "(´｡• ω •｡`)": "\x6D", "(>w<)": "\x6E",
            "ᕦ(ò_óˇ)ᕤ": "\x6F", "(╬ಠ益ಠ)": "\x70", "(⊙_⊙)": "\x71", "(。_。)": "\x72",
            "(>_<)": "\x73", "(￣▽￣)ノ": "\x74", "ヽ(´ー` )┌": "\x75", "(•_•) ( •_•)>⌐■-■ (⌐■_■)": "\x76",
            "(ᵔᴥᵔ)": "\x77", "(≧◡≦)": "\x78", "(๑‾᷅⍨‾᷅๑)": "\x79", "(✿´‿`)": "\x7A",
            "(⌒▽⌒)": "\x7B", "(✧ω✧)-": "\x7C", "( ͡° ͜ʖ ͡°)": "\x7D", "＼(°o°)／": "\x7E",
            "(ಥ﹏ಥ)": "\x7F"
        }

        # Sort the decoding map by the length of encoded string in descending order
        sorted_decoding_map = sorted(decoding_map.items(), key=lambda x: len(x[0]), reverse=True)
        
        for encoded_str, original_char in sorted_decoding_map:
            encoded_text = encoded_text.replace(encoded_str, original_char)

        return encoded_text

    except Exception as e:
        print(f"An error occurred during decoding: {e}")
        return None

def main():
    choice = input("Enter 1 to encode or 2 to decode: ")

    if choice == '1':
        text_to_encode = input("Enter the text to encode: ")
        encoded_text = encode(text_to_encode)
        if encoded_text is not None:
            print(f"Encoded text: {encoded_text}")
    elif choice == '2':
        text_to_decode = input("Enter the text to decode: ")
        decoded_text = decode(text_to_decode)
        if decoded_text is not None:
            print(f"Decoded text: {decoded_text}")
    else:
        print("Invalid choice, please enter 1 or 2.")

if __name__ == "__main__":
    main()

