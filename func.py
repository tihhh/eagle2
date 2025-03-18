
def progressBar(perc):
    total = 100
    length = 10
    filled_length = int(length * perc/total)
    bar = '=' * filled_length + ' ' * (length - filled_length)
    return f'[{bar}] {perc:.2f}%'