import random

word_bank=['python', 'java', 'kotlin', 'javascript']
word=random.choice(word_bank)

guessedword=["_"]*len(word)

attempts=10

while attempts>0:
    print('\nCurrent word: ' + ' '.join(guessedword))

    guess=input('guess a letter:').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessedword[i]=guess
        print('Correct!')
        
    else:
        attempts-=1
        print('wrong guess! attempts left:' + str(attempts))

    if '_' not in guessedword:
        print('\nCongratulations! You guessed the word: ' + word)
        break
    if attempts ==0 and '_' in guessedword:
        print('\nGame Over! The word was: ' + word)

