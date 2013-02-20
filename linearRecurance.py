def recurrentSequence(k, sequence, fn):
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

