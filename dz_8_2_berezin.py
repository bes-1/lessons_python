class MyClassExceptionDivZero(Exception):
    pass

while True:
    num = float(input('Enter a numerator: '))
    den = float(input('Enter a denominator: '))
    try:
        if den == 0:
            raise MyClassExceptionDivZero
        result = num / den
    except MyClassExceptionDivZero:
        print('Your denominator is null. Please repeat numerator and denominator again')
    if den != 0:
        print(f'Answer: {result}')
        break
