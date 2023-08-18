import re
from collections import defaultdict


# find the frequency of each letter in Moby Dick
def lettfreq(filename):
    fileIn = open(filename, "r")
    text = fileIn.read()

    text = "".join(text.lower().split())  # Splits by any sort of whitespace character and returns a string
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r" ", '', text)
    text = re.sub(r"\d", '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'_', '', text)
    letterCount = defaultdict(int)
    totalChars = len(text)

    for char in text:
        letterCount[char] += 1  #getting letter counts

    percentageDict = defaultdict(float)
    for char in letterCount:
        percentage = letterCount[char] / totalChars
        percentageDict[char] = percentage * 100    #calculate percentages

    return percentageDict
lettFrequency = lettfreq("TextFiles/mobydick.txt")
#print(lettFrequency)



# put letter frequency in descending order
def mostfreq(count_dict):
    most = sorted(count_dict.keys(), key=lambda key: count_dict[key], reverse=True)
    return most

mostFreqItem = mostfreq(lettFrequency)
# print(mostFreqItem)



# convert wordle possible answers into a list
def getList(filename):
    wordlist = open(filename, "r")
    text = wordlist.readlines()
    wordleList = []
    # print(text)
    for word in text:
        word = word.strip("\n")
        wordleList.append(word)

    return wordleList

wordleList = getList("/Users/alharethali/Documents/GitHub/WordleSolver/TextFiles/wordle-answers-alphabetical.txt")
# print(wordleList)

#randomly generate an answer word for reference
# answer = random.choice(wordleList)
# print(answer)


# Find the best starter word
wordleStr = " ".join(wordleList)
match = re.findall(r'[etaon]{5}', wordleStr, re.I)
# print(match)
# print("The first best guess is: atone.")

print("Put 'OTHER' for your first guess, and 'SNAIL' for your second guess! (Trust us on this)")



# Read in the user's results on their guess
print("For the results: type 'y' for yellow letters, 'g' for green letters, and 'x' for gray letters!")

# guessWord = input("Enter your Wordle guess: ")
# result = input("Enter your results (in 'y', 'g', 'x'): ")


def analyzeResult(guessWord, result):
    correctGuess = ["", "", "", "", ""]
    finalLetters = []
    finalLetterSeq = ["", "", "", "", ""]
    wrongLetters = []
    wrongLetterSeq = ["", "", "", "", ""]
    result = result.lower()
    guessWord = guessWord.lower()
    i = 0
    while i < 5:
        if result[i] =='y':
            finalLetters.append(guessWord[i])
            finalLetterSeq[i] = guessWord[i]
        elif result[i] == 'x':
            wrongLetters.append(guessWord[i])
            wrongLetterSeq[i] = guessWord[i]
        elif result[i] == 'g':
            correctGuess[i] = guessWord[i]
        i += 1
    return correctGuess, finalLetters, finalLetterSeq, wrongLetters, wrongLetterSeq

# print(analyzeResult(guessWord, result))
# correctGuess = analyzeResult(guessWord, result)[0]
# finalLetters = analyzeResult(guessWord, result)[1]
# finalLetterSeq = analyzeResult(guessWord, result)[2]
# wrongLetters = analyzeResult(guessWord, result)[3]
# wrongLetterSeq = analyzeResult(guessWord, result)[4]
# print(wrongLetterSeq)


# check if two lists overlap for repeating letters in green/gray
def overlap(a, b):
    setA = set(a)
    setB = set(b)
    intersec = setA.intersection(setB)
    result = list(intersec)
    return result

# print(overlap(correctGuess, finalLetters))
# print(overlap(correctGuess, wrongLetters))
# print(overlap(finalLetters, wrongLetters))



# get a list of possible answers
def filterWordleList (correctGuess, finalLetters, finalLetterSeq, wrongLetters, wrongLetterSeq, wordList):
    possibleWords = []

    if overlap(correctGuess, finalLetters) == [] and overlap(correctGuess, wrongLetters) == [] and overlap(finalLetters, wrongLetters) == []:
        for word in wordList:
            check = True
            for letter in word:
                if letter in wrongLetters:
                    check = False

            if check:
                for item in finalLetters:
                    if item not in word:
                        check = False
            if check:
                for item in finalLetterSeq:
                    if word[finalLetterSeq.index(item)] == item:
                        check = False

            if check:
                for item in correctGuess:
                    if item != "":
                        # print(correctGuess.index(item))
                        if word[correctGuess.index(item)] != item:
                            check = False
            if check:
                possibleWords.append(word)
        return possibleWords


    elif overlap(wrongLetters, correctGuess):
        # print(overlap(wrongLetters, correctGuess))

        for word in wordList:
            check = True
            for wrong in wrongLetters:
                if wrong in overlap(wrongLetters, correctGuess):
                    # for repeatLett in overlap(wrongLetters, correctGuess):
                        if word[wrongLetterSeq.index(wrong)] == wrong:
                            check = False
                        if word.count(wrong) > 1:
                            check = False
                else:
                    for letter in word:
                        if letter == wrong:
                            check = False


            if check:
                for item in finalLetters:
                    if item not in word:
                        check = False

            if check:
                for item in finalLetterSeq:
                    if word[finalLetterSeq.index(item)] == item:
                        check = False

            if check:
                for item in correctGuess:
                    if item != "":
                        # print(correctGuess.index(item))
                        if word[correctGuess.index(item)] != item:
                            check = False
            if check:
                possibleWords.append(word)
        return possibleWords


    elif overlap(finalLetters, correctGuess):
        for word in wordList:
            check = True
            for letter in word:
                if letter in wrongLetters:
                    check = False

            if check:
                for item in finalLetters:
                    if word.count(item) == 1:
                        check = False

            if check:
                for item in finalLetterSeq:
                    if word[finalLetterSeq.index(item)] == item:
                        check = False

            if check:
                for item in correctGuess:
                    if item != "":
                        # print(correctGuess.index(item))
                        if word[correctGuess.index(item)] != item:
                            check = False
            if check:
                possibleWords.append(word)
        return possibleWords


    elif overlap(finalLetters, wrongLetters):
        for word in wordList:
            check = True
            if check:
                for item in correctGuess:
                    if item != "":
                        if word[correctGuess.index(item)] != item:
                            check = False
            if check:
                for item in finalLetters:
                    if item not in word:
                        check = False

            if check:
                for item in finalLetterSeq:
                    if word[finalLetterSeq.index(item)] == item:
                        check = False

            if check:
                for lett in wrongLetters:
                    if lett in overlap(finalLetters, wrongLetters):
                        if word[finalLetterSeq.index(lett)] == lett:
                            check = False

                    else:
                        for letter in word:
                            if letter == lett:
                                check = False

            if check:
                possibleWords.append(word)

        return possibleWords


# possibleWords = filterWordleList(correctGuess, finalLetters, finalLetterSeq, wrongLetters, wrongLetterSeq, wordleList)
# print(possibleWords)



#find the best guess from the list of possible answers
def nextGuess(possList):

    scoreDict = {}
    for possWord in possList:
        wordScore = 0
        newWord = ''.join(sorted(set(possWord), key=possWord.index))
        for letter in newWord:
            letterScore = lettFrequency[letter]
            wordScore += letterScore
            aveScore = wordScore / len(newWord)
        # print(wordScore)
        scoreDict[possWord] = aveScore
    # print(scoreDict)        #get a dictionary of scores of each possible word

    maxValue = max(scoreDict, key=scoreDict.get)
    print("Your next best guess should be: " + maxValue)

# nextGuess(possibleWords)


def call():
    guessWord = input("Enter your Wordle guess: ")
    result = input("Enter your results (in 'y', 'g', 'x'): ")
    # analyzeResult(guessWord, result)
    correctGuess = analyzeResult(guessWord, result)[0]
    finalLetters = analyzeResult(guessWord, result)[1]
    finalLetterSeq = analyzeResult(guessWord, result)[2]
    wrongLetters = analyzeResult(guessWord, result)[3]
    wrongLetterSeq = analyzeResult(guessWord, result)[4]
    possibleWords = filterWordleList(correctGuess, finalLetters, finalLetterSeq, wrongLetters, wrongLetterSeq, wordleList)
    nextGuess(possibleWords)
    # print(possibleWords)
    return possibleWords

def call2(possibleWords):
    guessWord = input("Enter your Wordle guess: ")
    result = input("Enter your results (in 'y', 'g', 'x'): ")
    correctGuess = analyzeResult(guessWord, result)[0]
    finalLetters = analyzeResult(guessWord, result)[1]
    finalLetterSeq = analyzeResult(guessWord, result)[2]
    wrongLetters = analyzeResult(guessWord, result)[3]
    wrongLetterSeq = analyzeResult(guessWord, result)[4]
    possibleWords2 = filterWordleList(correctGuess, finalLetters, finalLetterSeq, wrongLetters, wrongLetterSeq, possibleWords)
    nextGuess(possibleWords2)
    return possibleWords2



words = call()
while True:
    user = input("Type 1 to continue, or 2 to exit: ")
    if user == "1":
        words = call2(words)

    elif user == "2":
        print("Good Game! See you tomorrow!")
        break

    else:
        print("Please enter 1 or 2")


