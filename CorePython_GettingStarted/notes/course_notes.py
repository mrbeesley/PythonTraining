""" High level notes from the course

Usage:
    python3 course_notes.py
"""

def course_notes():
    """ Control method to compile all of the notes

    Args: 
        none

    Returns:
        none
    """

    print('\n\n')
    variable_management()
    print('\n\n')
    value_equality()
    print('\n\n')
    passing_arguments()
    print('\n\n')
    default_value_evaluation()
    print('\n\n')
    scopes_in_python
    print('\n\n')
    string_collections()
    print('\n\n')
    collection_protocols()
    print('\n\n')
    tuples_in_python()
    print('\n\n')
    ranges_in_python()
    print('\n\n')
    lists_in_python()
    print('\n\n')
    dictionaries_in_python()
    print('\n\n')
    sets_in_python()
    print('\n\n')


def variable_management():
    print('=================================Variables=================================')
    print('Integer Objects in python are immutable and cannot be changed')
    print('x = 1000')
    print('x = 500')
    print('When you do this a new variable is allocated and the int with value 1000 is orphaned and left for garbage collection')


def value_equality():
    print('=================================Value vs Identity Equality=================================')
    print(' 1. Value-Equality and identity equality are fundamentally different concepts')    
    print(' 2. comparison by value can be controlled programatically')
    print(' 3. identity comparison is unalterably defined by the language')


def passing_arguments():
    print('=================================Passing Arguments=================================')
    print(' 1. when you pass and argument it is passed by creating a new label against the underlying object')
    print(' 2. for example if you pass a list and then modify the list it is modified in both scopes')
    print(' 3. it is the responsibility of the function to copy the object if that is the desired result')
    print(' 4. function arguments are transferred using pass-by-object-reference')
    print(' 5. references to objects are copoied, not the objects themselves')
    print(' 6. Arguments with default values must come after those without default values')


def default_value_evaluation():
    print('=================================Default Value Evaluation=================================')
    print(' 1. remember that def is a statemnt executed at runtime')
    print(' 2. default arguments are evaluated when def is executed')
    print(' 3. immutable default values dont cause problems')
    print(' 4. mutable default values can cause confusing effects since they are only evaluted once')
    print(' 5. RULE: Always use immutable objects for default values')


def scopes_in_python():
    print('=================================Scopes in Python=================================')
    print(' LEGB')
    print('     LOCAL: inside the current function')
    print('     ENCLOSING: inside the enclosing functions')
    print('     GLOBAL: at the top level of the module')
    print('     BUILT-IN: in the special builtins module')
    print('*note - use the global keyword to explicitely reference a top level module variable')


def string_collections():
    print('=================================String Collections in Python=================================')
    print(' 1. Concatenation with + results in temporaries')
    print(' 2. Use str.join() to join strings, to prevent high memory usage')
    print(' 3. str.join() inserts a separator between a collection of strings')
    print(' 4. call join() on the separator string')
    print(' 5. use str.join() for efficient string concatenation')
    print(' 6. use str.partition() for certain simple string parsing operations')
    print(' 7. str.format() is a powerful string interpolation technique')
    print(' 8. f-strings are a kind of string literal for performing interpolation')
    print('* to concatenate invoke join on empty text, something from nothing')


def collection_protocols():
    print('=================================Protocols in Python=================================')
    print(' 1. A set of operations that a type must suppor to implement the protocol')
    print(' 2. do not need to be defined as interfaces or base classes')
    print(' 3. types only need to provide functioning implementations')


def tuples_in_python():
    print('=================================Tuples in Python=================================')
    print(' 1. tuples are immutable sequences')
    print(' 2. tuple literals are optional parentheses around comma seperated items')
    print(' 3. use a trailing comma for a single-element tuples')
    print(' 4. tuple unpacking is useful for multiple return values and swapping')


def ranges_in_python():
    print('=================================Ranges in Python=================================')
    print(' 1. range objects represetn arithmetic progressions of integers')
    print(' 2. range() can be called with one two or three arguments: start stop and step')
    print(' 3. enumerate is often better than range for making loop counters')


def lists_in_python():
    print('=================================Lists in Python=================================')
    print(' 1. list supports indexing from the end with negative indices')
    print(' 2. slicing copies all or part of a list')
    print(' 3. the full slice is a common idiom for copying lists')
    print(' 4. use list.index() and list.count() to look for elements in a list')
    print(' 5. use the del keyword to remove elements from a list')
    print(' 6. sort and reverse lists in-place with list.sort() and list.reverse()')
    print(' 7. sorted() and reversed() sort and reverse any iterable')
    print(' 8. list copies are shallow, only copying the references')


def dictionaries_in_python():
    print('=================================Dictionaries in Python=================================')
    print(' 1. dictionaries map from keys to values')
    print(' 2. iteration and membership in dictionaries are over keys')
    print(' 3. do not assume any order when iterating dictionary keys')
    print(' 4. dict.keys(), dict.values() and dict.items() are iterable views into dictionaries')
    print(' 5. copy dictionaries with dict.copy() or the dict constructor')
    print(' 6. use dict.update() to extend one dictionary with another')


def sets_in_python():
    print('=================================Sets in Python=================================')
    print(' 1. sets are unordered collections of unique elements')
    print(' 2. sets support powerful set-algebra operations and predicates')
    print(' 3. buile-in collections can be organized by protocols')
    print(' 4. underscore often represents unused values')
    print(' 5. the pprint module supports pretty printing of compound data structures')


def exceptions_in_python():
    print('=================================Exceptions in Python=================================')
    print(' 1. Exceptions enable EAFP (easier to ask forgiveness)')
    print(' 2. without exceptions error handling is interspersed in program flow')
    print(' 3. exceptions can be handled non-locally')
    print(' 4. Exxceptions are not easily ignored while error codes are silent by default')



if __name__ == '__main__':
    course_notes()