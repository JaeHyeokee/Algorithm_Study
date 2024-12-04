def isPalindrome(num):
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]: return False
    return True
while True:
    num = input()
    if num == '0': break
    if isPalindrome(num) == True: print('yes')
    else: print('no')