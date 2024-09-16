#this is a madlib example for functions

adjective_1 = input('adjective_1')
noun_1 = input('noun_1')
adjective_2 = input('adjective_2')
place = input('place')
adverb_1 = input('adverb_1')
adverb_2 = input('adverb_2')
adjective_3 = input('adjective_3')
noun_2 = input('noun_2')
adverb_3 = input('adverb_3')

def madlib(adjective_1, noun_1, adjective_2, place, adverb_1, adverb_2, adjective_3, noun_2, adverb_3):
    '''madlib function'''
    story = f'''
On a {adjective_1} day, I found a {noun_1} in the {adjective_2} {place} . It was {adverb_1} glowing, and I decided to {adverb_2} take it home. My {adjective_3} {noun_2} was thrilled when I showed it to them. We spent the afternoon {adverb_3} playing with it and couldn’t stop laughing. It was the best day ever!
'''
    return story

output_story = madlib(adjective_1, noun_1, adjective_2, place, adverb_1, adverb_2, adjective_3, noun_2, adverb_3)
print(output_story)