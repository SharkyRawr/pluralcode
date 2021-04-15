if __name__ == '__main__':
    plural = decode_pluralcode(
        "PX0.1 N2 D9 C5 Q8 W4 <Lara: Gf Sh A1 Oi> <Go S~ Ax Ot>")
    from json import dumps
    print(dumps(plural, indent=4))
    try:
        from toml import dumps
        print(dumps(plural))
    except Exception as ex:
        print(ex)
    try:
        from yaml import dump
        print(dump(plural))
    except Exception as ex:
        print(ex)