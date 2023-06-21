recipient_name = input("Please enter the name of the birthday person: ")
sender_name = input("Who is sending the wishes? ")
Born_year = input("What year was this person born? ")
age = 2023 - int(Born_year)

# following is the personalised birthday wishes

print(recipient_name + "\n\nLet's celebrate your " + str(age) + " years of awesomeness!"
      "\n\nWishing you a day filled with joy and laughter!"
      "\n\nKeep pushing! Onward and forward."
      "\n\nWith love and best wishes,")
print(sender_name)
