guest_names = ["joe", "alice", "bob"]
print("You are cordially invited " + guest_names[0].title())
print("You are cordially invited " + guest_names[1].title())
print("You are cordially invited " + guest_names[2].title())

print(guest_names[0].title() + " can't make it")
guest_names[0] = "eric"

print("You are cordially invited " + guest_names[0].title())
print("You are cordially invited " + guest_names[1].title())
print("You are cordially invited " + guest_names[2].title())
