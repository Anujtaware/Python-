"""16) print the following pattern

*   *   *   *   *

  *   *   *   *

    *   *   *

      *   *

        *
"""
for i in range(1,6):

    for k in range(6 - i):
        print('*', end='   ')
    print()
    print()
    for j in range(0,i):
        print(' ', end=' ')