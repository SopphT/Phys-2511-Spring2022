#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 14:05:01 2022

@author: sopyt
"""
from collections import Counter
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,6)

movies = open("movies.csv","r")

movie_titles = []
movie_genres = []
genre_list = ["Action","Adventure","Animation","Children","Comedy","Crime","Drama","Documentary",
              "Fantasy","Musical","Mystery","Romance","Thriller","Sci-Fi","War"]
bad_words = ["the","of","a","at","an","and","to","in","for","on","de","la","is", ""]


for line in movies:
    splitted_lines = line.split(",")
    movie_genres.append(splitted_lines[-1].strip("\n").split("|"))
    x = ' '.join(splitted_lines[1:-1])
    movie_titles.append(x[0:-7].strip())
    
movies.close()
print(len(movie_titles))

def group_by_genre(genre):
    movies_by_genre = []
    index = 0
    while index < len(movie_genres):
        if genre in movie_genres[index]:
            movies_by_genre.append(movie_titles[index])
        index = index + 1
    return movies_by_genre

def remove_bad_characters(word_list):
    words = []
    for word in word_list:
        words.append(word.strip("?!,.:;'/-_1234567890 )(*^@#$%^&0!"))
    return words

def remove_boring_words(word_list):
    good_words = []
    for word in word_list:
        if word not in bad_words:
            good_words.append(word)
    return good_words

def get_words_from_list(placeholder):
    words = []
    for word in placeholder:
        words.extend(word.lower().split(" "))
    return remove_boring_words(remove_bad_characters(words))

for genre in genre_list:
    counts = Counter(get_words_from_list(group_by_genre(genre)))
    top_ten_words = counts.most_common()[0:10]
    most_common_words, counts = zip(*top_ten_words)
    plt.bar(most_common_words, counts, width = 0.8)
    plt.xlabel("Words")
    plt.ylabel("Number of Occurrences")
    plt.title("Top 10 Most Common Words in the " + "\"" + (genre) + "\"" + " Genre")
    plt.annotate("source: MovieLens Tag Genome Dataset 2021", (0,0), (-40,-30), fontsize=9, textcoords='offset points')
    plt.show()
      

