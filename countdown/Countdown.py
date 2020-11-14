import random
import time


vowels = "aaaaaaaaaeeeeeeeeeeiiiiiiiiioooooooo"
consonants = "bbccddddffggghhjkllllmmnnnnnnppqrrrrrrssssttttttvvwwxyyz"
totalletters=[]
words=[]
longest=[]
score=0

def select_characters(choice):
    n=choice
    while (n>0):
        choice=input("type v for vowel or c for consonant: ")
        if (choice=="v" or choice=="V"):
            vowel()
            n-=1
        elif (choice == "c" or choice == "C"):
            consonant()
            n-=1
        else:
            print("please enter a valid input")
    print(totalletters)

def dictionary_reader(choice):
    available=open("Availablewords.txt","w")
    available.write("")
    available.close
    print("please wait while we generate words")
    with open("words.txt") as f:
        for i in f:
            if len(i) <= choice:
                available= open("Availablewords.txt","a")
                available.write(i)
                available.close()

def vowel():
    vletter=vowels[random.randint(0,36)]
    totalletters.append(vletter)
    print(vletter)

def consonant():
    cletter=consonants[random.randint(0,55)]
    totalletters.append(cletter)
    print(cletter)

def word_lookup(word):
    score = 0

    for char in word:
        for i in totalletters:
            if char == i:
                score+=1
                totalletters.remove(i)
                break
    
    with open("words.txt") as f:
        if word in f.read() and score > 0:
            print("your word exists, your score: ", score)
        else:
            print("your word doesn't exist")
    
    if score < len(word):
        print("you cannot make that word")
        score=0
    with open("Availablewords.txt","r") as file:
        for word in file:
            words.append(word)

choice=int(input("please enter the length you want to play: "))
dictionary_reader(choice)
select_characters(choice)

timeleft=30
while (timeleft > 0):
    print(timeleft)
    timeleft -= 1
    time.sleep(1)

word=input("please enter your answer: ")
word_lookup(word)