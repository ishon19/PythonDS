def checkDistinct(arr):
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            return False
        else:
            dict[arr[i]] = 1
    return True


arr = [1, 1, 3, 4]
print("All elements distict? ", checkDistinct(arr))
