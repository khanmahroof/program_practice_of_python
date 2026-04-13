#repeating the string like shorter+longer+shorter
def it_short_long (a, b):

    if len(a) < len(b):
        short, long = a, b
    else:
        short, long = b, a
    return short + long + short
print(it_short_long('Hi','There'))
