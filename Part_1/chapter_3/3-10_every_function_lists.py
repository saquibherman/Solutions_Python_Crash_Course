# methods
# title(), append(), insert(), pop(), del, remove(), sort(), reverse()

#functions
# sorted(), len()

languages = ["swedish", "english", "arabic", "fench"]
print("The languages I wanna learn " + languages[3].title())
languages.append("hindustani")
print(languages)
languages.insert(2, "urdu")
print(languages)
mother_tounge = languages.pop()
print("I already know " + mother_tounge)
del languages[2]
print(languages)
languages.remove("english")
print(languages)
print(sorted(languages))
print(languages)
print("total languages in my list are " + str(len(languages)))
languages.sort()
print(languages)
languages.reverse()
print(languages)
