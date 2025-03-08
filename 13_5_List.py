# Find the union & intersection of two lists.

def find_union(list1, list2):
    return list(set(list1) | set(list2))

def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

def main():
    list1 = list(map(int, input("Enter elements of first list separated by space: ").split()))
    list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))
    
    union_result = find_union(list1, list2)
    intersection_result = find_intersection(list1, list2)
    
    print("\nUnion:", union_result)
    print("Intersection:", intersection_result)

if __name__ == "__main__":
    main()
