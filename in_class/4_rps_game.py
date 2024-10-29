import random

while True:
    u_ch = input('Enter r, p, s, or q to quit:')
    
    if u_ch == 'q':
        print('thanks for playing! goodbye!')
        break

    if u_ch not in ['r', 'p', 's']:
        print("invalid input! please enter 'r', 'p', 's', or 'q'.")
        continue
    c_ch = random.choice(["r", "p", "s"])
    print(f'you chose: {u_ch} and the computer chose {c_ch}; therefore...\n ')

    if u_ch == c_ch:
        print("it's a tie!")
    elif (u_ch == 'r' and c_ch == 's') or \
         (u_ch == 'p' and c_ch == 'r') or \
         (u_ch == 's' and c_ch == 'p'):
        print("you win!")
    else:
        print("you lose!")

    print()