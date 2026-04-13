def reverse_word (s):

    words = s.split('.')

    reversed_word = words [::-1]
    return '.'.join(reversed_word)
s = "i.like.this.program.very.much"
print(reverse_word(s))


