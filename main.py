

# Nom & Prenom Mohammad ZEFRI
# Groupe Developpement Degital 103
# Module Les Bases d Algorithmique
# Controle Continu 3
# 01/26/2023
# Projet 1






import random
from en_words_file import en_words



menu='\n---MENU---\n\n1 Play\n2 Quit\n3 About\n'




def draw(tries) :
    if tries == 8 :
        return('   ____ \n'
                '  |    \n'
                '  |    \n'
                '  |    \n'
                '  |    \n'
                '  |    \n'
                '  |    \n'
                '__|__\n')
    elif tries == 7 :
        return('   ____ \n'
                '  |  |\n'
                '  |   \n'
                '  |   \n'
                '  |   \n'
                '  |   \n'
                '  |   \n'
                '__|__\n')
    elif tries == 6 :
        return('   ____ \n'
                '  |  |\n'
                '  |  |\n'
                '  |   \n'
                '  |   \n'
                '  |   \n'
                '  |   \n'
                '__|__\n')
    elif tries == 5 :
        return('   ____ \n'
                '  |  |\n'
                '  |  |\n'
                '  |  |\n'
                '  |   \n'
                '  |   \n'
                '  |   \n'
                '__|__\n')
    elif tries == 4 :
        return('   ____ \n'
                '  |  |\n'
                '  |  |\n'
                '  |  |\n'
                '  |  O\n'
                '  | / \n'
                '  |   \n'
                '__|__\n')
    elif tries == 3 :
        return('   ____ \n'
                '  |  |\n'
                '  |  |\n'
                '  |  |\n'
                '  |  O \n'
                '  | /|  \n'
                '  |   \n'
                '__|__\n')
    elif tries == 2 :
        return('   ____ \n'
                '  |  |\n'
                '  |  |\n'
                '  |  |\n'
                '  |  O \n'
                '  | /|\ \n'
                '  |   \n'
                '__|__\n')
    elif tries == 1 :
        return('   ____ \n'
                '  |  |\n'
                '  |  |\n'
                '  |  |\n'
                '  |  O\n'
                '  | /|\ \n'
                '  | /   \n'
                '__|__\n')
    elif tries == 0 :
        return('   ____ \n'
                '  |  |\n'
                '  |  |\n'
                '  |  |\n'
                '  |  O\n'
                '  | /|\ \n'
                '  | / \ \n'
                '__|__\n')


while True:

    clist = ['1', '2', '3', '4']

    print(menu)
    c = input('Type your choice :\n')

    if c not in clist:
        print(menu)
        print('Invalid choice')

    elif c == '1':
        tries = 8
        saveC = ""
        wrd = random.choice(en_words)
        wrd_as_list = list(wrd)
        hddn_wrd = '_'*len(wrd)
        hddn_wrd_as_lst = list(hddn_wrd)
        correct_guesses = 0
        wrong_guesses = 0
        print(str(hddn_wrd_as_lst))
        character = input('Enter a character:\n').strip().lower()

        # Case one
        if character == wrd:
            print('\nCongratulations you won\n')

        # Case two
        elif character != wrd and character not in wrd:
            print(f'False the caracter \"{character}\" is not in')
            print(str(hddn_wrd_as_lst))
            tries = tries - 1
            wrong_guesses = wrong_guesses + 1
            print(f'{tries} tries left')
            print(draw(tries))
            while tries != 0:
                if saveC == wrd:
                    print('\nCongratulations you won\n')
                    print(f'You did :\n{correct_guesses} correct guesses\n{wrong_guesses} wrong guesses')
                    break
                elif len(saveC) == len(wrd) :
                    break
                else:
                    while saveC != wrd:
                        if len(saveC) == len(wrd):
                            print('\nCongratulations you won\n')
                            print(f'You did :\n{correct_guesses} correct guesses\n{wrong_guesses} wrong guesses')
                            break
                        else :
                            character = input('Enter a new character:\n')
                            if character in wrd:
                                if saveC.count(character) == wrd.count(character):
                                    print(f'There is no more \"{character}\" in')
                                    print(str(hddn_wrd_as_lst))
                                elif saveC.count(character) < wrd.count(character):
                                    print(f'True the caracter \"{character}\" is in')
                                    saveC = saveC + character
                                    correct_guesses = correct_guesses + 1
                                    ##################################
                                    for u in range(len(wrd)) :
                                        if wrd[u] == character and hddn_wrd_as_lst[u] == '_' :
                                            hddn_wrd_as_lst[u] = character
                                            break
                                    print(str(hddn_wrd_as_lst))
                                    ##################################
                            else:
                                wrong_guesses = wrong_guesses + 1
                                print(f'False the caracter \"{character}\" is not in')
                                print(str(hddn_wrd_as_lst))
                                tries = tries - 1
                                if tries == 0:
                                    print(draw(tries))
                                    print('Game over')
                                    print(f'You did :\n{correct_guesses} correct guesses\n{wrong_guesses} wrong guesses')
                                    break
                                else:
                                    print(draw(tries))
                                    print(f'{tries} tries left')


        # Case three
        elif character != wrd and character in wrd:
            while tries != 0:
                if saveC == wrd:
                    print('\nCongratulations you won\n')
                    print(f'You did :\n{correct_guesses} correct guesses\n{wrong_guesses} wrong guesses')
                    break
                elif len(saveC) == len(wrd) :
                    break
                else:
                    if saveC.count(character) == wrd.count(character):
                        print(f'There is no more \"{character}\" in')
                        print(str(hddn_wrd_as_lst))
                    elif saveC.count(character) < wrd.count(character):
                        print(f'True the caracter \"{character}\" is in')
                        saveC = saveC + character
                        correct_guesses = correct_guesses + 1
                        ##################################
                        for u in range(len(wrd)) :
                            if wrd[u] == character and hddn_wrd_as_lst[u] == '_' :
                                hddn_wrd_as_lst[u] = character
                                break
                        print(str(hddn_wrd_as_lst))
                        ##################################

                    while saveC != wrd :
                        if len(saveC) == len(wrd):
                            print('\nCongratulations you won\n')
                            print(f'You did :\n{correct_guesses} correct guesses\n{wrong_guesses} wrong guesses')
                            break
                        else :
                            character = input('Enter a new character:\n')
                            if character in wrd:
                                if saveC.count(character) == wrd.count(character):
                                    print(f'There is no more \"{character}\" in')
                                    print(str(hddn_wrd_as_lst))
                                elif saveC.count(character) < wrd.count(character):
                                    print(f'True the caracter \"{character}\" is in')
                                    saveC = saveC + character
                                    correct_guesses = correct_guesses + 1
                                    ##################################
                                    for u in range(len(wrd)) :
                                        if wrd[u] == character and hddn_wrd_as_lst[u] == '_' :
                                            hddn_wrd_as_lst[u] = character
                                            break
                                    print(str(hddn_wrd_as_lst))
                                    ##################################

                            else:
                                print(f'False the caracter \"{character}\" is not in')
                                print(str(hddn_wrd_as_lst))
                                wrong_guesses = wrong_guesses + 1
                                tries = tries - 1
                                if tries == 0:
                                    print(draw(tries))
                                    print('Game over')
                                    print(f'You did :\n{correct_guesses} correct guesses\n{wrong_guesses} wrong guesses')
                                    break
                                else:
                                    print(f'{tries} tries left')
                                    print(draw(tries))

    elif c == '2':
        print('Bye')
        break
    elif c == '3':
        print('By Mohammad Zefri 2023\nVersion 1.0')