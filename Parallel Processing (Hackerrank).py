def minTime(files, numCores, limit):
    time = 0
    files.sort(reverse=True)
    for file in files:
        if file % numCores == 0 and limit != 0:
            time += file//numCores
            limit -= 1
        else:
            time += file
    return time


if __name__ == '__main__':
    files_count = int(input().strip())
    files = []
    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)
    numCores = int(input().strip())
    limit = int(input().strip())
    result = minTime(files, numCores, limit)
    print(result)
