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