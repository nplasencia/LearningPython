"""
Consider a list (list = []). You can perform the following commands:

    - insert i e: Insert integer e at position i.
    - print: Print the list.
    - remove e: Delete the first occurrence of integer e.
    - append e: Insert integer e at the end of the list.
    - sort: Sort the list.
    - pop: Pop the last element from the list.
    - reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the
7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

· Input Format

The first line contains an integer, n, denoting the number of commands.
Each line n of the i subsequent lines contains one of the commands described above.

· Constraints

The elements added to the list must be integers.

·Output Format

For each command of type print, print the list on a new line.
"""


if __name__ == '__main__':
    N = int(input())
    res = []

    # for _ in range(N):
    #     arr = input().split()
    #
    #     if arr[0] == "insert":
    #         res.insert(int(arr[1]), int(arr[2]))
    #     elif arr[0] == "print":
    #         print(res)
    #     elif arr[0] == "remove":
    #         res.remove(int(arr[1]))
    #     elif arr[0] == "append":
    #         res.append(int(arr[1]))
    #     elif arr[0] == "sort":
    #         res.sort()
    #     elif arr[0] == "reverse":
    #         res.reverse()
    #     elif arr[0] == "pop":
    #         res.pop()

    # Better way
    for _ in range(N):
        cmd, *args = input().split()

        if cmd != "print":
            eval("res.{0}({1})".format(cmd, ','.join(args)))
        else:
            print(res)

