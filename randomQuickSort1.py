from random import randint

def swap(a, b, arr): 
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot_index= start 
    pivot = elements[pivot_index]

    #start = pivot_index + 1
    #end = len(elements) -1 

    while start < end:
        while start < len(elements) and elements[start] <= pivot: 
            start += 1 
        while elements[end] > pivot: 
            end -= 1 

        if start < end: 
            swap(start, end, elements)
    
    swap(pivot_index, end, elements)

    return end

def randomized_quick_sort(elements, start, end):
    if start < end:
        partInd= partition(elements, start, end)
        randomized_quick_sort(elements, start, partInd-1)
        randomized_quick_sort(elements, partInd+1, end)

#elements = [2, 3, 9, 2, 2]

#print(randomized_quick_sort(elements, 0, len(elements)-1))


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
