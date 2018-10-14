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
guest_names.insert(-1, "john")

print("You are cordially invited " + guest_names[0].title())
print("You are cordially invited " + guest_names[1].title())
print("You are cordially invited " + guest_names[2].title())
print("You are cordially invited " + guest_names[3].title())
print("You are cordially invited " + guest_names[4].title())

