def toAcronym( userInput ):
    wordList = userInput.split(' ')
    letterList = list(map(lambda word: word[0], wordList))
    upperLetterList = list(filter(lambda word: word.isupper() , letterList ))
    acronym = ''.join(map(str, upperLetterList))

    return acronym

if __name__== "__main__":
    try:
        acronymList = []
        userInputCount = int(input('Enter amount of time: \n'))
        
        for _ in range( userInputCount ):
            userInputWord = input('Enter word: \n')
            acronym = toAcronym( userInputWord )
            
            acronymList.append( acronym )

        acronymList.sort( key = lambda item: ( -len(item),item )  )

        print('\nSolution:\n')
        print(*acronymList, sep = "\n\n")
        
    except ValueError:
            print('this is not a number')
