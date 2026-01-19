arr = [1, 45, 3, 65, 23, 33, 32, 2];


i = 0;

for i in range(len(arr) - 1):
    for j in range(len(arr) - 1):
        if(arr[j + 1] < arr[j]):
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp
print(arr)