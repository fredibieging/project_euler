# https://projecteuler.net/problem=42

def word_to_number(word):
	return sum([ord(c) - 64 for c in word]) 

def generate_triangles(n):
	return [x * (x + 1) / 2 for x in xrange(1, n + 1)]

words = open('words.txt', 'r').read().replace("\"", "").split(",")
triangles = generate_triangles(30)
triangle_words = [word for word in words if word_to_number(word) in triangles]
print len(triangle_words)
