import textblob

test=1
while test:
    text = input("enter your words: ~")
    print("orginal sentence:"+text)

    blob = textblob.TextBlob(text)
    print("correct text:"+str(blob.correct()))
    while True:
        try:
            test = int(input("try again? 1:0 "))
            break 
        except ValueError:
            print("Enter a number please!")

