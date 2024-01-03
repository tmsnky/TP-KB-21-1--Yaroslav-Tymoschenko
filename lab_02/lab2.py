def findExtremumWithIndex(listForSearch: list, find_max: bool):
    extremum = None
    index = None

    for idx, val in enumerate(listForSearch):
        if extremum is None or (find_max and val > extremum) or (not find_max and val < extremum):
            extremum = val
            index = idx

    return index, extremum

def main():
    listOfData = [5, 11, 14, 22, 33, 7, 88, 999, 123, -4, 64, 10, 55, 66, 44, 20, 345]
    
    result = findExtremumWithIndex(listOfData, False)  # Finding Minimum
    print(f"Min id: {result[0]}, Min value: {result[1]}")  # Output: Min id: 9, Min value: -4

    result = findExtremumWithIndex(listOfData, True)  # Finding Maximum
    print(f"Max id: {result[0]}, Max value: {result[1]}")  # Output: Max id: 16, Max value: 345

if __name__ == "__main__":
    main()
