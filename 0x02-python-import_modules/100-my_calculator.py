#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = len(sys.argv) - 1
    operators = "+-*/"

    if args == 3:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
        else:
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = sub(a, b)
            elif op == '*':
                result = mul(a, b)
            else:
                result = div(a, b)

            print("{} {} {} = {}".format(a, op, b, result))

    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
