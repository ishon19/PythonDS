def reverse(str):
    return str[::-1]


def reverseStrLoop(str):
    reverse = ''
    for i in range(len(str)-1, -1, -1):
        reverse += str[i]
    return reverse


print("Reverse of Shreyans is: ", reverse("Shreyans"))
print("Reverse of Shashwat is :", reverseStrLoop("Shashwat"))
