# Typing speed game
import time
import random

sentence = "There seems to be an unusual amount of pigeons here."


def user_input():
    tic = time.perf_counter()
    print(sentence)
    user_typing = input("Please type the sentence above. ")
    toc = time.perf_counter()
    total_time = toc - tic

    sentence_words = sentence.split()
    sentence_word_num = len(sentence_words)

    user_words = user_typing.split()
    user_word_num = len(user_words)

    not_in_sentence = set(sentence_words).difference(set(user_words))

    correct_percent = (len(sentence_words) - len(not_in_sentence)) / len(sentence_words)
    print("Accuracy: " + str(correct_percent * 100) + "%")
    wpm = ((len(sentence_words) - len(not_in_sentence)) / total_time) * 60
    print("Your WPM is " + str(round(wpm, 0)))


user_input()
