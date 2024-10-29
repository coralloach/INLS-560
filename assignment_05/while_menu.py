# While loop menu.

menu_option = ''

while menu_option != 'q':
    print('FLOWERS:', 'a: alstromeria', 'b: lobelia', 'q:quit', sep="\n")
    menu_option = input("please choose 'a', 'b', or 'q': ")
    if menu_option == 'a':
        print("- my mom's favourite flower, various colours, with a speckled pattern")    
    elif menu_option == 'b':
        print('- one of my favourite flowers, small, and dark, bold blue/purple in colour')
