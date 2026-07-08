#Using a List and a Loop
# Define phrases in a list
spam_phrases = ["Make a lot of money", "buy now", "subscribe this", "click this"]

message = input("Enter your comment: ")
is_spam = False

# Check each phrase using a loop
for phrase in spam_phrases:
    if phrase in message:
        is_spam = True
        break  # Stop checking once a match is found

if is_spam:
    print("This comment is a spam")
else:
    print("This comment is not a spam")

