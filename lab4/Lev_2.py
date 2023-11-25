def m(a, b):
    return int(a!=b)

def lev(str1, str2):
    #str1 = input().strip()
    #str2 = input().strip()
    L = len(str1) + 1
    L2 = len(str2) + 1
    mass = [0]*L2
    mass[0] = range(L)
    for i in range(1, L2):
        mass[i] = [0]*L
        mass[i][0] = i
    for i in range(1, L2):
        for j in range(1, L):
            mass[i][j] = min(mass[i][j-1] + 1,
                             mass[i-1][j] + 1,
                             mass[i-1][j-1] + (str1[j-1] != str2[i-1]))
    return mass[L2-1][L-1]
