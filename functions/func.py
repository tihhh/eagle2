
def progressBar(perc):
    total = 100
    length = 10
    filled_length = int(length * perc/total)
    bar = '=' * filled_length + ' ' * (length - filled_length)
    return f'[{bar}] {perc:.2f}%'

intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)
def timeConvert(seconds, granularity=2):
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])
