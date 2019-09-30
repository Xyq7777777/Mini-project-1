import fileinput

key1 = 'recommend'
key2 = 'like'
key3 = 'love'
key4 = 'best'
key5 = 'worth'
key6 = 'great'
key7 = 'good'
key8 = 'fantastic'
key9 = 'yummy'

count = 0

with open('twitter_stream_10tweets.txt') as f:
     content = str(f.readlines())

list_of_sentences = content.split(".")
for sentence in list_of_sentences:
    words = sentence.split(" ")
    for word in words:
        if word == key1 or word == key2 or word == key3 or word == key4 or word == key5 or word == key6 or word == key7 or word == key8 or word == key9:
           count = count + 1
           percentage = (count / 10) * 100

print("The total likes for this restaurant is: ", count)
print("The percentage would be: ", percentage, "%")
           