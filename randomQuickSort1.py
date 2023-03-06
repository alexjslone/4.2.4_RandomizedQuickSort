from random import randint

def swap(a, b, arr): 
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    #first you establish a pivot that will always be your first element in the list 
    pivot_index= start 
    pivot = elements[pivot_index]

    #start = pivot_index + 1
    #end = len(elements) -1 
    #if elements[start] == elements[end]: 
    #    return 
    
    firstElement= elements[start:end+1].count(elements[start])
    if firstElement == (end+1) - start: 
        return 

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
    #if elements[start] != elements[partInd-1]:
        if partInd != None:
            randomized_quick_sort(elements, start, partInd-1)
        #if elements[partInd+1] != elements[end]:
        if partInd != None:
            randomized_quick_sort(elements, partInd+1, end)
    return elements

elements = [2, 3, 9, 2, 9]

print(randomized_quick_sort(elements, 0, len(elements)-1))

"""
if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
"""