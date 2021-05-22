import argparse
import sys

def calc(args):
    if args.o=='add':
        return args.x+args.y
    elif args.o=='null':
        return args.x*args.y
    elif args.o=='sub':
        return args.x-args.y
    elif args.o=='div':
        return args.x/args.y
    else:
        return "Something went wrong"



if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,
                        help="Enter first number.This is utility for calculation.please contact with Harry")
    parser.add_argument('--y',type=float,default=3.0,
                        help="Enter second number.This is utility calculator")
    parser.add_argument('--o', type=str, default="add",
                        help="This is utility calculator.For any help pls contact with harry")
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))