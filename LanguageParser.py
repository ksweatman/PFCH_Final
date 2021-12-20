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

feat_corpus = ''
feat_corpus_list = []
file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)
next(data,None)
for row in data:
    feat_corpus = feat_corpus + row[15] + ' '
    feat_corpus_list.append(row[15])


#tokenize words, convert to lowercase
feat_tokens = nltk.word_tokenize(feat_corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of feat_filtered_tokens with stopwords removed

stop_words = set(stopwords.words('english'))
feat_filtered_tokens = []

for word in feat_tokens:
    if not word in stop_words:
        feat_filtered_tokens.append(word)

# print length of feat_corpus_list (Number of rows), tokens list (number of words), and feat_filtered_tokens list (number of words minus stopwords)

#print(len(feat_corpus_list), len(tokens), len(filtered_tokens))

# print list of all words
#print(feat_tokens)

# print list of all words minus stopwords
#print(feat_filtered_tokens)

# Transform word lists (feat_tokens) into NLTK Text objects

feat_text = nltk.Text(feat_tokens)

feat_filtered_text = nltk.Text(feat_filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

feat_freq_dist = FreqDist(feat_tokens)

feat_freq_dist_filtered = FreqDist(feat_filtered_tokens)

#plot of top 25 tokens

#print(feat_freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(feat_freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

feat_filter_words = dict([(m, n) for m, n in feat_freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better']])

#for key in sorted(feat_filter_words):
 #   print("%s: %s" % (key, feat_filter_words[key]))
 
feat_data_analysis = nltk.FreqDist(feat_filter_words)
#feat_data_analysis.plot(25, cumulative=False)

## Creating FreqDist for filtered_words, keeping the 25 most common tokens
feat_all_fdist = FreqDist(feat_filter_words).most_common(25)

## Conversion to Pandas series via Python Dictionary for easier plotting
feat_all_fdist = pd.Series(dict(feat_all_fdist))


#create bar plot from data above using same layout
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title('Top 25 Words in Survey Responses to "What feature(s) do you wish our website had?"')
plt.grid()

bar_plot = sns.barplot(x=feat_all_fdist.index, y=feat_all_fdist.values, ax=ax,palette='inferno')
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("Charts/sitefeatures.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(feat_text.collocations(n))

#plot wordcloud

feat_wordcloud = WordCloud(width = 800, height = 800,random_state=1,
    background_color ='white',colormap='inferno',
    min_font_size = 10).generate((str(feat_filter_words).replace("'","")))
 
#WordCloud image                      
plt.figure(figsize = (10, 10), facecolor = None)
plt.title('Survey Responses to "What feature(s) do you wish our website had?"')
plt.imshow(feat_wordcloud)
plt.axis("off")
ax.set_title('Survey Responses to "What feature(s) do you wish our website had?"', fontsize=48, color='black')
plt.tight_layout(pad = 10)

plt.savefig("Charts/featurecloud.png")

# Question: "What do you like about the library's current website?" in row [13]

#import survey data and convert to nltk corpus

like_corpus = ''
like_corpus_list = []
file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)

for row in data:
    like_corpus = like_corpus + row[13] + ' '
    like_corpus_list.append(row[13])

           
file.close()

#tokenize words, convert to lowercase
like_tokens = nltk.word_tokenize(like_corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens- tokens with stopwords removed

stop_words = set(stopwords.words('english'))
like_filtered_tokens = []

for word in like_tokens:
    if not word in stop_words:
        like_filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)

#print(len(like_corpus_list), len(like_tokens), len(like_filtered_tokens))

# print list of all words
#print(like_tokens)

# print list of all words minus stopwords
#print(like_filtered_tokens)

# Transform word lists (like_tokens) into NLTK Text objects

like_text = nltk.Text(like_tokens)

like_filtered_text = nltk.Text(like_filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

freq_dist = FreqDist(like_tokens)

freq_dist_filtered = FreqDist(like_filtered_tokens)

#plot of top 25 tokens

#print(freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

like_filter_words = dict([(m, n) for m, n in freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better','also','many']])

#for key in sorted(filter_words):
 #   print("%s: %s" % (key, like_filter_words[key]))
 
data_analysis = nltk.FreqDist(like_filter_words)
#data_analysis.plot(25, cumulative=False)

## Creating FreqDist for filtered_words, keeping the 25 most common tokens
all_fdist = FreqDist(like_filter_words).most_common(25)

## Conversion to Pandas series via Python Dictionary for easier plotting
all_fdist = pd.Series(dict(all_fdist))


#create bar plot from data in above cell using same layout
## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title('Top 25 Words in Survey Responses to "What do you like about the library website?"')
plt.grid()

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing

bar_plot = sns.barplot(x=all_fdist.index, y=all_fdist.values, ax=ax,palette='plasma')
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("Charts/sitelikes.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(like_text.collocations(n))

#plot wordcloud

likewordcloud = WordCloud(width = 800, height = 800,random_state=1,
    background_color ='white',colormap='plasma',
    min_font_size = 10).generate((str(like_filter_words).replace("'","")))
 
#WordCloud image                      
plt.figure(figsize = (10, 10), facecolor = None)
plt.title('Survey Responses to "What do you like about the library website?"')
plt.imshow(likewordcloud)
plt.axis("off")
ax.set_title('Survey Responses to "What do you like about the library website?"', fontsize=48, color='black')
plt.tight_layout(pad = 10)
 
plt.savefig("Charts/likecloud.png")

# Question: "What do you dislike about the library's current website?" in row [14]

#import survey data and convert to nltk corpus

dislike_corpus = ''
dislike_corpus_list = []
file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)

for row in data:
    dislike_corpus = dislike_corpus + row[14] + ' '
    dislike_corpus_list.append(row[14])

           
file.close()

#tokenize words, convert to lowercase
dislike_tokens = nltk.word_tokenize(dislike_corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens- tokens with stopwords removed

stop_words = set(stopwords.words('english'))
dislike_filtered_tokens = []

for word in dislike_tokens:
    if not word in stop_words:
        dislike_filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)
#print(len(dislike_corpus_list), len(dislike_tokens), len(dislike_filtered_tokens))

# print list of all words
#print(dislike_tokens)

# print list of all words minus stopwords
#print(dislike_filtered_tokens)

# Transform word lists (dislike_tokens) into NLTK Text objects

dislike_text = nltk.Text(dislike_tokens)

dislike_filtered_text = nltk.Text(dislike_filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

dislike_freq_dist = FreqDist(dislike_tokens)

dislike_freq_dist_filtered = FreqDist(dislike_filtered_tokens)

#plot of top 25 tokens

#print(dislike_freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(dislike_freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

dislike_filter_words = dict([(m, n) for m, n in dislike_freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better','also','many','little','hard','sometimes','always','look']])

""" for key in sorted(dislike_filter_words):
    print("%s: %s" % (key, dislike_filter_words[key])) """
 
data_analysis = nltk.FreqDist(dislike_filter_words)
#data_analysis.plot(25, cumulative=False)

# Creating FreqDist for filtered_words, keeping the 25 most common tokens
dislike_all_fdist = FreqDist(dislike_filter_words).most_common(25)

# Conversion to Pandas series via Python Dictionary for easier plotting
dislike_all_fdist = pd.Series(dict(dislike_all_fdist))


#create bar plot from data in above cell using same layout
## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title('Top 25 Words in Survey Responses to "What do you dislike about the library website?"')
plt.grid()

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing

bar_plot = sns.barplot(x=dislike_all_fdist.index, y=dislike_all_fdist.values, ax=ax,palette='viridis')
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("Charts/sitedislikes.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(dislike_text.collocations(n))

#plot wordcloud

dislikewordcloud = WordCloud(width = 800, height = 800,random_state=1,
    background_color ='white',colormap='viridis',
    min_font_size = 10).generate((str(dislike_filter_words).replace("'","")))
 
#WordCloud image                      
plt.figure(figsize = (10, 10), facecolor = None)
plt.title('Survey Responses to "What do you like about the library website?"')
plt.imshow(dislikewordcloud)
plt.axis("off")
ax.set_title('Survey Responses to "What do you like about the library website?"', fontsize=48, color='black')
plt.tight_layout(pad = 10)
 
plt.savefig("Charts/dislikecloud.png")

# Question: "Are there any features of the library website that confuse you? If so, what are they?" in row [16]

confuse_corpus = ''
confuse_corpus_list = []
file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)

for row in data:
    confuse_corpus = confuse_corpus + row[16] + ' '
    confuse_corpus_list.append(row[16])

           
file.close()

#tokenize words, convert to lowercase
confuse_tokens = nltk.word_tokenize(confuse_corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens- tokens with stopwords removed

stop_words = set(stopwords.words('english'))
confuse_filtered_tokens = []

for word in confuse_tokens:
    if not word in stop_words:
        confuse_filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)
#print(len(confuse_corpus_list), len(confuse_tokens), len(confuse_filtered_tokens))

# print list of all words
#print(confuse_tokens)

# print list of all words minus stopwords
#print(confuse_filtered_tokens)

# Transform word lists (confuse_tokens) into NLTK Text objects

confuse_text = nltk.Text(confuse_tokens)

confuse_filtered_text = nltk.Text(confuse_filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

confuse_freq_dist = FreqDist(confuse_tokens)

confuse_freq_dist_filtered = FreqDist(confuse_filtered_tokens)

#plot of top 25 tokens

#print(confuse_freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(confuse_freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

confuse_filter_words = dict([(m, n) for m, n in confuse_freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better','also','many','little','hard','sometimes','always','look','pick','check','person','first','place','went','come','drop','confusing']])

#for key in sorted(confuse_filter_words):
#    print("%s: %s" % (key, confuse_filter_words[key])) 

data_analysis = nltk.FreqDist(confuse_filter_words)
#data_analysis.plot(25, cumulative=False)

# Creating FreqDist for filtered_words, keeping the 25 most common tokens
confuse_all_fdist = FreqDist(confuse_filter_words).most_common(25)

# Conversion to Pandas series via Python Dictionary for easier plotting
confuse_all_fdist = pd.Series(dict(confuse_all_fdist))


#create bar plot from data in above cell using same layout
## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title('Top 25 Words in Survey Responses to "What features of the library website that confuse you?"')
plt.grid()

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing

bar_plot = sns.barplot(x=confuse_all_fdist.index, y=confuse_all_fdist.values, ax=ax,palette='magma')
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("Charts/siteconfusion.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(confuse_text.collocations(n))


#plot wordcloud

confusewordcloud = WordCloud(width = 800, height = 800,random_state=1,
    background_color ='white',colormap='magma',
    min_font_size = 10).generate((str(confuse_filter_words).replace("'","")))
 
#WordCloud image                      
plt.figure(figsize = (10, 10), facecolor = None)
plt.title('Survey Responses to "What features of the library website that confuse you?"')
plt.imshow(confusewordcloud)
plt.axis("off")
ax.set_title('Survey Responses to "What features of the library website that confuse you?"', fontsize=48, color='black')
plt.tight_layout(pad = 10)
 
plt.savefig("Charts/confusecloud.png")

# Question: "Why do you come to the library in person? Check all that apply. - Other - Text" in row [3]

#import survey data and convert to nltk corpus

libuse_corpus = ''
libuse_corpus_list = []
file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)

for row in data:
    libuse_corpus = libuse_corpus + row[3] + ' '
    libuse_corpus_list.append(row[3])

           
file.close()

#tokenize words, convert to lowercase
libuse_tokens = nltk.word_tokenize(libuse_corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens- tokens with stopwords removed

stop_words = set(stopwords.words('english'))
libuse_filtered_tokens = []

for word in libuse_tokens:
    if not word in stop_words:
        libuse_filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)
#print(len(libuse_corpus_list), len(libuse_tokens), len(libuse_filtered_tokens))

# print list of all words
#print(libuse_tokens)

# print list of all words minus stopwords
#print(libuse_filtered_tokens)

# Transform word lists (libuse_tokens) into NLTK Text objects

libuse_text = nltk.Text(libuse_tokens)

libuse_filtered_text = nltk.Text(libuse_filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

libuse_freq_dist = FreqDist(libuse_tokens)

libuse_freq_dist_filtered = FreqDist(libuse_filtered_tokens)

#plot of top 25 tokens

#print(libuse_freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(libuse_freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

libuse_filter_words = dict([(m, n) for m, n in libuse_freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better','also','many','little','hard','sometimes','always','look','pick','check','person','first','place','went','come','drop']])

#for key in sorted(libuse_filter_words):
#    print("%s: %s" % (key, libuse_filter_words[key])) 
 
data_analysis = nltk.FreqDist(libuse_filter_words)
#data_analysis.plot(25, cumulative=False)

# Creating FreqDist for filtered_words, keeping the 25 most common tokens
libuse_all_fdist = FreqDist(libuse_filter_words).most_common(25)

# Conversion to Pandas series via Python Dictionary for easier plotting
libuse_all_fdist = pd.Series(dict(libuse_all_fdist))


#create bar plot from data in above cell using same layout
## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title('Top 25 Words in Survey Responses to "Why do you come to the library in-person?"')
plt.grid()

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing

bar_plot = sns.barplot(x=libuse_all_fdist.index, y=libuse_all_fdist.values, ax=ax)
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("Charts/libuselanguage.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(libuse_text.collocations(n))


# Question: "Why do you use the library website? Check all that apply. - Other - Text" in row [5]

#import survey data and convert to nltk corpus

webuse_corpus = ''
webuse_corpus_list = []
file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)

for row in data:
    webuse_corpus = webuse_corpus + row[5] + ' '
    webuse_corpus_list.append(row[5])

           
file.close()

#tokenize words, convert to lowercase
webuse_tokens = nltk.word_tokenize(webuse_corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens- tokens with stopwords removed

stop_words = set(stopwords.words('english'))
webuse_filtered_tokens = []

for word in webuse_tokens:
    if not word in stop_words:
        webuse_filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)
#print(len(webuse_corpus_list), len(webuse_tokens), len(webuse_filtered_tokens))

# print list of all words
#print(webuse_tokens)

# print list of all words minus stopwords
#print(webuse_filtered_tokens)

# Transform word lists (webuse_tokens) into NLTK Text objects

webuse_text = nltk.Text(webuse_tokens)

webuse_filtered_text = nltk.Text(webuse_filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

webuse_freq_dist = FreqDist(webuse_tokens)

webuse_freq_dist_filtered = FreqDist(webuse_filtered_tokens)

#plot of top 25 tokens

#print(webuse_freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(webuse_freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

webuse_filter_words = dict([(m, n) for m, n in webuse_freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better','also','many','little','hard','sometimes','always','look','pick','check','person','first','place','went','come','drop',]])

#for key in sorted(webuse_filter_words):
#    print("%s: %s" % (key, webuse_filter_words[key])) 
 
data_analysis = nltk.FreqDist(webuse_filter_words)
#data_analysis.plot(25, cumulative=False)

# Creating FreqDist for filtered_words, keeping the 25 most common tokens
webuse_all_fdist = FreqDist(webuse_filter_words).most_common(25)

# Conversion to Pandas series via Python Dictionary for easier plotting
webuse_all_fdist = pd.Series(dict(webuse_all_fdist))


#create bar plot from data in above cell using same layout
## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title('Top 25 Words in Survey Responses to "Why do you visit the library website?"')
plt.grid()

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing

bar_plot = sns.barplot(x=webuse_all_fdist.index, y=webuse_all_fdist.values, ax=ax,palette='cividis')
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("Charts/webuselanguage.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(webuse_text.collocations(n))

# Other Uses for other Library sites

#import survey data and convert to nltk corpus

otherlibuse_corpus = ''
otherlibuse_corpus_list = []

file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)

for row in data:
    otherlibuse_corpus=otherlibuse_corpus+row[20]+' '
    otherlibuse_corpus_list.append(row[20])
    otherlibuse_corpus=otherlibuse_corpus+row[24]+' '
    otherlibuse_corpus_list.append(row[24])
    otherlibuse_corpus=otherlibuse_corpus+row[28]+' '
    otherlibuse_corpus_list.append(row[28])
    otherlibuse_corpus = otherlibuse_corpus + row[32] + ' '
    otherlibuse_corpus_list.append(row[32])
    otherlibuse_corpus=otherlibuse_corpus+row[36]+' '
    otherlibuse_corpus_list.append(row[36])
    otherlibuse_corpus=otherlibuse_corpus+row[40]+' '
    otherlibuse_corpus_list.append(row[40])


#tokenize words, convert to lowercase
otherlibuse_tokens = nltk.word_tokenize(otherlibuse_corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens- tokens with stopwords removed

stop_words = set(stopwords.words('english'))
otherlibuse_filtered_tokens = []

for word in otherlibuse_tokens:
    if not word in stop_words:
        otherlibuse_filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)
#print(len(otherlibuse_corpus_list), len(otherlibuse_tokens), len(otherlibuse_filtered_tokens))

# print list of all words
#print(otherlibuse_tokens)

# print list of all words minus stopwords
#print(otherlibuse_filtered_tokens)

# Transform word lists (otherlibuse_tokens) into NLTK Text objects

otherlibuse_text = nltk.Text(otherlibuse_tokens)

otherlibuse_filtered_text = nltk.Text(otherlibuse_filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

otherlibuse_freq_dist = FreqDist(otherlibuse_tokens)

otherlibuse_freq_dist_filtered = FreqDist(otherlibuse_filtered_tokens)

#plot of top 25 tokens

#print(otherlibuse_freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(otherlibuse_freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

otherlibuse_filter_words = dict([(m, n) for m, n in otherlibuse_freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better','also','many','little','hard','sometimes','always','look','pick','check','person','first','place','went','come','drop','visit']])

#for key in sorted(otherlibusefilter_words):
#    print("%s: %s" % (key, otherlibuse_filter_words[key])) 

data_analysis = nltk.FreqDist(otherlibuse_filter_words)
#data_analysis.plot(25, cumulative=False)

# Creating FreqDist for filtered_words, keeping the 25 most common tokens
otherlibuse_all_fdist = FreqDist(otherlibuse_filter_words).most_common(25)

# Conversion to Pandas series via Python Dictionary for easier plotting
otherlibuse_all_fdist = pd.Series(dict(otherlibuse_all_fdist))


#create bar plot from data in above cell using same layout
## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title("Top 25 Words in Survey Responses to 'Why do you use [other library]'s website?'")
plt.grid()

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing

bar_plot = sns.barplot(x=otherlibuse_all_fdist.index, y=otherlibuse_all_fdist.values, ax=ax)
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("Charts/otherlibotheruse.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(otherlibuse_text.collocations(n))

# Other Likes for other Library Sites

#import survey data and convert to nltk corpus

otherliblike_corpus = ''
otherliblike_corpus_list = []

file = open("SurveyData.csv","r",encoding="utf-8")
data = csv.reader(file)

for row in data:
    otherliblike_corpus=otherliblike_corpus+row[22]+' '
    otherliblike_corpus_list.append(row[22])
    otherliblike_corpus=otherliblike_corpus+row[26]+' '
    otherliblike_corpus_list.append(row[26])
    otherliblike_corpus=otherliblike_corpus+row[30]+' '
    otherliblike_corpus_list.append(row[30])
    otherliblike_corpus = otherliblike_corpus + row[34] + ' '
    otherliblike_corpus_list.append(row[34])
    otherliblike_corpus=otherliblike_corpus+row[38]+' '
    otherliblike_corpus_list.append(row[38])
    otherliblike_corpus=otherliblike_corpus+row[42]+' '
    otherliblike_corpus_list.append(row[42])


#tokenize words, convert to lowercase
otherliblike_tokens = nltk.word_tokenize(otherliblike_corpus.lower())

# create stop_words variable from NLTK stopwords
# create new list of filtered_tokens- tokens with stopwords removed

stop_words = set(stopwords.words('english'))
otherliblike_filtered_tokens = []

for word in otherliblike_tokens:
    if not word in stop_words:
        otherliblike_filtered_tokens.append(word)

# print length of corpus_list (Number of rows), tokens list (number of words), and filtered_tokens list (number of words minus stopwords)
#print(len(otherliblike_corpus_list), len(otherliblike_tokens), len(otherliblike_filtered_tokens))

# print list of all words
#print(otherliblike_tokens)

# print list of all words minus stopwords
#print(otherliblike_filtered_tokens)

# Transform word lists (otherliblike_tokens) into NLTK Text objects

otherliblike_text = nltk.Text(otherliblike_tokens)

otherliblike_filtered_text = nltk.Text(otherliblike_filtered_tokens)

# Create a frequency distribution of all words (how often a word appears in text)

otherliblike_freq_dist = FreqDist(otherliblike_tokens)

otherliblike_freq_dist_filtered = FreqDist(otherliblike_filtered_tokens)

#plot of top 25 tokens

#print(otherliblike_freq_dist.plot(25, cumulative=False))

#plot of top 25 filtered tokens

#print(otherliblike_freq_dist_filtered.plot(25, cumulative=False))

#clean up data based on initial plots

otherliblike_filter_words = dict([(m, n) for m, n in otherliblike_freq_dist_filtered.items() if len(m) > 3 and m not in ['would','think','sure','like','know','sure','maybe','could','much','wish','better','also','many','little','hard','sometimes','always','look','pick','check','person','first','place','went','come','drop','visit','nypl','great','used']])

#for key in sorted(otherliblikefilter_words):
#    print("%s: %s" % (key, otherliblike_filter_words[key])) 

data_analysis = nltk.FreqDist(otherliblike_filter_words)
#data_analysis.plot(25, cumulative=False)

# Creating FreqDist for filtered_words, keeping the 25 most common tokens
otherliblike_all_fdist = FreqDist(otherliblike_filter_words).most_common(25)

# Conversion to Pandas series via Python Dictionary for easier plotting
otherliblike_all_fdist = pd.Series(dict(otherliblike_all_fdist))


#create bar plot from data in above cell using same layout
## Setting figure, ax into variables
fig, ax = plt.subplots(figsize=(10,10))

ax.set_ylabel('Number of Occurrences')
ax.set_xlabel('Word')
plt.title("Top 25 Words in Survey Responses to 'What do you like about [other library]'s website?'")
plt.grid()

## Seaborn plotting using Pandas attributes + xtick rotation for ease of viewing

bar_plot = sns.barplot(x=otherliblike_all_fdist.index, y=otherliblike_all_fdist.values, ax=ax,palette='turbo')
ax.set_ylim(ymin=0)
plt.xticks(rotation=45)
plt.savefig("Charts/otherlibotherlike.png")

# prints top n of collocates in text (how often words appear next to one another, in pairs)

n = 25
print(otherliblike_text.collocations(n))

