import tweepy
import turtle

listOfNegatives = list()
with open ("negative.txt", "r") as myfile:
    for line in myfile:
        listOfNegatives.append(line.strip())


listOfPositives = list()
with open ("positive.txt", "r") as myfile1:
    for line in myfile1:
        listOfPositives.append(line.strip())

kevin = turtle.Turtle()
kevin.pensize(5)
turtle.title("Pos/Neg")
turtle.screensize(2000,1500)
kevin.color('white')
kevin.backward(300)



def comparePositive(word):
    for x in range(len(listOfPositives)):
        if word == listOfPositives[x]:
            return True

def compareNegative(word):
    for x in range(len(listOfNegatives)):
        if word == listOfNegatives[x]:
            return True

def compareToList(tweet):

    print("Selected: ", tweet)
    tweetList = list(tweet.split())
    for x in range(len(tweetList)):


        isPositive = comparePositive(tweetList[x])
        isNegative = compareNegative(tweetList[x])

        if isPositive == True:
            kevin.color('green')
            kevin.left(45)
            kevin.forward(30)
            kevin.dot(7)
            kevin.right(90)
            kevin.forward(30)
            kevin.left(45)


        elif isNegative == True:
            kevin.color('red')
            kevin.right(45)
            kevin.forward(30)
            kevin.dot(7)
            kevin.left(90)
            kevin.forward(30)
            kevin.right(45)


        else:
            kevin.color('grey')
            kevin.dot(7)
            kevin.forward(20)




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

    final = list()
    count = 0
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = name, tweet_mode="extended").items(50):
        if not (tweet.full_text[0] == '@') and not (tweet.full_text[0] == 'R' and tweet.full_text[1] == 'T'):
            #print(tweet.full_text)

            count = count + 1
            temp = str(tweet.full_text)

            final += [temp]
            if count == 10:
                break;

    for x in range(10):
        print(x + 1,':', final[x], '\n')

    index = input("Which tweet would you like to visualise? \n =>")
    index = int(index)
    compareToList(final[index - 1])




name = input("Whose tweet would you like to analyze: ")
getTweets(name)

turtle.done()

