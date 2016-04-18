""" String assembler, taking a string and making it
into a list; delimited by space?"""
a = "Black blue red orange"
b = a.split(' ')
print(b)

c = ' '.join(b)
print(c)

# str.replace() could be used to eliminate a loop. Replace names?

# Finding player id, use c.find('x)