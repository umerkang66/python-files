def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please return a number'
    except ValueError as err:
        # we don't have to raise the error, but return it, because we want to catch this in our testing environment
        return err
