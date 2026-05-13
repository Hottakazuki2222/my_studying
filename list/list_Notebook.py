base_arr = [1,2,3,4,5,6,7,8,9,10]

#要素の追加
print("\n==========")
arr = base_arr.copy()
arr.append(100)
print("append:",arr)

#要素の削除(要素番号)
print("\n==========")
arr = base_arr.copy()
del arr[3]
print("delete:",arr)

#要素の削除(値で削除)
print("\n==========")
arr = base_arr.copy()
arr.remove(3)
print("remove:",arr)

#要素の削除+取り出し
print("\n==========")
arr = base_arr.copy()
arr.pop(3)
print("pop:",arr)

#要素を整列させる
print("\n==========")
arr_sort = [10,2,3,9,6,7,5,1,4,8]
print("before_sort",arr_sort)
arr_sort.sort()
print("after_sort:",arr_sort)

#元配列を守る
print("\n==========")
arr = base_arr.copy()
new_arr = sorted(arr,reverse=True)
print("original:",arr)
print("sorted:",new_arr)

#要素の反転
print("\n==========")
arr = base_arr.copy()
arr.reverse()
print("reverse:",arr)

#要素の検索
print("\n==========")
arr = base_arr.copy()
print("search_arr:",3 in arr)
print("search_arr2:",100 in arr)

#要素の位置取得
print("\n==========")
arr = base_arr.copy()
print("get_position:",arr.index(5))

#要素のステータス
print("\n==========")
arr = base_arr.copy()
print("max:",max(arr))
print("min:",min(arr))
print("length:",len(arr))
print("sum:",sum(arr))

#特定の要素の抜き出し
print("\n==========")
arr = base_arr.copy()
print("slice:",arr[2:5])

#ひとつづつ取り出す
print("\n==========")
arr = base_arr.copy()
for i in arr:
    print(i)

#配列の連結
print("\n==========")
arr = base_arr.copy()
arr2 = [11,12,13,14,15]
add_arr = arr+arr2
print("add_arr:",add_arr)

#特定要素の数を数える
print("\n==========")
count_arr = [1,1,4,5,1,4,1,9,1,9,8,1,0]
print("count:",count_arr.count(1))

#リストの初期化
print("\n==========")
arr = base_arr.copy()
arr.clear()
print("clear:",arr)

#要素の抜き出し
print("\n==========")
arr = base_arr.copy()
print(*arr)