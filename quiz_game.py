print('Welcome to the Quiz Game!')

play = input('Do you wish to play the game? ')
score = 0
if play.lower() != 'yes':
    quit()
else:
    print("Okay, let's play!!")

question1 = input('What does CPU stands for? ')
if question1.lower() == 'central processing unit':
    print('Correct answer mate!!')
    score += 1
else:
     print('Sorry dude, wrong answer')

question2 = input('What does GPU stands for? ').lower()
if question2 == 'graphics processing unit':
    print('Correct again dude')
    score += 1
else:
     print('Srry dude, wrong answer!')

question3 = input('What does RAM stands for? ').lower()
if question3 == 'random access memory':
    print('Correct!')
    score += 1
else:
   print('Wrong')

question4 = input('What does PSU stands for? ').lower()
if question4 == 'power supply':
    print('Correct')
    score += 1
else:
    print('Wrong')

print('You got ' + str(score) + " question's correct")
print('Your accuracy is: ' + str((score/4)*100) + '%')


