if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = max(arr)
    
    # Remove all occurrences of the maximum score
    arr = [x for x in arr if x != max_score]
    
    # Find the new maximum, which will be the runner-up score
    runner_up = max(arr)
    print(runner_up)
