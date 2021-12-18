import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.util import ngrams
import pandas as pd
import matplotlib.pyplot as plt
from numpy import spacing

import collections, operator
import csv
import seaborn as sns
from wordcloud import WordCloud

nltk.download('stopwords')

nltk.download('punkt')


#Sample Question: "What feature(s) do you wish our website had?" in row [15]

#import survey data and convert to nltk corpus

corpus = ''
corpus_list = []
file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)
next(data,None)
for row in data:
    corpus = corpus + row[15] + ' '
    corpus_list.append(row[15])


#tokenize words, convert to lowercase
tokens = nltk.word_tokenize(corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens with stopwords removed

stop_words = set(stopwords.words('english'))
filtered_tokens = []

for word in tokens:
    if not word in stop_words:
        filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)

#print(len(corpus_list), len(tokens), len(filtered_tokens))

# print list of all words
#print(tokens)

# print list of all words minus stopwords
#print(filtered_tokens)

# Transform word lists (tokens) into NLTK Text objects

text = nltk.Text(tokens)

filtered_text = nltk.Text(filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

freq_dist = FreqDist(tokens)

freq_dist_filtered = FreqDist(filtered_tokens)

#plot of top 25 tokens

#print(freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

filter_words = dict([(m, n) for m, n in freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better']])

#for key in sorted(filter_words):
 #   print("%s: %s" % (key, filter_words[key]))
 
data_analysis = nltk.FreqDist(filter_words)
#data_analysis.plot(25, cumulative=False)

## Creating FreqDist for filtered_words, keeping the 25 most common tokens
all_fdist = FreqDist(filter_words).most_common(25)

## Conversion to Pandas series via Python Dictionary for easier plotting
all_fdist = pd.Series(dict(all_fdist))


#create bar plot from data above using same layout

fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title('Top 25 Words in Survey Responses to "What feature(s) do you wish our website had?"')
plt.grid()

bar_plot = sns.barplot(x=all_fdist.index, y=all_fdist.values, ax=ax)
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("sitefeatures.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(text.collocations(n))

#plot wordcloud

wordcloud = WordCloud(width = 800, height = 800,random_state=1,
    background_color ='white',colormap='gist_heat',
    min_font_size = 10).generate(str(filter_words))
 
#WordCloud image                      
plt.figure(figsize = (10, 10), facecolor = None)
plt.title('Survey Responses to "What feature(s) do you wish our website had?"')
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.savefig("featurecloud.png")
