class HangManGame:
    def __init__( self ):
        self.answerList = []
        self.displayList = []
        self.loopTime = 5
        self.score = 0

    def checkDigitRange( self , digit ):
        number = int(digit)
        if not ( number >= 0 and number <= 9):
            raise Exception('digit out of range')
        
    def checkAnswerListValidation( self ):
        for element in self.answerList:
            self.checkDigitRange( element )
            
    def checkAnswerListLength( self ):
        if len(self.answerList) < 12:
            raise Exception('not reach the input length')
                
    def inputToAnswerList( self ):
        userInput = input('Input answer: ')
        self.answerList = userInput.split(' ')
        
        self.displayList = [ '_' for element in range( len( self.answerList) )]
     
    def updateDisplayList( self, digit ):
        if digit in self.answerList:
            for index in range( len( self.answerList ) ):
                if self.answerList[ index ] == digit:
                    self.displayList[ index ] = self.answerList[ index ]
        else:
            self.displayList.append( digit )
            
    def calculatePoint( self ):
        for element in range(len(self.answerList)):
            if self.displayList[ element ] != '_':
                self.score += 1
                
    def inputGuessWord( self ):
        for _ in range( self.loopTime ):
            userInput = input('\nGuess digit: ')

            self.checkDigitRange( userInput  )
            self.updateDisplayList( userInput )
            print(*self.displayList , sep = " ")
        
    def playGame( self ):
        try:
            self.inputToAnswerList()
            self.checkAnswerListValidation()
            self.checkAnswerListLength()
            
            self.inputGuessWord()
                
            self.calculatePoint()
            print('\nYour score is: ', self.score )
        except Exception as error:
            print( error )
            
if __name__ == '__main__':
    game = HangManGame()
    game.playGame()
