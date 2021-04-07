# Mad Libs is a phrasal template word game which consists of one
# player prompting others for a list of words to substitute for blanks in a story.
# #string concatenation(aka joining two or more strings together)
# #suppose we want to create a string that says "Connect with ______"
# linkedin = "Ruchita Potamsetti" #some string variable

# #there a few ways to do that
# print("Connect with " + linkedin)
# print("Connect with {}".format(linkedin))
# print(f"Connect with {linkedin}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")


madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)