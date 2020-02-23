import turtle
import random
import collections

stringIn = input("Enter your tweet:")
kim = turtle.Turtle()
kim.pensize(7)
turtle.title(stringIn)
stringIn = stringIn.lower()

def toss():
    a=['left','right']
    return(random.choice(a))

def randColor():
    b=['red','cyan','blue','green','orange','purple','pink','brown']
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