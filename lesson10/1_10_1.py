
def oops():
    raise IndexError


# oops()


def catch_oops():
    try:
        oops()
    except IndexError:
        print('we came here')


catch_oops()
