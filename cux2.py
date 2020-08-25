"""
Command Line Utility Practice 2 
Multiplication Table 
"""

import argparse 
import sys


def mul(args):
    
    for i in range (args.x, args.x + 1):
        print(f"-------{args.x} Table is -------")
        for j in range(args.y):
            print(f"{args.x} X {args.y} = {args.x * args.y}")
            
        
if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--x",
                        type = int,
                        default = 2,
                        help = "This is a Multiplication Table Printer")
    
    parser.add_argument("--y",
                        type = int,
                        default = 12,
                        help = "This is a Multiplication Table Printer")
    
    args = parser.parse_args()
    sys.stdout.write(str(mul(args)))
    
    