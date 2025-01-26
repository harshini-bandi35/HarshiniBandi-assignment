'''Word Counter
   - Create a program to count the occurrences of each word in a sentence provided bhiy the user.
'''
user_sentence=input("enter the sentence to find word count: ")
words=user_sentence.split() 
count_of_words={}
for i in words:
    i=i.lower()
    count_of_words[i]=count_of_words.get(i, 0)+1
for i,count in count_of_words.items():
    print(f"{i}:{count}")