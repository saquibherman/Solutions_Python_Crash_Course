string1 = 'abcd'
string2 = 'plmn'
print("if string1 != string2? I predict True.")
print(string1 != string2)

string1 = 'abcd'
string2 = 'ABCD'
print("if string1 == string2? I predict True.")
print(string1 == string2.lower())

debt = 20000
deposit = 100000
print

value1 = 10
value2 = 10
print("if value1 <= value2 I predict True.")
print(value1 <= value2)

value1 = 10
value2 = 20
print("if value1 < value2 I predict True.")
print(value1 < value2)

value1 = 30
value2 = 20
print("if value1 > value2 I predict True.")
print(value1 > value2)

value1 = 30
value2 = 20
print("if value1 > 10 and value2 < 30 I predict True.")
print(value1 > 10 and value2 < 30)

countries = ['india', 'usa', 'japan', 'sweden', 'south korea']

if 'sweden' in countries:
	print("sweden is in the countries list")
	
if 'turkey' not in countries:
	print("turkey is not in the countries list")
