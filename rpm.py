# rpm.py
#   This program uses the "Russian Peasant Multiplication" algorthm
#   to solve for muliplication through binary expansion.
#   (See rpm.md for a full explaination)
# by: Scott Gordon

import math
import pandas as pd

def main():
    print('***** Russian Peasant Multiplication *****')
    def rpm():
        print('Input two comma separated numbers (x, y): ')
        input_str = input('> ')
        inputs = input_str.split(',')
        n1, n2 = int(inputs[0]), int(inputs[1])

        halving = [n1]
        while(min(halving) > 1):
            halving.append(math.floor(min(halving)/2))

        doubling = [n2]
        while(len(doubling) < len(halving)):
            doubling.append(max(doubling) * 2)

        half_double = pd.DataFrame(zip(halving,doubling))
        rpm_out = half_double.to_markdown()
        print('\n*** RPM Table ***')
        print(f'{rpm_out}\n') # requires tabulate to display output as md
        half_double = half_double.loc[half_double[0]%2 == 1,:]

        answer = sum(half_double.loc[:,1])
        print(f'The solution to your problem is {answer}\n')

    rpm()

if __name__=='__main__':
    main()
