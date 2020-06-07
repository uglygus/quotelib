# quotelib

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
