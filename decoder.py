import re

RE_PLURAL_SEG = re.compile(r'(\<.+?\>)')

GENDERS = {
    'm': 'male',
    'f': 'female',
    'nb': 'non-binary',
    'o': 'other'
}

SHAPE_AND_FORM = {
    'h': 'human',
    's': 'spiritual',
    '~': 'shape-shifter',
    'm': 'mammal',
    'mc': 'canine',
    'mf': 'feline'
}

ORIGIN = {
    'b': 'born with body',
    't': 'traumagenic',
    'n': 'natural',
    'i': 'intentional',
    'u': 'unknown'
}


def decode_pluralcode(code: str):
    c = {}

    if code[0] == 'P':
        if code[1] != 'X':
            raise Exception('pluralcode version not implemented')
        c['version'] = code[2:code.index(' ')]

    # scan for headmate segments
    if not '<' in code:
        raise Exception('no headmates in pluralcode found or malformed code')

    m = RE_PLURAL_SEG.findall(code)
    for segment in m:
        headmate = {}
        if ':' in segment:
            headmate['name'] = segment[1:segment.index(':')]
            segment = segment[segment.index(':'):]

        for part in segment.split(' '):
            if part[0] == 'G':
                headmate['gender'] = GENDERS[part[1:]]

            elif part[0] == 'S':
                form = ""
                if part[1:] in SHAPE_AND_FORM:
                    form += SHAPE_AND_FORM[part[1:]]
                else:
                    form += part[1:]
                headmate['form'] = form

            elif part[0] == 'A':
                if part[1:] == 'x':
                    headmate['age'] = 'unknown'
                else:
                    headmate['age'] = int(part[1:])

            elif part[0] == 'O':
                headmate['origin'] = ORIGIN[part[1:2]]

        if 'headmates' in c:
            c['headmates'].append(headmate)
        else:
            c['headmates'] = [headmate]

    for part in code.split(' '):
        if part[0] == 'N':
            c['number'] = int(part[1:])
        elif part[0] == 'D':
            c['discovery'] = int(part[1:])
        elif part[0] == 'C':
            c['communication'] = int(part[1:])
        elif part[0] == 'Q':
            c['amnesia'] = int(part[1:])
        elif part[0] == 'W':
            c['openness'] = int(part[1:])

    return c


if __name__ == '__main__':
    plural = decode_pluralcode(
        "PX0.1 N2 D9 C5 Q8 W4 <Lara: Gf Sh A1 Oi> <Go S~ Ax Ot>")
    from json import dumps
    print(dumps(plural, indent=4))
    import sys
    sys.exit(0)
    try:
        from toml import dumps
        print(dumps(plural))
    except:
        pass
    try:
        from yaml import dump
        print(dump(plural))
    except:
        pass
