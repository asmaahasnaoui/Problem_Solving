#can sum function it has two arguments it return true if we can sum combination of numbers to get arguments
def canSum(sum, element):
    if sum == 0:   
        return True
    
    if sum < 0:
        return False
    
    for i in element:
        remainder = sum - i
        if canSum(remainder, element)==True:
            return True
    return False

# can sum function using memoisation
def canSumMemo(sum, element,memo={}):
    
    if sum in memo:
        return memo[sum]
    
    if (sum == 0):  
        return True
    if (sum < 0):
        return False
    for i in element:
        remainder = sum - i
        if (canSumMemo(remainder, element)):
            memo[sum] = True
            return True
    memo[sum] = False
    return False

# Function to find a combination of numbers that add up to the targetSum
# Returns a pointer to an array of integers representing the combination,
# or NULL if no combination is found.
#without memoisation
def find_combination(target_sum, numbers):
    if target_sum == 0:
        # Return an empty list as the combination
        return []

    if target_sum < 0:
        # Return None to indicate no combination is found
        return None
    for num in numbers:
        remainder = target_sum - num
        result = find_combination(remainder, numbers)
        if result is not None:
            # Append the current number to the result list
                     
            return result+[num]  
    return None
#with memoisation
def find_combinationMemo(target_sum, numbers, memo={}):
    if target_sum == 0:
        # Return an empty list as the combination
        return []

    if target_sum < 0:
        # Return None to indicate no combination is found
        return None

    if target_sum in memo:
        return memo[target_sum]

    for num in numbers:
        remainder = target_sum - num
        result = find_combinationMemo(remainder, numbers, memo)
        if result is not None:
            # Append the current number to the result list
            combination = result + [num]
            memo[target_sum] = combination
            return combination

    # Return None if no combination is found
    memo[target_sum] = None
    return None
#function return the shortest combination of numbers
def bestSum(targetSum,numbers):
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    shortestCombination=None
    for num in numbers:
        remainder=targetSum-num 
        result=bestSum(remainder,numbers)
        if  result is not None:
            combination=result+[num]
            if shortestCombination is None or len(shortestCombination) > len(combination):
                shortestCombination=combination
    return shortestCombination
#function return the shortest combination of numbers using memoisation
def bestSumMemo(targetSum,numbers,memo={}):
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    if targetSum in memo:
        return memo[targetSum]
    shortestCombination=None
    for num in numbers:
        remainder=targetSum-num 
        result=bestSumMemo(remainder,numbers,memo)
        if  result is not None:
            combination=result+[num]
            if shortestCombination is None or len(shortestCombination) > len(combination):
                shortestCombination=combination
    memo[targetSum]=shortestCombination            
    return memo[targetSum]  
        
#can construct functionn is a function that have 2 arguments target and word bank it return true if we can construct the target from the word bank 
#else it return false
def canConstruct(target,wordBank):

    if target=='':
        return True
    for word in wordBank:
        #index of means the first character from wrd and target are the same
        if target.startswith(word):
            #suffixe return the rest of target after deleting prefix(word)
            suffix=target[len(word):]
            if canConstruct(suffix,wordBank)==True:
                return True

    return False
#canConstruct using memoisation
def canConstructMemo(target,wordBank,memo={}):
    
    if target=='':
        return True
    if target in memo:
        return memo[target]
    for word in wordBank:
        #index of means the first character from wrd and target are the same
        if target.startswith(word):
            #suffixe return the rest of target after deleting prefix(word)
            suffix=target[len(word):]
            if canConstructMemo(suffix,wordBank,memo)==True:
                memo[target]=True
                return memo[target]
    
    memo[target]=False
    return memo[target]
#Count construct is a function that return how many way we can construct the target from word bank
def CounConstruct(target,wordBank):
    if target=='':
        return 1
    count=0
    for word in wordBank:
        if target.startswith(word):
            suffix=target[len(word):]
            if CounConstruct(suffix,wordBank)==1:
                count=count+1
    return count 
#count construct using memoisation
def CountConstructMemo(target,wordBank,memo={}):
    if target=='':
        return 1
    if target in memo:
        return memo[target]
    count=0
    for word in wordBank:
        if target.startswith(word):
            suffix=target[len(word):]
            if CountConstructMemo(suffix,wordBank,memo)==1:
                count=count+1
    memo[target]=count
                
                
    return count   
