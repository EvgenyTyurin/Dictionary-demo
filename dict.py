# Bill Lubanovich "Introducing Python"
# Chapter 3, Exercises 10-14: Dictionary demo

# English/French dictionary
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"}
print("English/French dictionary: " + str(e2f))    

# Walrus in french?
print("walrus in french = " + e2f["walrus"])

# Make French/English dictionary from English/French dictionary
f2e = {}
word_list = list(e2f.items())
pare_count = 0;
while pare_count < len(word_list):
    pare = word_list[pare_count]
    f2e[pare[1]] = pare[0];
    pare_count += 1    
print("French\English dictionary: " + str(f2e))

# Chien?
print("chien means = " + f2e["chien"])
