def balance(arr):                                                                  
    if not arr:                                                                    
        return                                                                     
                                                                                   
    N = len(arr)                                                                   
    i = 0                                                                          
    j = N-1                                                                        
                                                                                   
    while i<j:                                                                     
        if arr[i] == "R":                                                          
            i += 1                                                                 
                                                                                   
        if arr[j] == "B":                                                          
            j -= 1                                                                 
                                                                                   
        if arr[i] == "B" and arr[j] == "R":                                        
            arr[i], arr[j] = arr[j], arr[i]                                        
            i += 1                                                                 
            j -= 1                                                                 
                                                                                   
arr = ["R", "B", "B", "R", "R", "B", "R"]                                          
balance(arr)                                                                       
print(arr)