#how construct is a function that return all combinition from wordBank that can construct target
def howConstruct(target,wordBank):
    if target=="":
        return [[]]
    allCombination=[]
    for word in wordBank:
        if target.startswith(word):
            suffix=target[len(word):]
            result= howConstruct(suffix,wordBank) 
            for combination in result:           
                allCombination.append([word] + combination)
    
    return allCombination
#howConstruct using Memoisation
def howConstructMemo(target,wordBank,memo={}):
    if target=="":
        return[[]]
    if target in memo:
        return memo[target]
    allCombination=[]
    for word in wordBank:
        if target.startswith(word):
            suffix=target[len(word):]
            result= howConstructMemo(suffix,wordBank,memo) 
            for combination in result:
                allCombination.append([word] + combination)
                memo[target]=allCombination
    return allCombination 
#Fibonacci using memoisation
def fibo(n,memo={}):
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibo(n - 1) + fibo(n - 2)

    return memo[n]
# Grid traveler return how many way we can move in matrix of m*n from starting point to end point
def gridTraveller( m, n):
    if m == 0 or n == 0:
        return 0
    
    else:
    
        if m == 1 and n == 1:  
            return 1
        
        else:
            return gridTraveller(m - 1, n) + gridTraveller(m, n - 1)
# Grid traveller using memo
def gridTravellerMemo(m, n,memo={}):

    if m == 0 or n == 0:   
        return 0    
    else:  
        if m == 1 and n == 1:     
            return 1 
    if (m,n) in memo:   
        return  memo[(m, n)] 
    memo[(m, n)] = gridTravellerMemo(m - 1, n,memo) + gridTravellerMemo(m, n - 1,memo)

    return  memo[(m, n)]
######################################################################################################
######################################################################################################
######################################################################################################
# fibbo using tabulation
def fibTab(n):
    tab={}
    if (n <= 1):
        return n
    tab[0] = 0
    tab[1] = 1
    for i in range(2,n+1):
        tab[i] = tab[i - 1] + tab[i - 2]

    return tab[n]

# Grid traveller using tabulation
def gridTavellerTab(m, n):
    tab2 = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base case: there is one way to reach (1, 1)
    tab2[1][1] = 1

    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if i + 1 <= m:
                tab2[i + 1][j] += tab2[i][j]
            if j + 1 <= n:
                tab2[i][j + 1] += tab2[i][j]
    return tab2[m][n]
#CanSum using tabulation
def canSumTab(target,number):
    tab=[False] * (target + 1)
    tab[0]=True
    for i in range(0,len(tab)):
        if tab[i]==True:
            for num in number:
                if i + num <= target:
                    tab[i+num]=True

    return tab[target]  
#howSum using tabulation
def howSumTab(target,number):
    tab =[None] * (target + 1)  
    tab[0]=[]
    for i in range(0,len(tab)):
        if tab[i]is not None:
            for num in number:
                if i + num <= target:
                    tab[i+num]=tab[i]+[num]
    return tab[target]                      
#bestSum using tabulation
# def bestSumTab(target,number):
#     tab =[None] * (target + 1)  
#     tab[0]=[]
#     for i in range(0,len(tab)):
#         if tab[i]is not None:
#             for num in number:
#                 if i + num <= target:
#                     combination=tab[i]+[num]
#                     if (not tab[i+num] or len(tab[i]+num)>len(combination)):
#                         tab[i+num]=combination
#     return tab[target]       

      
    
        


# Example usage:
# target_sum = 8
# numbers = [3,5,2]
# result = canSumMemo(target_sum, numbers)
# if result==True:
#     print("true")
# else:
#     print("false")    


# if result is not None:
#     print("Combination:", result)
# else:
#     print("No combination found.")
# target_sum = 8
# numbers = [3, 5, 2]
# result = bestSumMemo(target_sum, numbers)

# if result is not None:
#     print("Combination:", result)
# else:
#     print("No combination found.")
# target = "abcdef"
# wordBank = ["ab", "abc", "cd","ef"]
# result = howConstructMemo(target, wordBank)

# if result is not None:
#     print("we can:",result)
# else:
#     print("No we cant.")
#print(fibo(7))
#print(gridTraveller(2,3))
#print(gridTravellerMemo(2,3))
#print(fibTab(7))
#print(gridTavellerTab(2,3))
target_sum = 8
numbers = [3,5,2]
result = howSumTab(target_sum, numbers)
if result is not None:
    print(result)
else:
    print("false") 




