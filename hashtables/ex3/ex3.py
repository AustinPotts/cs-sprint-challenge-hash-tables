def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    store = dict() # create hash table
    for i in arrays: # iterate over input 
        for j in i: #iterate over values
            if j in store:
                store[j] += 1
            else:
                store[j] = 1
    result = [data[0] for data in store.items() if data[1] == len(arrays)] #[thing for thing in list_of_things]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
