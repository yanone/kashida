# https://www.khtt.net/en/page/1821/the-big-kashida-secret


def word(string):
    """Insert kashida characters into a single word."""

    finalAndIsolatedOnly = [
        "ء",
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
    ]

    kashida = "ـ"

    # 0. remove all existing kashidas from the string
    string = string.replace(kashida, "")

    # 1. after a kashida that is manually placed in the text by the user,
    if "ـ" in string:
        pos = string.find("ـ")
        # print '#1'
        return string[:pos] + kashida + string[pos:]

    # 2. after a Seen or Sad (initial and medial form),
    letters = ["س", "ص", "ښ", "ڛ", "ش", "ۺ", "ڜ", "ﺺ", "ڝ", "ڞ", "ض", "ݜ", "ݭ"]
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1
        if letter in letters:
            # print '#2', string[pos], string[pos+1]
            pos_plus_one = pos + 1
            return string[:pos_plus_one] + kashida + string[pos_plus_one:]

    # 3. before the final form of Taa Marbutah, Haa, Dal,
    letters = ["ه", "ۀ", "ة", "ە", "د", "ذ", "ڈ", "ڌ", "ڍ", "ډ", "ڊ", "ڋ", "ڎ", "ڏ", "ڐ", "ۮ", "ݙ", "ݚ"]
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1
        if letter in letters:
            if not string[pos - 1] in finalAndIsolatedOnly:
                # print '#3', string[pos-1], string[pos]
                return string[:pos] + kashida + string[pos:]

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
        if letter in letters:
            if not string[pos - 1] in finalAndIsolatedOnly and string[pos] in finalAndIsolatedOnly:
                # print '#4', string[pos-1], string[pos]
                return string[:pos] + kashida + string[pos:]

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
    succeeding = ["ر", "ز", "ڑ", "ڒ", "ړ", "ڔ", "ڕ", "ږ", "ڗ", "ژ", "ڙ", "ۯ", "ݛ", "ݫ", "ݬ", "ى", "ي", "ئ", "ی", "ې", "ۑ", "ٸ"]
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1
        if letter in succeeding:
            if string[pos - 1] in preceding and string[pos] in succeeding:
                # print '#5', string[pos-1], string[pos]
                return string[:pos] + kashida + string[pos:]

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

        # letter is at the end of word
        if not string[pos - 1] in finalAndIsolatedOnly and i == 0 and letter in letters:
            # print '#6 letter is at the end of word', string[pos-1], string[pos]
            return string[:pos] + kashida + string[pos:]

        # letter is in middle of word, but final form
        if not string[pos - 1] in finalAndIsolatedOnly and string[pos] in letters and string[pos] in finalAndIsolatedOnly:
            # print '#6 final form of letter', string[pos-1], string[pos]
            return string[:pos] + kashida + string[pos:]

    # 7. before the final form of other characters that can be connected.
    for i, letter in enumerate(reversed(string)):
        pos = len(string) - i - 1
        # print(pos, string[pos - 1], string[pos])

        if not string[pos - 1] in finalAndIsolatedOnly:
            # print '#7', string[pos-1], string[pos]
            return string[:pos] + kashida + string[pos:]

    return string


def text(string):
    """Insert kashida characters into a whole text, once per word."""

    sentence = []
    for single_word in string.split(" "):
        sentence.append(word(single_word))
    return " ".join(sentence)
