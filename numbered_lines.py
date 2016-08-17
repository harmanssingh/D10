#!/usr/bin/env python3
def numbered_lines():
    with open('small.txt', 'r') as f:
        txt=f.readlines()
    for lines in txt:
        lines.strip()
    with open('smallnew.txt', 'w') as f1:
        line=1
        for lines in txt:
            f1.write(str(line)+' '+lines)
            line+=1

def main():
    numbered_lines()

if __name__ == "__main__":
    main()
