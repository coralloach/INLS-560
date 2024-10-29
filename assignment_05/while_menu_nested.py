# While loop menu.

menu_option = ''

while menu_option != 'q':
    print(f'''
          what troubles you today?
          a: the state of the world
          b: the passage of time
          q: i don't want to answer your question
          ''')
    menu_option = input('please choose an option: ')
    if menu_option == 'a':
        print('''
              the world is very big, and you are so small. 
              
              there is nothing that an individual could do to cease the horrors. 
              it is through community, through culture, and collaboration that 
              things become something than what they already are.
              
              the power of the individual is a myth in this, our post-capitalist
              society. do not let capitalism get you down.
              ''')
    elif menu_option == 'b':
        clarifier = input('does the time pass too fast? (y/n): ')
        if clarifier == 'y':
            print('''
                  there are so many things to do, but the time in which to do
                  them keeps disappearing.

                  the only sensible prioritization is to do what makes you safe
                  first and foremost, content (and maybe even happy) next, and,
                  if possible, what makes you proud when you look back.

                  remember that you have more time than you think. focus on what
                  stretches out before you, rather than what is disappearing
                  behind you
                  ''')
        else:
            print('''
                  and yet it still passes.

                  with all the time in the world, what are you waiting for? if
                  time stretches before you, empty and hungry, find something
                  to fill it. learn how to bake bread, or sew a pair of pants,
                  or paint a cloud, or play a game. there are more things than
                  any one person could ever experience, but why not try?
                  ''')