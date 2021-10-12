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
    objects_and_types()
    string_collections()


def objects_and_types():
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


def variable_management():
    print('=================================Variables=================================')
    print('Integer Objects in python are immutable and cannot be changed')
    print('x = 1000')
    print('x = 500')
    print('When you do this a new variable is allocated and the int with value 1000 is orphaned and left for garbage collection')


def value_equality():
    print('=================================Value vs Identity Equality=================================')
    print('Value-Equality and identity equality are fundamentally different concepts')    
    print('comparison by value can be controlled programatically')
    print('identity comparison is unalterably defined by the language')


def passing_arguments():
    print('=================================Passing Arguments=================================')
    print('when you pass and argument it is passed by creating a new label against the underlying object')
    print('for example if you pass a list and then modify the list it is modified in both scopes')
    print('it is the responsibility of the function to copy the object if that is the desired result')
    print('function arguments are transferred using pass-by-object-reference')
    print('references to objects are copoied, not the objects themselves')
    print('Arguments with default values must come after those without default values')


def default_value_evaluation():
    print('=================================Default Value Evaluation=================================')
    print('remember that def is a statemnt executed at runtime')
    print('default arguments are evaluated when def is executed')
    print('immutable default values dont cause problems')
    print('mutable default values can cause confusing effects since they are only evaluted once')
    print('RULE: Always use immutable objects for default values')


def scopes_in_python():
    print('=================================Scopes in Python=================================')
    print('LEGB')
    print('LOCAL: inside the current function')
    print('ENCLOSING: inside the enclosing functions')
    print('GLOBAL: at the top level of the module')
    print('BUILT-IN: in the special builtins module')
    print('*note - use the global keyword to explicitely reference a top level module variable')


def string_collections():
    print('=================================String Collections in Python=================================')
    print('1. Concatenation with + results in temporaries')
    print('2. Use str.join() to join strings, to prevent high memory usage')
    print('3. str.join() inserts a separator between a collection of strings')
    print('4. call join() on the separator string')
    print('* to concatenate invoke join on empty text, something from nothing')



if __name__ == '__main__':
    course_notes()