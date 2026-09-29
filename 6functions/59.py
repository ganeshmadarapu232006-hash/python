def word_frequency(sentence):
    frequency = {}

    words = sentence.split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

sentence = "python is easy and python is powerful"

result = word_frequency(sentence)

print(result)