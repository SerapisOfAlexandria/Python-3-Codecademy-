name = "Stan"
question = "Will I be in a relationship with a girl?"
answer = ""

if random_number == 1:
  answer = "Yes - definetely"
elif random_number == 2 :
  answer = "It is decidedly so"
elif random_number == 3 :
  answer = "Without a doubt"
elif random_number == 4 :
  answer = "Reply hazy, try again"
elif random_number == 5 :
  answer = "Ask again later"
elif random_number == 6 :
  answer = "Better not tell you now"
elif random_number == 7 :
  answer = "My sources say no"
elif random_number == 8 :
  answer = "Outlook not so good"
else:
  answer = "Very doubtful"
if answer == "":
  question = "Question: "

print(name + " asks: " + question )
print("Magic 8-Ball's answer: " + answer)