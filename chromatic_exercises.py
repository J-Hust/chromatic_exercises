# fingers = [0,0,0,0]
# offsets = [0,0,0,0]

    # for each set of fingers:
        # for each set of offsets:
            #make the tab
        
import itertools

def combos():
    f = [1,2,3,4]
    o = [0,1,2,3,4,5]

    for x in itertools.permutations(f, 4):
        for y in itertools.product(o, repeat=4):
            print('x', x, 'y', y)

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

    print(format_tab(tab))

def format_tab(tab):
    final = ''
    for string in list(reversed(tab)):
        final += ' '.join(map(str, string)) + '\n'
    return final + '\n\n\n'


# make_tab([4,2,3,1], [0,0,0,0])
combos()