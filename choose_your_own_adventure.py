name = input('Type in your name: ')
print('Welcome', name, 'to this adventure!')

question = input('Hey, You are on a dirt road and it has come to an end. So there are two roads left to move i.e, left or right, so which way would you go(left/right).').lower()
if question == 'left':
    question = input('You are on a river and to move further you can either swim across the river or just walk around it. So what would you choose "swim" to swim through the river or "walk" to walk around the river.').lower()
    if question == 'swim':
        print('Unfortunately, there was a crocodile in the middle of the river. So you died!!')
    elif question == 'walk':
        print('You walked desperately for many mile and died of starvation.')
    else:
        print('Enter a valid choice, next time..')

elif question == 'right':
    question = input('There was a Truck parked along the side of the road with its key inside. So would you take the Truck or walk(Truck/Walk)').lower()
    if question == 'truck':
        print('The Truck had a time bomb set to 30 minutes, but you were lazy enough to get out of it when you saw a bed on the roadside. So while resting on the bed, the Truck exploded and you died due to the explosion. So you lost!!')
    elif question == 'walk':
        print('You were brave enough to walk, rather than taking the Truck which had a time bomb below it. So, you won!!')
    else:
        print('Enter a valid choice, next time..')

else:
   print('Enter a valid choice, next time...')