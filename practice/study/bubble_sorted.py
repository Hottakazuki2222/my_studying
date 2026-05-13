#バブルソート

def bubble_sort(arr):
    n = len(arr)
    
    #外側ループ(繰り返し回数)
    for i in range(n):
        print(f"\n---{i+1}回目の走査---")
        #内側ループ(隣同士を比較)
        for j in range(0, n-i-1):
            print("比較中:", arr)
            if arr[j] > arr[j+1]:
                #要素を交換
                arr[j],arr[j+1] = arr[j+1],arr[j]
                print(f"交換:{arr}")
    
    return arr

#入力
numbers = [5,2,8,1,3]

print("入力:",numbers)

#ソート
sorted_numbers = bubble_sort(numbers)

#出力
print("出力:",sorted_numbers)