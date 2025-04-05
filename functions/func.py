import json, time, re

def progressBar(perc):
    total = 100
    length = 10
    filled_length = int(length * perc/total)
    bar = '█' * filled_length + '░' * (length - filled_length)
    return f'|{bar}| {perc:.2f}%'


def strip_all_markup(text):
    # Remove custom tags like <i=1>, <voice=3>, etc.
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove common Markdown symbols (bold, italic, strikethrough, inline code)
    text = re.sub(r'(\*\*|\*|__|_|~~|`)', '', text)
    
    # Remove HTML entities like &nbsp;, &lt;, etc. (optional)
    text = re.sub(r'&[a-zA-Z]+;', '', text)
    
    # Optional: Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


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

def time_until_target(target_timestamp):
    current_timestamp = int(time.time())
    time_difference = target_timestamp - current_timestamp
    
    return time_difference