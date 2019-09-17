class ParserError(Exception):
    pass


class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

# returns the next word


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# goes through the sentence figures out if the word is the same as expecting


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

# skips stop words, and goes through the list to the end


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

# finds out if there is a verb, and what it is


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

# finds out if there is a object, and what it is


def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

# figures out what to do if there is an implied subject


def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

# figures out if a sentence has all three components


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
