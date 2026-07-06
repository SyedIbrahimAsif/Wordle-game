# WORDLE game
# choose_word() : chooses a random 5-letter word
def choose_word():
    from random import randint
    words = ["abbey", "abled", "abler", "abide", "ables", "abuzz", "acorn", "acred", "adage", "adays", "addle", "adieu", "agate", "agaze", "agent", "agger", "agile", "aging", "aglow", "agone", "agree", "alamo", "alate", "alway", "amole", "ample", "anglo", "angus", "anise", "antra", "anted", "anyon", "apage", "apian", "apnea", "apple", "aquas", "arcus", "argan", "argil", "argue", "arise", "armor", "armed", "artel", "ascot", "asper", "asset", "attest", "audio", "audit", "auger", "aural", "avian", "avise", "axoid", "azote", "bacon", "badge", "bafta", "bager", "baggy", "banal", "baron", "baser", "basky", "batch", "begot", "betas", "bible", "bilge", "bison", "biped", "blank", "blitz", "block", "blurb", "blush", "booby", "boose", "bourn", "boxer", "bower", "boxey", "boyar", "brace", "brash", "brave", "brose", "bumpy", "butte", "cabin", "cabal", "cache", "cadet", "camel", "carol", "casus", "chads", "chape", "chaos", "chock", "chic", "chip", "chive", "chock", "chlor", "chorus", "claps", "clap", "clamp", "clear", "clip", "cluck", "crab", "crack", "crop", "cuban", "cuter", "damp", "damps", "deal", "dears", "depth", "dingo", "doner", "dodge", "dolce", "downy", "dwarf", "edgey", "elder", "elect", "elide", "enema", "escar", "exile", "faxed", "feuar", "fezes", "feyer", "ficus", "fiber", "frisk", "funny", "fudge", "gazed", "gemmy", "geese", "gered", "gilt", "girly", "gothic", "greet", "haunt", "hecto", "horse", "house", "hoist", "hotly", "icyly", "idol", "idyll", "iris", "invoy", "ivy", "jabby", "jolly", "jiffy", "jumbo", "kayak", "keyer", "large", "lapse", "leper", "lucky", "lupus", "madly", "maked", "malth", "manly", "merry", "mighty", "moonlit", "motif", "nacho", "noddy", "nymph", "oval", "oxen", "ounce", "oval", "ouija", "pacey", "panky", "prick", "quail", "quote", "quoth", "reach", "ready", "robin", "rompy", "runway", "soily", "squash", "search", "shut", "smush", "smite", "slick", "snoop", "snuck", "stags", "stake", "stria", "sweet", "taint", "teary", "topic", "trophy", "uncle", "unlit", "unraw", "vessel", "venom", "vices", "viewy", "visa", "yages", "yucky"]
    return words[randint(0,len(words)-1)]
#reveal_word() : reveales the word with only the guessed characters
def display_word():
    outstr = ""
    for pos in range(len(word)):
        if foundchar[pos]:
            outstr += word[pos]
        else:
            outstr += "_"
    return outstr
#check_guess(guess) : checks the guess
def check_guess(guess,word):
    for guessChar in range(0,len(guess)-1):
        for wordChar in range(0,len(word)-1):
            if guess[guessChar] == word[wordChar] and (guessChar) == (wordChar):
                foundchar[wordChar] = True
    for guessChar in range(0,len(guess)-1):
        for wordChar in range(0,len(word)-1):
            if guess[guessChar] == word[wordChar] and not foundchar[wordChar]:
                misplaced[guessChar] = True
                if foundchar[wordChar]:
                    misplaced[wordChar] = False
    for guessChar in range(0,len(guess)-1):
        if not foundchar[guessChar] and not misplaced[guessChar] and guess[guessChar] not in not_in_word:
            not_in_word.append(guess[guessChar])
replay = True
while replay:
    word = choose_word()
    found = False
    not_in_word = []
    foundchar = []
    misplaced = []
    misplacedChar = []
    for pos in range(0,len(word)-1):
        misplaced.append(False)
    attempt = 5
    for pos in range(len(word)):
        foundchar.append(False)
    print("Welcome to WORDLE!")
    print(f"The word is: ", display_word())
    print(" ")
    while not found:
        print(f"You have {attempt} attempts left.")
        print("not in word:", not_in_word)
        print("not in correct position: ", misplacedChar)
        guessvalid = False
        while not guessvalid:
            guess = input("Enter a word: ")
            if len(guess) == 5:
                guessvalid = True
            elif len(guess) != 5:
                print("Word needs to be 5 letters!")
        check_guess(guess,word)
        for pos in range(0,len(word)-1):
            if misplaced[pos]:
                print(f"{guess[pos]} is not in the correct position")
                if guess[pos] not in misplacedChar:
                    misplacedChar.append(guess[pos])
        found = True
        for thischar in foundchar:
            if not thischar:
                found = False
        else:
            attempt -= 1
            if attempt == 0:
                print("game over : 6 attempts used")
                print(f"the word was: {word}")
                break
            print("The word is: ", display_word())
        print(" ")
    if found:
        print("congratulations! you've guessed the word!")
    print("game has finished!")
    valid = False
    while not valid:
        reinput = input("to replay, enter 're'. to exit, enter 'end'.").lower()
        if reinput == "re":
            replay = True
            valid = True
        elif reinput == "end":
            replay = False
            valid = True
        else:
            print("i don't understand that, do you wish to continue or end?")
            print(" ")
    print(" ")
    print(" ")
