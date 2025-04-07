#Домашнее задание 9.1
def popular_words(text, words):
    text = text.lower()
    text_words = text.split()
    result = {}
    for word in words:
        count = 0
        for w in text_words:
            if w == word:
                count += 1
        result[word] = count
    return result

assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
) == {
    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
}, 'Test1'


print('OK')

#Домашнее задание 9.2
def difference(*args):
    if not args:
        return 0
    min_val = min(args)
    max_val = max(args)
    return round(max_val - min_val, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'


print('OK')
