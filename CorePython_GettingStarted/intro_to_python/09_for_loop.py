# for-loop

cities = ['london', 'new york', 'paris', 'oslo', 'helsinki']
for city in cities:
    print(city)

colors = {'crimson': 0xdc143c, 'coral': 0xff7f50, 'teal': 0x008080}
for color in colors:
    print(color, colors[color])

# putting this section together, string, bytes, dict and for loop
from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    #http by default returns bytes, have to decode to string
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()
print(story_words)