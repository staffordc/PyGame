stuff = input('> ')


def scan(words):
    results = []
    directions = {'north', 'east', 'west', 'south'}
    verbs = {'go', '', 'eat'}
    stops = {'the', 'in', 'of', 'from', 'at', 'it'}
    nouns = {'door', 'bear', 'princess', 'cabinet'}

    words = convert_lower(words)

    splitwords = words.split()

    # loops through words and returns the set name with the word that was input
    for word in splitwords:
        if word in directions:
            results.append(('direction', word))
        elif word in verbs:
            results.append(('verb', word))
        elif word in stops:
            results.append(('stop', word))
        elif word in nouns:
            results.append(('noun', word))
        elif word.isdigit():
            numb = convert_numbers(word)
            results.append(('number', numb))
        else:
            results.append(('error', word))
    return results

# converts string inputs to int


def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

# converts uppercase inputs to lowercase


def convert_lower(a):
    try:
        return a.lower()
    except ValueError:
        return None
