# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 22:47:11 2022

@author: sophi
"""

import numpy as np
import matplotlib.pyplot as plt

full_text = open("frankenstein.txt", "r", encoding="utf8")

read_file = False

character_names = ["Victor","Agatha","Caroline","Lacey","Elizabeth"
                   ,"Ernest","Felix","Henry","Justine","William","TheCreature"]

book_text = []
for line in full_text:
    if "Chapter 24" in line:
        read_file = True
    if "*** END OF THE PROJECT GUTENBERG EBOOK FRANKENSTEIN ***" in line:
        read_file = False
    if read_file == True:
        book_text.append(line.lower())
book_text[0] = " "
full_text.close()

for i in range(0, len(book_text)):
    book_text[i] = book_text[i].replace("the creature", "thecreature")

labels = []
name_counter = []

chapter_number = 1
for chapter_number in range(1,25):
    labels.append(str(chapter_number))
    chapter_text = []
    for line in book_text:
        if "chapter " + str(chapter_number) in line:
            read_file = True
        if "chapter " + str(chapter_number + 1) in line:
            read_file = False
        if read_file == True:
            string_of_words = line.split()
            for word in string_of_words:
                word = word.strip(".,:;\"?!\'*)( ")
                chapter_text.append(word)
    print("\nChapter " + str(chapter_number) + "\n")
    this_chapter_counts = []            
    for name in character_names:
        print(name, chapter_text.count(name.lower()))
        this_chapter_counts.append(chapter_text.count(name.lower()))
    name_counter.append(this_chapter_counts)

# swap rows and columns
name_counter = np.array(name_counter).T

# time to plot
fig, ax = plt.subplots()
i = 0
for name_counts in name_counter:
    ax.plot(range(1,25),name_counts, label = character_names[i], linewidth = 3)
    i = i + 1

ax.set_ylabel('Times Name Mentioned Per Chapter')
ax.set_xlabel('Chapter Number')
ax.set_title('Names in Frankenstein')
ax.set_xticks(range(0,25))
ax.legend()

plt.show()

#I hope it's okay that I used https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
#I know this website was mentioned as a resource in class, but I was unsure if that also made it a resource for the lab
