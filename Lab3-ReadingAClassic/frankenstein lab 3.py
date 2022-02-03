# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 22:47:11 2022

@author: sophi
"""

full_text = open("frankenstein.txt", "r", encoding="utf8")

read_file = False

character_names = ["Victor", "creature","Agatha","Caroline","Lacey","Elizabeth"
                   ,"Ernest","Felix","Henry","Justine","William"]

book_text = []
for line in full_text:
    if "Chapter 24" in line:
        read_file = True
    if "*** END OF THE PROJECT GUTENBERG EBOOK FRANKENSTEIN ***" in line:
        read_file = False
    if read_file == True:
        book_text.append(line)
book_text[0] = " "

#4 letters
#24 chapters
letter_number = 1
for letter_number in range(1,5):
    chapter_text = []
    for line in book_text:
        if "Letter " + str(letter_number) in line:
            read_file = True
        if "Letter " + str(letter_number + 1) in line or "Chapter 1" in line:
            read_file = False
        if read_file == True:
            string_of_words = line.split()
            for word in string_of_words:
                word = word.strip(".,:;\"?!\'*)( ")
                chapter_text.append(word)
    print("\nLetter " + str(letter_number) + "\n")            
    for name in character_names:
        print(name, chapter_text.count(name))
        
chapter_number = 1
for chapter_number in range(1,25):
    chapter_text = []
    for line in book_text:
        if "Chapter " + str(chapter_number) in line:
            read_file = True
        if "Chapter " + str(chapter_number + 1) in line:
            read_file = False
        if read_file == True:
            string_of_words = line.split()
            for word in string_of_words:
                word = word.strip(".,:;\"?!\'*)( ")
                chapter_text.append(word)
    print("\nChapter " + str(chapter_number) + "\n")            
    for name in character_names:
        print(name, chapter_text.count(name))
        
    
   

    


        
        
"""
string_of_words = line.split()
        
        
      
    for word in string_of_words:
        word = word.strip(".,:;\"?!\'*)( ")
        list_of_words.append(word)
        """
# *** END OF THE PROJECT GUTENBERG EBOOK FRANKENSTEIN ***

