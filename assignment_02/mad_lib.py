# This is a madlib example for functions.



def madlib(adjective_1, noun_1, adjective_2, place, adverb_1, adverb_2, adjective_3, noun_2, adverb_3):
    '''madlib function'''
    story = f'''
On a {adjective_1} day, I found a {noun_1} in the {adjective_2} {place} . \
It was {adverb_1} glowing, and I decided to {adverb_2} take it home. My \
{adjective_3} {noun_2} was thrilled when I showed it to them. We spent the \
afternoon {adverb_3} playing with it and couldn’t stop laughing. It was the \
best day ever!
'''
    return story

def get_input():
    '''prompt user for inputs to madlib'''
    adjective_1 = input('adjective:')
    noun_1 = input('noun:')
    adjective_2 = input('adjective:')
    place = input('place:')
    adverb_1 = input('adverb:')
    adverb_2 = input('adverb:')
    adjective_3 = input('adjective:')
    noun_2 = input('noun:')
    adverb_3 = input('adverb:')

    return adjective_1, noun_1, adjective_2, place, adverb_1, adverb_2, adjective_3, noun_2, adverb_3

input = get_input()
print(madlib(*input))


# Previous setup following two comments:
# output_story = madlib(adjective_1, noun_1, adjective_2, place, adverb_1, adverb_2, adjective_3, noun_2, adverb_3)
# print(output_story)