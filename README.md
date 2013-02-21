A generator for linear recurrence equations (homogenous and nonhomogenous).

Get the full scoop at [http://www.pmallory.com/linear-recurrence-generator.html](http://www.pmallory.com/linear-recurrence-generator.html)

Here's a Fibonacci example:

    :::python
    In [1]: def fib(s, n):
                return s[0]+s[1]

    In [2]: g = linearRecurance.recurrentSequence(fib, 2, [1,1])

    In [3]: g.next
    Out[3]: <method-wrapper 'next' of generator object at 0xe7b198>

    In [4]: g.next()
    Out[4]: 2

    In [5]: g.next()
    Out[5]: 3

    In [6]: g.next()
    Out[6]: 5

And an example of a nonhomogeneous equation:

    :::python
    In [7]: def lines(seq, n):
                 return seq[0]+n

    In [8]: g = linearRecurance.recurrentSequence(lines, 1, [1])

    In [9]: g.next()
    Out[9]: 2

    In [10]: g.next()
    Out[10]: 4

    In [11]: g.next()
    Out[11]: 7

    In [12]: g.next()
    Out[12]: 11

