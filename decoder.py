def decode_pluralcode(code: str):
    c = {}

    for part in code.split(' '):
        if part[0] == 'P':
            if part[1] != 'X':
                raise Exception('pluralcode version not implemented')
            c['version'] = part[2:]

        elif part[0] == 'N':
            c['number'] = int(part[1:])
        elif part[0] == 'D':
            c['discovery'] = int(part[1:])
        elif part[0] == 'C':
            c['communication'] = int(part[1:])
        elif part[0] == 'Q':
            c['amnesia'] = int(part[1:])
        elif part[0] == 'W':
            c['openness'] = int(part[1:])
        
        elif part[0] == 'G':
            genders = []
            if 'genders' in c:
                genders = c['genders']
            
            gd = {
                'm': 'male',
                'f': 'female',
                'nb': 'non-binary',
                'o': 'other'
            }
            genders.append(gd[part[1:]])
            c['genders'] = genders

        elif part[0] == 'S':
            form = []
            if 'form' in c:
                form = c['form']
            
            gd = {
                'h': 'human',
                's': 'spiritual',
                '~': 'shape-shifter',
                'm': 'mammal',
                'mc': 'canine',
                'mf': 'feline'
            }
            if part[1:] in gd:
                form.append(gd[part[1:]])
            else:
                form.append(part[1:])
            c['form'] = form

        elif part[0] == 'A':
            age = []
            if 'age' in c:
                age = c['age']
            
            if part[1:] == 'x':
                age.append('unknown')
            else:
                age.append(int(part[1:]))
            c['age'] = age

        elif part[0] == 'O':
            origin = []
            if 'origin' in c:
                origin = c['origin']
            
            gd = {
                'b': 'born with body',
                't': 'traumagenic',
                'n': 'natural',
                'i': 'intentional',
                'u': 'unknown'
            }
            origin.append(gd[part[1:]])
            c['origin'] = origin

        

    return c

if __name__ == '__main__':
    print(decode_pluralcode("PX0.1 N2 D9 C5 Q8 W4 Gf Gnb Sh S~ A1 Ax Oi Ot"))