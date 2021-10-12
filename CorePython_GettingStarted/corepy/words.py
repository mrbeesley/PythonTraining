#!/usr/bin/env python3
""" Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
"""


import sys
from urllib.request import urlopen


def fetch_words(url):
    """ Fetch a list of words from a URL.

    Args: 
        url: The URL of a utf-8 text document.

    Returns:
        A list of strings containing the words 
        from the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """ Print Items one per line.

    Args:
        an iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """ Print each word from a text document at a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    #url = 'http://sixty-north.com/c/t.txt' Example URL
    words = fetch_words(url)
    print_items(words)


# using __name__ variable to determine if this is being imported or executed
# if its being executed then we need to run the function
if __name__ == '__main__':
    # sys.argv[0] is the module filename
    main(sys.argv[1])