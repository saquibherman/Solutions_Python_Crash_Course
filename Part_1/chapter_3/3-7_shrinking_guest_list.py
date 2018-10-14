guest_names = ["joe", "alice", "bob"]
print("You are cordially invited " + guest_names[0].title())
print("You are cordially invited " + guest_names[1].title())
print("You are cordially invited " + guest_names[2].title())

print(guest_names[0].title() + " can't make it")
guest_names[0] = "eric"

print("You are cordially invited " + guest_names[0].title())
print("You are cordially invited " + guest_names[1].title())
print("You are cordially invited " + guest_names[2].title())

guest_names.insert(0, "peter")
guest_names.insert(2, "matthes")
guest_names.append("john")

print("\n")
print("You are cordially invited " + guest_names[0].title())
print("You are cordially invited " + guest_names[1].title())
print("You are cordially invited " + guest_names[2].title())
print("You are cordially invited " + guest_names[3].title())
print("You are cordially invited " + guest_names[4].title())
print("You are cordially invited " + guest_names[5].title())

print("\n")

print("I can invite two people for the dinner")

guest_names.pop()
guest_names.pop()
guest_names.pop()
guest_names.pop()

print("You are cordially invited " + guest_names[0].title())
print("You are cordially invited " + guest_names[1].title())

del guest_names[0]
del guest_names[0]

print("\n")
print(guest_names)

