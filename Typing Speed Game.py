# Typing speed game
import time
import random
from Word_List import word_list

sentence_rand = random.sample(word_list, 10)
sentence_rand_together = " ".join(sentence_rand)
sentence = sentence_rand_together


def user_input():
    print(sentence)
    tic = time.perf_counter()
    user_typing = input("Please type the sentence above. ")
    toc = time.perf_counter()
    total_time = toc - tic

    sentence_words = sentence_rand

    user_words = user_typing.split()

    not_in_sentence = set(sentence_words).difference(set(user_words))

    correct_percent = (len(sentence_words) - len(not_in_sentence)) / len(sentence_words)
    print("Accuracy: " + str(correct_percent * 100) + "%")
    wpm = ((len(sentence_words) - len(not_in_sentence)) / total_time) * 60
    print("Your WPM is " + str(round(wpm, 0)))


user_input()
