def recurrentSequence(fn, k, sequence):
    """ A generator for linear recurrence equations

    fn: a function to calculat a_n from sequence
    k: how many terms fn uses to calculate a_n
    sequence: The first k elements of the sequence
    """

    # n indexes the sequence
    n = k

    while True:
        try:
            Sn = fn(sequence, n)
        except IndexError:
            # if fn requires more terms than we have that's bad
            print('fn needs more terms than were provided')
            break

        sequence.append(Sn)
        sequence = sequence[-k:]

        yield Sn

        n += 1

