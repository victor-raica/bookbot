def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    count = {}
    for char in text:
        char = char.lower()
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return count


def sort_char_count(char_count):
    list_of_counts = [{'char': char, 'num': count} for char, count in char_count.items()]
    list_of_counts.sort(key=lambda x: x['num'], reverse=True)
    return list_of_counts