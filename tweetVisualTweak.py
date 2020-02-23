import turtle
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
jade = turtle.Turtle()
jade.pensize(7)
turtle.title(stringIn)
stringIn = stringIn.lower()



def charSplit(word):
	return list(word)


eachWord = stringIn.split()

#stringIn.replace(" ", "")
numChars = len(stringIn)
eachChar = charSplit(stringIn)

jade.color('grey')
#e t a o i n s r h l d c u m f p g w y b v k x j q z
turtle.screensize(2000,1500)
for i in range(numChars):
	if eachChar[i] == 'e':
		jade.forward(10)
	elif eachChar[i] == 't':
		jade.dot(11)
	elif eachChar[i] == 'a':
		jade.right(45)
		jade.forward(15)
	elif eachChar[i] == 'o':
		jade.left(45)
		jade.forward(15)
	elif eachChar[i] == 'i':
		for i in range(5):
			jade.forward(10)
			jade.left(15)
	elif eachChar[i] == 'n':
		for i in range(5):
			jade.forward(10)
			jade.right(15)
	elif eachChar[i] == 's':
		jade.dot(11)
	elif eachChar[i] == 'r':
		jade.left(120)
		jade.forward(15)
	elif eachChar[i] == 'h':
		jade.right(120)
		jade.forward(15)
	elif eachChar[i] == 'l':
		jade.right(30)
		jade.forward(15)
	elif eachChar[i] == 'd':
		jade.left(30)
		jade.forward(15)
	elif eachChar[i] == 'c':
		jade.color('orange')
		jade.forward(7)
	elif eachChar[i] == 'u':
		jade.color('maroon')
		jade.forward(7)
	elif eachChar[i] == 'm':
		jade.color('gold')
		jade.forward(7)
	elif eachChar[i] == 'f':
		jade.color('turquoise')
		jade.forward(7)
	elif eachChar[i] == 'p':
		jade.color('lightgreen')
		jade.forward(7)
	elif eachChar[i] == 'g':
		jade.color('magenta')
	elif eachChar[i] == 'w':
		jade.color("violet")
		jade.forward(7)
	elif eachChar[i] == 'y':
		jade.color('red')
	elif eachChar[i] == 'b':
		jade.color('skyblue')
	elif eachChar[i] == 'v':
		jade.color('purple')
	elif eachChar[i] == 'k':
		jade.color('pink')
	elif eachChar[i] == 'x':
		jade.color('brown')
	elif eachChar[i] == 'j':
		jade.color('black')
	elif eachChar[i] == 'q':
		jade.left(90)
		jade.forward(10)
	elif eachChar[i] == 'z':
		jade.right(90)
		jade.forward(10)
	
turtle.done()