#マージソート
def merge_sort(a,left,right):
    if left >= right: return
    m = int((left+right)/2)
    merge_sort(a,left,m)
    merge_sort(a,m+1,right)
    merge(a,left,m,right)

def merge(a,left,m,right):
    n1 = m - left + 1
    n2 = right - m
    L = [0]*n1;R = [0]*n2
    for i in range(0,n1):
        L[i] = a[left + i]
        i += 1
    for j in range(0,n2):
        R[j] = a[m+1+j]
        j += 1
    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]; i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def print_data(a):
    n = len(a)
    for i in range(0,n):
        print("{:2d}".format(a[i]),end="")
        print()

def print_data2(a,l,r):
    for i in range(l,r):
        print("{:2d}".format(a[i]),end="")

def main():
    a = [64,28,61,32,29,31,97,3,0]
    n = len(a)
    print("before:",end=""),print_data(a)
    merge_sort(a,0,n-1);
    print("After:",end=""),print_data(a);

if __name__ == "__main__":
    main()