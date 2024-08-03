# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    user_input = input().strip()
    size, step = map(int, user_input.split())
    arr = list(range(1, size+1))
    #print(arr)

    pos = 0
    steps = []

    while True:
        #steps.append(arr[pos])
        print(arr[pos], end="")
        pos = (pos + step-1) % size
        if pos == 0:
            break

    #print(steps)

if __name__ == "__main__":
    main()