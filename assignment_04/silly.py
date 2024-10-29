# Create constants.
SILLY_LVL = 5
SILLY_DURATION = 7

# Create variables with user input.
silly_scale = int(input('How silly are you on a scale from 1 to 10? '))
silly_xp = int(input('How many practical experience do you have being silly? '))

# Compare variables to constants.
if silly_scale >= SILLY_LVL and silly_xp >= SILLY_DURATION:
    print('You are silly enough to survive the coming hardships; never lose your whimsy.')
elif silly_scale >= SILLY_LVL and silly_xp < SILLY_DURATION:
    print(f'''
          You may be silly, but you still have much to learn.

          You need to have spent at least {SILLY_DURATION} units in the trenches;
          Keep practicing.
          ''')
elif silly_scale < SILLY_LVL and silly_xp >= SILLY_DURATION:
    print(f'''
          You've been here a long time, but you have lost what made you silly.
          
          You have fallen below {SILLY_LVL} silly units.

          Where is your whimsy? Your joy?
          ''')
else:
    print(f'''
          Partner, I fear for you. 
          It is a difficult thing to survive in this world without a baseline 
          silliness.
          
          You have less than {SILLY_LVL} sillies, and that can't be good for 
          anyone.
          You haven't even been silly for {SILLY_DURATION} times.

          How do you do it? How do you face the world without some level of
          silliness to overcome the horrors that pervade? How do you look
          unflinchingly into cruelty and hate? How do you reckon with the worst
          of humanity, without celebrating absurdity, joy, and, yes, silliness?
          ''')
    
# I forgot the 'f' before the triple quotes, so my constants were printing with
# the curly brackets, instead of the value. I asked chatgpt why, which is how
# I figured out the solution