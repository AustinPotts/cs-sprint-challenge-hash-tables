# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
 
    #return a valid list of attributes
    dir = dict()
    #iterate over files 
    for file in files:
        split_file = file.split("/") #split the file with /
        filename = split_file[-1] #file name = i.e split/file
        if filename not in dir: #check if file is in dict, if not add
            dir[filename] = []
        dir[filename].append(file)
    #iterate over queries
    for q in queries:
        if q in dir: 
            result.extend(dir[q]) # Iterate over arguments + adding each element to the list and extending the list

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
