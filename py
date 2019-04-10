# Question 1 
# Simple Array Sum
#
def simpleArraySum(ar):
    count = 0 
    for i in range(len(ar)):
        count = count + ar[i]
    return count

# Question 2 
# Compare the Triplets
#
def compareTriplets(a, b):
    bobScore = 0
    elisScore = 0 
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] > b[i]:
                bobScore = bobScore + 1
            elif a[i] == b[i]:
                bobScore = bobScore
            else:
                elisScore = elisScore + 1
    else:
        return('Enter the valid data')
        
    return bobScore , elisScore
    
