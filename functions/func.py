import json

def progressBar(perc):
    total = 100
    length = 10
    filled_length = int(length * perc/total)
    bar = '+' * filled_length + '-' * (length - filled_length)
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

def loadJson(file_path):
    """
    Load a JSON file and return its contents as a dictionary.
    Returns None if the file cannot be loaded.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data  # Return the dictionary directly
    except FileNotFoundError:
        print(f"Error: JSON file not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return None
    except Exception as e:
        print(f"Error loading JSON from {file_path}: {e}")
        return None
