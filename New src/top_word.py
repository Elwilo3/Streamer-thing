import os
import chardet

blacklist = [
    'the', 'a', 'an', 'and', 'or', 'in', 'of', 'to', 'for', 'on', 'at', 'with', 'you', 'i',
    'is', 'it', 'that', 'this', 'not', 'be', 'are', 'was', 'were', 'am', 'been', 'has', 'have',
    'had', 'do', 'does', 'did', 'can', 'could', 'will', 'would', 'should', 'must', 'might', 'may',
    'who', 'what', 'where', 'when', 'why', 'how', 'which', 'there', 'their', 'they', 'them',
    'he', 'she', 'his', 'her', 'him', 'its', 'we', 'us', 'our', 'your', 'yours', 'my', 'mine',
    'their', 'theirs', 'any', 'all', 'every', 'each', 'some', 'such', 'many', 'much', 'more',
    'most', 'several', 'few', 'enough', 'other', 'another', 'also', 'even', 'just', 'than',
    'then', 'now', 'ever', 'still', 'already', 'yet', 'however', 'therefore', 'thus', 'moreover',
    'though', 'although', 'even though', 'unless', 'except', 'but', 'with', 'without', 'about',
    'above', 'across', 'after', 'against', 'among', 'around', 'before', 'behind', 'below', 'beneath',
    'beside', 'between', 'beyond', 'by', 'down', 'during', 'except', 'from', 'inside', 'into', 'like',
    'near', 'off', 'on', 'onto', 'outside', 'over', 'past', 'since', 'through', 'throughout', 'toward',
    'under', 'until', 'up', 'upon', 'within', 'without', 'yet', 'you', 'your', 'yours', 'he', 'him',
    'his', 'she', 'her', 'hers', 'it', 'its', 'we', 'us', 'our', 'ours', 'they', 'them', 'their',
    'theirs', 'i', 'me', 'my', 'mine', 'yourself', 'yourselves', 'himself', 'herself', 'itself',
    'ourselves', 'themselves', 'anybody', 'anyone', 'anything', 'each', 'either', 'everybody',
    'everyone', 'everything', 'neither', 'nobody', 'no one', 'nothing', 'one', 'other', 'somebody',
    'someone', 'something', 'both', 'few', 'many', 'several', 'all', 'most', 'some', 'no', 'none',
    'any', 'enough', 'every', 'each', 'much', 'more', 'some', 'such', 'that', 'these', 'those',
    'and', 'but', 'for', 'nor', 'or', 'so', 'yet', 'with', 'although', 'as', 'because', 'if',
    'since', 'when', 'while', 'where', 'whether','I','1','https','good','time','get','chat','gem','hidden','raid','Avghans','avghans','2', 'u','3','im','got']
  # list of unwanted words

# initialize word count dictionary
word_count = {}

# loop through all files in directory
for filename in os.listdir():
    if filename.endswith('.txt'):  # only process text files
        # detect the encoding of the file
        with open(filename, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']
        
        # count the words in the file
        with open(filename, 'r', encoding=encoding) as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    if word not in blacklist:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1

# sort the word_count dictionary by values in descending order and output the top 10 words
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:15]:
    print(f'{word}: {count}')
