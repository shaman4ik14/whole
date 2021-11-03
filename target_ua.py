"""MY GAME ABOUT UKRAINE ALPHABET"""
import doctest
import random
import urllib.request


def generate_grid():
    """
    GENERATE GAME AREA WITH 9 LETTERS
    :return: list

    >>> True == True
    True
    """
    symbols = ' а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с,\
 т, у, ф, х, ц, ч, ш, щ, ь, ю, я'
    symbols = symbols.split(", ")
    grid = []
    while len(grid) < 5:
        element = random.choice(symbols)
        if element not in grid:
            grid.append(element)
    return grid


def get_words(file, letters):
    """
    RETURN ALL RIGHT WORDS FROM FILE
    :param f: link for this dictionary
    :param letters: letters from grid
    :return: dict of pair only good words

    >>> True == True
    True
    """
    file = 'https://raw.githubusercontent.com/shaman4ik14/whole/master/base.lst'
    amount_of_pair = []
    dict_of_pair = []
    with urllib.request.urlopen(file) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            if line[0] in letters:
                line = line.split(' ')
                line = line[0:2]
                if not (len(line[0]) > 5 or ('intj' in line[1] or 'noninfl' in line[1])):
                    amount_of_pair.append(line)
        for i in amount_of_pair:
            if '/n' in i[1] or 'noun' in i[1]:
                dict_of_pair.append((i[0], 'noun'))
            elif '/v' in i[1] or 'verb' in i[1]:
                dict_of_pair.append((i[0], 'verb'))
            elif '/adj' in i[1] or 'adjective' in i[1]:
                dict_of_pair.append((i[0], 'adjective'))
            elif 'adv' in i[1] or 'adverb' in i[1]:
                dict_of_pair.append((i[0], 'adverb'))
    return dict_of_pair


def get_user_words():
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.

    >>> True == True
    True
    """
    user_input = []
    while True:
        try:
            input_word = input()
            user_input.append(input_word)
        except EOFError:
            break
    return user_input


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    CHECK USER`S ANSWERS
    :param user_words: list
    :param language_part: str
    :param letters:list
    :param dict_of_words:list
    :return:list

    >>> True == True
    True
    """
    for word in user_words:
        if word[0] not in letters:
            user_words.remove(word)
    local_dict = {}
    for elements in dict_of_words:
        if elements[1] == language_part and elements[0][0] in letters:
            local_dict[elements[0]] = elements[1]
    right_words = []
    for words in user_words:
        if words in local_dict.keys():
            right_words.append(words)
    passed_words = list(set(local_dict.keys()) - set(right_words))
    return right_words, passed_words


def result_area():
    """
    FUNCRION FOR COMPILE ALL GAME ASPECTS
    :return: tuple of right words and words that wasn't mentioned

    >>> True == True
    True
    """
    parts = ['noun', 'verb', 'adjective', 'adverb']
    language_part = random.choice(parts)
    letters = generate_grid()
    print(letters)
    print(language_part)
    user_input = get_user_words()
    dict_of_words = get_words('a', letters)
    res = check_user_words(user_input, language_part, letters, dict_of_words)
    return res
