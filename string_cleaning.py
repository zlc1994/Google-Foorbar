"""
String cleaning
===============
Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists who
are
turning rabbits into zombies. He sends a text transmission to you, but it is
intercepted by a pirate, who jumbles the message by repeatedly inserting the
same word into the text some number of times.
At each step, he might have inserted the word anywhere, including at the start
or end, or even into a copy of the word he inserted in a previous step.
By offering the pirate a dubloon, you get him to tell you what that word was.
A few bottles of rum later, he also tells you that the original text was the
shortest possible string formed by repeated removals of that word,
and that the text was actually the lexicographically earliest string from all
the possible shortest candidates.
Using this information, can you work out what message your spy originally sent?
For example, if the final chunk of text was "lolol," and the inserted word was
"lol," the shortest possible strings are "ol" (remove "lol" from the beginning)
and "lo" (remove "lol" from the end). The original text therefore must have
been
"lo," the lexicographically earliest string.
Write a function called answer(chunk, word) that returns the shortest,
lexicographically earliest string that can be formed by removing occurrences of
word from chunk.
Keep in mind that the occurrences may be nested, and that removing one
occurrence might result in another. For example, removing "ab" from "aabb"
results in another "ab" that was not originally present. Also keep in mind that
your spy's original message might have been an empty string.
chunk and word will only consist of lowercase letters [a-z].
chunk will have no more than 20 characters.
word will have at least one character, and no more than the number of
characters
in chunk.
"""

def cut(string, start, length):
    """remove a substring with a certain start index and length"""
   
    return string[:start]+string[start+length:]


def clean(chunk, word, start):
    """remove all occurrence word in chunk at the start index"""
     
    index = chunk.find(word, start)

    while index != -1 and start < len(word):
        chunk = cut(chunk, index, len(word))
        index = chunk.find(word)

    return chunk


def answer(chunk, word):
    """do clean method with all the subsequences, and return the 
    lexicographically earliest string  """
    

    result = []

    for start in range(len(chunk)-len(word)):
        string = clean(chunk, word, start)
        
        if string != chunk:
            result.append(string)

    return sorted(result)[0]
