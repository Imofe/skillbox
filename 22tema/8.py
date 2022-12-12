def get_frequency(text):
    dict = {}
    count = 0

    for char in text:
        if ord('a') <= ord(char) <= ord('z'):
            dict[char] = dict.get(char, 0) + 1
            count += 1

    frequency = [(char, "{:5.3f}".format(dict[char] / count)) for char in dict.keys()]
    frequency.sort(key=lambda x: x[0])
    frequency.sort(key=lambda x: x[1], reverse=True)
    return frequency


text = open("22tema/text.txt", "r").read().lower()

analysis = open("22tema/analysis.txt", "w")
analysis.write("\n".join([char_data[0] + " " + char_data[1] for char_data in get_frequency(text)]))
analysis.close()