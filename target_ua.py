import random
import urllib.request

def generate_grid():
    symbols = ' а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с,\
     т, у, ф, х, ц, ч, ш, щ, ь, ю, я'
    symbols = symbols.split(", ")
    grid = []
    while len(grid) < 5:
        el = random.choice(symbols)
        if el not in grid:
            grid.append(el)
    return grid

def get_words(f, letters):
    f = 'https://raw.githubusercontent.com/shaman4ik14/whole/master/base.lst'
    amount_of_pair = []
    dict_of_pair = {}
    with urllib.request.urlopen(f) as webpage:
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
                dict_of_pair[i[0]] = 'noun'
            elif '/v' in i[1] or 'verb' in i[1]:
                dict_of_pair[i[0]] = 'verb'
            elif '/adj' in i[1] or 'adjective' in i[1]:
                dict_of_pair[i[0]] = 'adjective'
            elif 'adv' in i[1] or 'adverb' in i[1]:
                dict_of_pair[i[0]] = 'adverb'
    return dict_of_pair

def get_user_words():
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
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
    for element in user_words:
        if element[0] not in letters:
            user_words.remove(element)
    right_res = []
    wrong_res = []
    for el in user_words:
        if dict_of_words[el] == language_part:
            right_res.append(el)
        else:
            wrong_res.append(el)
    return right_res, wrong_res

def result_area():
    parts = ['noun', 'verb', 'adjective', 'adverb']
    language_part = random.choice(parts)
    letters = generate_grid()
    user_input = get_user_words()
    dict_of_words = get_words('a', letters)
    res = check_user_words(user_input, language_part, letters, dict_of_words)
    return res

print(result_area())