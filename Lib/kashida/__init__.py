# https://www.khtt.net/en/page/1821/the-big-KASHIDA-secret

import re
import copy

KASHIDA = "ـ"
ISOLFINA = [
    "ا",
    "إ",
    "ٳ",
    "د",
    "ذ",
    "ڈ",
    "ڌ",
    "ڍ",
    "ډ",
    "ڊ",
    "ڋ",
    "ڎ",
    "ڏ",
    "ڐ",
    "ۮ",
    "ݙ",
    "ݚ",
    "ر",
    "ز",
    "ڑ",
    "ڒ",
    "ړ",
    "ڔ",
    "ڕ",
    "ږ",
    "ڗ",
    "ژ",
    "ڙ",
    "ۯ",
    "ݛ",
    "ݫ",
    "ݬ",
    "ﻻ",
    "ﻹ",
    "و",
    "ۄ",
    "ۊ",
    "ۏ",
    "ؤ",
    "ۅ",
    "ۆ",
    "ۇ",
    "ۈ",
    "ۉ",
    "ۋ",
    "ٷ",
    "ﻻ",
    "ﻷ",
    "ﻹ",
]


def word(string):
    """Insert KASHIDA characters into a single word."""

    # 0. remove all existing KASHIDAs from the string
    string = string.replace(KASHIDA, "")

    # # 1. after a KASHIDA that is manually placed in the text by the user,
    # if "ـ" in string:
    #     pos = string.find("ـ")
    #     print("#1")
    #     return string[:pos] + KASHIDA + string[pos:]

    # 2. after a Seen or Sad (initial and medial form),
    letters = ["س", "ص", "ښ", "ڛ", "ش", "ۺ", "ڜ", "ﺺ", "ڝ", "ڞ", "ض", "ݜ", "ݭ"]
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1
        if pos > 0 and letter in letters:
            # print("#2", string[pos], string[pos + 1])
            pos_plus_one = pos + 1
            return string[:pos_plus_one] + KASHIDA + string[pos_plus_one:]

    # 3. before the final form of Taa Marbutah, Haa, Dal,
    letters = ["ه", "ۀ", "ة", "ە", "د", "ذ", "ڈ", "ڌ", "ڍ", "ډ", "ڊ", "ڋ", "ڎ", "ڏ", "ڐ", "ۮ", "ݙ", "ݚ"]
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1
        if pos > 0 and letter in letters:
            if not string[pos - 1] in ISOLFINA:
                # print("#3", string[pos - 1], string[pos])
                return string[:pos] + KASHIDA + string[pos:]

    # 4. before the final form of Alef, Tah, Lam, Kaf and Gaf,
    letters = [
        "ا",
        "إ",
        "ٳ",
        "ب",
        "پ",
        "ٻ",
        "ڀ",
        "ت",
        "ٽ",
        "ث",
        "ٹ",
        "ٺ",
        "ٿ",
        "ݐ",
        "ݑ",
        "ݒ",
        "ݓ",
        "ݔ",
        "ݕ",
        "ݖ",
        "ك",
        "گ",
        "ڰ",
        "ڴ",
        "ڬ",
        "ڮ",
        "ڲ",
        "ڭ",
        "ڱ",
        "ڳ",
        "ل",
        "ڸ",
        "ݪ",
    ]
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1
        previous = string[pos - 1]
        if pos > 0 and letter in letters:
            if not previous in ISOLFINA and string[pos] in ISOLFINA:
                # print("#4", previous, string[pos])
                return string[:pos] + KASHIDA + string[pos:]

    # 5. before the preceding medial Baa of Ra, Ya and Alef Maqsurah,
    preceding = [
        "ٮ",
        "ب",
        "پ",
        "ٻ",
        "ڀ",
        "ت",
        "ٽ",
        "ث",
        "ٹ",
        "ٺ",
        "ٿ",
        "ݐ",
        "ݑ",
        "ݒ",
        "ݓ",
        "ݔ",
        "ݕ",
        "ݖ",
        "ن",
        "ں",
        "ڻ",
        "ڽ",
        "ى",
        "ي",
        "ئ",
        "ی",
        "ې",
        "ۑ",
        "ٸ",
    ]
    superceding = ["ر", "ز", "ڑ", "ڒ", "ړ", "ڔ", "ڕ", "ږ", "ڗ", "ژ", "ڙ", "ۯ", "ݛ", "ݫ", "ݬ", "ى", "ي", "ئ", "ی", "ې", "ۑ", "ٸ"]
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1
        if pos > 0 and letter in superceding:
            if string[pos - 1] in preceding and string[pos] in superceding:
                # print("#5", string[pos - 1], string[pos])
                return string[:pos] + KASHIDA + string[pos:]

    # 6. before the final form of Waw, Ain, Qaf and Fa,
    letters = [
        "ع",
        "ڠ",
        "غ",
        "ف",
        "ڤ",
        "ڡ",
        "ڢ",
        "ڣ",
        "ڥ",
        "ڦ",
        "ٯ",
        "ق",
        "ڧ",
        "ڨ",
        "و",
        "ۄ",
        "ۊ",
        "ۏ",
        "ؤ",
        "ۅ",
        "ۆ",
        "ۇ",
        "ۈ",
        "ۉ",
        "ۋ",
        "ٷ",
        "ݝ",
        "ݞ",
        "ݟ",
        "ݠ",
        "ݡ",
    ]
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1

        if pos > 0:

            # letter is at the end of word
            if not string[pos - 1] in ISOLFINA and i == 0 and letter in letters:
                # print("#6 letter is at the end of word", string[pos - 1], string[pos])
                return string[:pos] + KASHIDA + string[pos:]

            # letter is in middle of word, but final form
            if not string[pos - 1] in ISOLFINA and string[pos] in letters and string[pos] in ISOLFINA:
                # print("#6 final form of letter", string[pos - 1], string[pos])
                return string[:pos] + KASHIDA + string[pos:]

    # 7. before the final form of other characters that can be connected.
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1

        if pos > 0:
            if not string[pos - 1] in ISOLFINA:
                # print("#7", string[pos - 1], string[pos])
                return string[:pos] + KASHIDA + string[pos:]

    return string


def text(string):
    """Insert KASHIDA characters into a whole text, once per word."""

    output = copy.copy(string)
    rgx = re.compile("(\w[\w']*\w|\w)")
    for _word in rgx.findall(string):
        output = output.replace(_word, word(_word))

    return output
