import random

opt = ['sasso',
       'carta',
       'forbice']

scelta = raw_input('Sasso, carta oppure forbice? >')


def game():
    x = random.randint(0, 2)
    scelta_pc = opt[x]
    if 's' in scelta:
        if 's' in scelta_pc:
            print "Parita'"
        elif 'c' in scelta_pc:
            print "Hai perso"
        else:
            print "Hai vinto"
    elif 'c' in scelta:
        if 's' in scelta_pc:
            print "Hai vinto"
        elif 'c' in scelta_pc:
            print "Parita'"
        else:
            print "Hai perso"
    elif 'f' in scelta:
        if 's' in scelta_pc:
            print "Hai perso"
        elif 'c' in scelta_pc:
            print "Hai vinto"
        else:
            print "Parita'"

game()
