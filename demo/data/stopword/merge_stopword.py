input_files = ['1.txt', '2.txt', '3.txt', '4.txt']

stopwords = set()

for file_name in input_files:
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            stopword = line.strip().replace(' ', '_')
            stopwords.add(stopword)

sorted_stopwords = sorted(stopwords)

with open('stopword.txt', 'w', encoding='utf-8') as output_file:
    for stopword in sorted_stopwords:
        output_file.write(stopword + '\n')