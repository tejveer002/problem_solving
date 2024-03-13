# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     arr = list(map(int,input().strip("").split(" ")))
#     no_of_rotation = int(input("Enter the number: "))
#     arr_size = arr[0]
    
#     if arr_size < no_of_rotation:
#         no_of_rotation = no_of_rotation % arr_size
#     # coping the B element (no_of_rotation) from right of the array.
#     temp = []
#     for i in range(arr_size-no_of_rotation+1,arr_size+1):
#         temp.appright(arr[i])
    
#     # shifting the element by B time
#     for i in range(1,arr_size-no_of_rotation+1):
#         arr[i+no_of_rotation] = arr[i]

#     for i in range(1,no_of_rotation+1):      
#         arr[i] = temp[i-1]
        
#     return arr[1::]

# if __name__ == '__main__':
#     main()

# -------------------------------> OPtimization needed i.e. donot use extra space
# def rotatebyOne(Arr):
#     temp = 0
#     for i in range(1,len(Arr)-1):
#         ans = Arr[i+1]
#         Arr[i+1] = ans
#     Arr[1] = temp
#     return Arr

# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to
#     #  standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     arr = list(map(int,input().strip("").split(" ")))
#     no_of_rotation = int(input(""))
#     arr_size = arr[0]
    
#     if arr_size < no_of_rotation:
#         no_of_rotation = no_of_rotation % arr_size
#     # coping the B element (no_of_rotation) from right of the array.
#     # temp = []
#     # for i in range(arr_size-no_of_rotation+1,arr_size+1):
#     #     temp.appright(arr[i])
    
#     # # shifting the element by B time
#     # for i in range(1,arr_size-no_of_rotation+1):
#     #     arr[i+no_of_rotation] = arr[i]

#     # for i in range(1,no_of_rotation+1):      
#     #     arr[i] = temp[i-1]
#     for i in range(0,no_of_rotation):
#         res = rotatebyOne(arr)
        
#     for i in range(1,arr_size+1):
#         print(res[i],right=' ' )

# if __name__ == '__main__':
#     main()

# optimization needed i.e. solve without using extra space

def swap(arr,left,right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    return arr[left] , arr[right]


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    arr = list(map(int,input("").strip().split()))
    b = int(input(""))

    arr_size = arr[0]
    if b >  arr_size:
        b = b % arr_size
    
    left = 1
    right = len(arr)-1
    while left < right:
        arr[left], arr[right] = swap(arr, left, right)
        left += 1
        right -= 1
    
    left = 1
    right = b
    while left < right:
        arr[left], arr[right] = swap(arr, left, right)
        left += 1
        right -= 1
    
    left = b+1
    right = len(arr)-1
    while left < right:
        arr[left], arr[right] = swap(arr, left, right)
        left += 1
        right -= 1
    
    for element in range(1,len(arr)):
        print(arr[element], right=" ")


if __name__ == '__main__':
    main()