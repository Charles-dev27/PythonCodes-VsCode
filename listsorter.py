def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j][0].lower() < arr[min_index].lower():
                min_index = j
            arr[i],  arr[min_index] = arr[min_index], arr[i]
    return arr

texts = input('> ').split(',')
text = [text.strip() for text in texts]
select = selection(text.copy())
print(select)