def numerize (x):
    ref = {
        "K": 1000,
        "M": 1000000
    }
    base = ""
    for char in x:
        if char.isdigit():
            base += char
        else:
            prefix = char
    number = int(base) * ref[prefix]
    return number

