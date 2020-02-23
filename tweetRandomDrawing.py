import turtle
import random
import tweepy
import collections



def getTweets(name):

    # personal details
    consumer_key = "eCpBUXRzDme1HAgZDpQBujXIH"
    consumer_secret = "Rdvvz9dWybTFG1RqB68EGVHFMoyElJU7gWtXd2lV5eJLLo7FJc"
    access_token = "1231350294144933889-fNgUqRuabgbs82mjUqfpK61SjQCM7A"
    access_token_secret = "oqXajRy9dO3DiBmGuv9Gww4nyB6pVoBS3uSqGFuamZb7n"

    # authentication of consumer key and secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # authentication of access token and secret
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    for tweet in tweepy.Cursor(api.user_timeline, screen_name = name, tweet_mode="extended").items(10):
        if not (tweet.full_text[0] == '@') and not (tweet.full_text[0] == 'R' and tweet.full_text[1] == 'T'):
            #print(tweet.full_text)
            print("\n")
            final = tweet
            break;

    return str(final.full_text)



tweetIn = input("Enter whose tweet you want drawn: ")

stringIn = getTweets(tweetIn)

print(stringIn)
kim = turtle.Turtle()
kim.pensize(7)
turtle.title(stringIn)
stringIn = stringIn.lower()

def toss():
    a=['left','right']
    return(random.choice(a))

def randColor():
    b=['red','cyan','skyblue','lightgreen','orange','purple','pink','brown','gold','turquoise','magenta','maroon']
    return(random.choice(b))
kim.color(randColor())

def charSplit(word):
	return list(word)


eachWord = stringIn.split()

#stringIn.replace(" ", "")
numChars = len(stringIn)
eachChar = charSplit(stringIn)


turtle.screensize(2000,1500)
for i in range(numChars):
	if eachChar[i] == 'e':
		direction = toss()
		newColor = randColor()
		if direction == 'left':
			kim.left(120)
			kim.forward(15)
		elif direction == 'right':
			kim.right(120)
			kim.forward(15)	
		kim.color(newColor)
	elif eachChar[i] == 't':
		newColor = randColor()
		kim.color(newColor)
		kim.forward(15)
	elif eachChar[i] == 'a':
		newColor = randColor()
		kim.color(newColor)
		kim.forward(15)
	elif eachChar[i] == 'o':
		for i in range(4):
			kim.forward(15)
			kim.right(20)
	elif eachChar[i] == 'i':
		for i in range(4):
			kim.forward(15)
			kim.left(20)
	elif eachChar[i] == 'n' or 'h':
		kim.left(45)
		kim.forward(15)
	elif eachChar[i] == 's' or 'r':
		kim.right(45)
		kim.forward(15)
	elif eachChar[i] == 'd' or 'c':
		kim.left(90)
		kim.forward(15)
	elif eachChar[i] == 'c' or 'u':
		kim.right(90)
		kim.forward(15)
	
turtle.done()


# print(eachChar)
# print(eachWord)
