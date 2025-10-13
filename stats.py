def count_words(text):
    words = text.split()

    return len(words)

def count_chars(text):
    lower_text = text.lower()
    chars = {}

    for char in lower_text:

        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
        
    return chars

def sort_dict(dictionary):
    list_of_char_dicts = []

    for char in dictionary:
        new_dict = {"char": char, "num": dictionary[char]}
        list_of_char_dicts.append(new_dict)

    list_of_char_dicts.sort(reverse=True, key=get_character_count)

    return list_of_char_dicts

def get_character_count(character_dictionary):
    return character_dictionary["num"]
