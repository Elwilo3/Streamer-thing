import os
import chardet

blacklist = ['1']  # list of unwanted words

word_count = {}
unique_chatters = set()

for filename in os.listdir():
    if filename.endswith('.txt'):  # only process text files
        with open(filename, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']

        with open(filename, 'r', encoding=encoding) as f:
            for line in f:
                words = line.strip().split()
                chatter = words[0].split('!')[0]  # extract chatter username
                unique_chatters.add(chatter)  # add to set of unique chatters
                for word in words[1:]:
                    if word not in blacklist:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1

print(f'Total unique chatters: {len(unique_chatters)}')
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:15]:
    print(f'{word}: {count}')
