# EC 601 Mini Project 1：Tweet4Like

For the owner of the restaurants, they can simply type in the name of their restaurants and then get the result of liking judgement based on comments on Twitter. The input name of the restaurant and “number of tweets to handle” can be determined by users, which enable a more flexible option. Therefore, they can easily know how many tweets like their restaurant and the percentage of it. This may help to improve their service, menu, dishes. Customers may conceive the improvement when visiting next time.

## User stories

I, the owner of restaurants, would like to know the current popular choice of food or drinks (what kinds of products should be released).  
I, the owner of restaurants, would like to know the comments (like, dislike, suggestions) on my store from customers.  
I, the owner of restaurants, would like to know which marketing strategies (promotions, advertisements, discounts, events) will have the most positive reflect.  
I, the customer, would like to know what is the percentage of positive comments.
 
 
## Architecture

<img src= "https://github.com/Xyq7777777/Mini-project-1/raw/master/Architecture.png">
 
## How to build your system

Our design is consist of Twitter API for developers and python codes. The API helps us grab tweets with specific terms on Twitter. The python codes enable us to reorder the tweets and then analyze it. The results can be shown on the terminal for users.


## Running the tests

(1) Download our resources in github.
    
   <img src= "https://github.com/Xyq7777777/Mini-project-1/raw/master/download.png">

(2) Open Oracle VM VirtualBox and put this documents in a folder.

(3) Open terminal in this folder.

   <img src= "https://github.com/Xyq7777777/Mini-project-1/raw/master/terminal.png">
    
(4) Type python twitter_stream.py
  
   <img src= "https://github.com/Xyq7777777/Mini-project-1/raw/master/terminal.png">
   
(5)


## Work distribution

Yaqun was in charge of module 1 which is getting users' tweets from twitter.
Yi-Wei was in charge of module 2 which is related to the analysis of the grabbed tweets.

## Lessons learned

### Yaqun Xia

In this project I was in charge of the twitter API.In my part, I learned a developer's basic use of the twitter API.I learned about the connection between twitter and python and the use of some commands.I learned how to format the information I got from twitter and to get the information I needed.I learned how to use github to record my project.

### Yi-Wei Chen

In this process, I learned how to accomplish the job using python. To be specific, how to read lines in txt files, how to search specific terms in lines, how to make a correct judgement based on keys. These stratagies are new to me which I was learning by doing. This is the first time for me using Github to complete a group project which I found is convenient for projects in teamwork. Throughout the discussion with my teammate, we eventually built a small system by ourselves from none which is a great accomplish in my point of view. The experience and lessons learned from this mini-project could be my motivation to start the next one.

## Future improvements

The part we think could be better is that we should use the existing tools, namely, Google API to help us to do the judgement for it is already built and is with higher accuracy than our code. This caused by not having a full exploring to current tools available. Another thing could be done better is that we did not develop an user interface which may cause the difficulty of using for general users. This is caused by not having enough experience of application development.
