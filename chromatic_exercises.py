import itertools
import sys

def chromatic():
    fingers = [1,2,3,4]
    offsets = [0,1,2,3,4,5]
    i = 1

    file = open('chromatic_exercises.txt', 'a')
    for f in itertools.permutations(fingers, 4):
        for o in itertools.product(offsets, repeat=4):
            file.write('#' + str(i) + '\n\n' + make_tab(f,o))
            sys.stdout.flush()
            i += 1
    print('i at the end was', i)

    file.close()

def make_tab(fingers, offsets):

    # tab = [E, A, D, G, B, e]
    tab = [[], [], [], [], [], []]

    finished = False
    active_string = 0

    while finished == False:
        for i in range(0, 4):
            tab[offsets[i] + active_string].extend([fingers[i], '-'])
            for s in range(0, 6):
                if s != offsets[i] + active_string:
                    tab[s].extend(['-', '-'])
            if offsets[i] + active_string == 5: 
                finished = True
        active_string += 1


    fingers = list(reversed(fingers))
    offsets = list(reversed(offsets))
    finished = False
    active_string = 5

    while finished == False:
        for i in range(0, 4):
            tab[active_string - offsets[i]].extend([fingers[i], '-'])
            for s in range(0, 6):
                if s != active_string - offsets[i]:
                    tab[s].extend(['-', '-'])
            if active_string - offsets[i]  == 0: 
                finished = True
        active_string -= 1

    return format_tab(tab)

def format_tab(tab):
    final = ''
    for string in list(reversed(tab)):
        final += ' '.join(map(str, string)) + '\n'
    return final + '\n\n'


chromatic()