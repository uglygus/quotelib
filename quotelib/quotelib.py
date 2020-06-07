
'''
    quotelib.py

    quote(item, use_shlex=True, always=False)
    
        Quotes item using single quotes.
        If item contains a single uses double quotes.
        If item contains both single and double quotes returns None and prints a warning to stdout.

        If item is a list returns a new list with each element quoted

        By default uses shlex.quote() to do the actual quoting.

        This means that items containing both single and double quotes
        will be escaped as if they are being used in the shell which may not be ideal.

        item :  can be a list,string, int, float probably more.
        use_shlex (bool) : use shlex to do the quoting or our custom function?
                           implies always=False
        always (bool) :  only matters if use_shlex=False.
                         wether to quote all strings or just ones that
                         contain certain characters. (quotes and whitespace)
        returns : a quoted version of the thing to quote
'''

import shlex


# characters that will force a quote when always=False
quotable_chars = '\t\n "\''


def _contains_any(str, set):
    ''' Check whether sequence str contains ANY of the items in set. '''
    return True in [c in str for c in set]

def _already_quoted(astring):
    ''' Check whether string begins and ends with a quote (single or double) and 
        does not contain the same kind of quote inside it.
    '''
    
    if len(astring) < 2:
        return False  
    
    if astring[0] != astring[-1]:
        return False


    if astring[0] != '"' and astring[0] != "'":
        return False

    quotechar=astring[0]
    
    stripped_string = astring[1:]   #trim first char
    stripped_string = astring[0:-1] #trim last char
    
    if quotechar in stripped_string:
        return False

    
    return True
    

    
def _dumbquote(input):
    '''
        returns a quoted string regardless of what it contains.
    '''

    if '"' in input and "'" in input:
        print('WARNING: input contains both single and double quotes. Returning None.')
        result = None
    elif "'" in input:
        #print('has single quote')
        result = '"' + input + '"'
    else:
        result = "'" + input + "'"

    return result


def _quoteitem(input, use_shlex=True, always=False):
    '''
        Quotes input in single quotes.
        If input contains  a single uses double quotes.

        input (string, int, float, maybe more?) : the thing to quote

        use_shlex : quoting is done by shlex.quote() which is
                    designed for shell arguments.

        always : Only considered if use_shlex = False
                 if true always return a quoted string or None on failure
                 if false don't bother quoting strings that don't
                 contain any whitespace or quote characters.

                 If it contains both single and double quotes returns None.
    '''

    if not isinstance(input, str):
        input = str(input)

    if use_shlex:
        return shlex.quote(input)

    #print('not using shlex')

    if always:
       # print('always is true calling dumbquote')
        result = _dumbquote(input)
    else:
        if _contains_any(input, quotable_chars):
            result = _dumbquote(input)
        else:
          # print('returning orginal input untouched.')
            result = input

    return result


def _quotelist(input, use_shlex=True, always=False):
    '''
        quotes individual items in list
        items (list) : a list of strings
        returns (list) : a list of strings
    '''

    new_items = []
    for item in input:
        new_items.append(_quoteitem(item, use_shlex, always))

    return(new_items)



def quote(input, use_shlex=True, always=False):

#    print('quote input=', input)

    if isinstance(input, list):
        return _quotelist(input, use_shlex, always)
    else:
        return _quoteitem(input, use_shlex, always)


def test():


    res = _already_quoted('')
    print('_already_quoted(\'\') res= ', res)

    res = _already_quoted('"')
    print('_already_quoted(\'"\') res= ', res)

    res = _already_quoted('""')
    print('_already_quoted(\'""\') res= ', res)

    res = _already_quoted('"abc"')
    print('_already_quoted(\'"abc"\') res= ', res)


#     item = 'whithout_white_spacespace'
#     print('quote(', item, ')=', quote(item), '\n')
# 
#     item = 'Has white space'
#     print('quote(', item, ')=', quote(item), '\n')
# 
#     item = 'jim"s'
#     print('quote(', item, ')=', quote(item), '\n')
# 
#     item = "Cooper's"
#     print('quote(', item, ')=', quote(item), '\n')
# 
#     item = "contains single \' and double \"."
#     print('quote(', item, ')=', quote(item), '\n')
# 
#     item = "use_shlex=False:  contains single \' and double \"."
#     print('quote(', item, ')=', quote(item, use_shlex=False), '\n')
# 
#     item = 333
#     print('quote(', item, ')=', quote(item), '\n')
# 
#     item = 6.67
#     print('quote(', item, ')=', quote(item), '\n')
# 
#     alist = [5, 5.1, 'a string', 'oneword', 'use_shlex=True', 'always=False']
#     alist = quote(alist)
#     print('quote(', alist, ')=', alist)
# 
#     for item in alist:
#         print('\ta list item = ', item)
# 
#     alist = [5, 5.1, 'a string', 'oneword', 'use_shlex=False', 'always=True']
#     alist = quote(alist, use_shlex=False, always=True)
#     print('quote(', alist, ')=', alist)
# 
#     for item in alist:
#         print('\ta list item = ', item)
# 
#     alist = [5, 5.1, 'a string', 'oneword', 'use_shlex=False', 'always=False']
#     alist = quote(alist, use_shlex=False, always=False)
#     print('quote(', alist, ')=', alist)
# 
#     for item in alist:
#         print('\ta list item = ', item)


if __name__ == '__main__':
    test()
