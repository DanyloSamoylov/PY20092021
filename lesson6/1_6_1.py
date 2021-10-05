
sentence_ = input('Please enter some words:')
words_ = sentence_.split(' ')
result_ = {}
for element in words_:
    if element in result_:
        result_[element] += 1
    else:
        result_[element] = 1

print(result_)
