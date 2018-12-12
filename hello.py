# ask user for their name
name = input("what is your name?: ")
# ask use for their age 
age = input("what is your age?: ")
# ask user what city they are in
city = input("what city are you in?: ")
#ask user what they enjoy doing
love = input("what do you love doing in your spare time?: ")
#Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age , city, love)
#Print output to screen

print(output)



word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
# and store it in the answer variable....

answer = word[word.index("esta"): word.index("aria")]
print(answer)