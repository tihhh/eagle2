
def progressBar(perc):
    total = 100
    length = 10
    filled_length = int(length * perc/total)
    bar = '=' * filled_length + ' ' * (length - filled_length)
    return f'[{bar}] {perc:.2f}%'

intervals = (
    ('weeks', 604800),  
    ('days', 86400),    
    ('hours', 3600),    
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
