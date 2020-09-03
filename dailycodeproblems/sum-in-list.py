#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

from timeit import default_timer as timer
from datetime import timedelta
from bisect import bisect_left

#Solution 1 ; Brute Force - O(N*2)
def sum_match_check(num_list, k):
    start = timer()
    for i in range(len(num_list)): 
        for j in range(len(num_list)): 
            if i != j and num_list[i] + num_list[j] == k:
                end = timer()
                print("Brute force match: " , timedelta(seconds=end-start))
                return True
    end  = timer()
    print("Brute force no-match: " , timedelta(seconds=end-start))
    return False

print(sum_match_check([10,4,3,9,2], 11));
print(sum_match_check([10,4,3,9,2], 50));


#Solution 1a : Do without For loops

#Solution 2 : add to a set
#O(N) since lookups of sets are O(1) each.

def sum_match_check2(num_list, k):
    start = timer()
    already_seen_set = set()
    for number in num_list:
        if k - number in already_seen_set:
            end = timer()
            print("Sets match : " , timedelta(seconds=end-start))
            return True
        already_seen_set.add(number)
    end = timer()
    print("With sets no-match: ", timedelta(seconds=end-start))
    return False

print(sum_match_check2([10,4,3,9,2], 11));
print(sum_match_check2([10,4,3,9,2], 50));

#Solution 3: sort & Binary search
#binary search algo - divide & conquer: log time
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php
# for N elements = O(N log N)
#sort the list. We can then iterate through the list and run a binary search on K - lst[i]. 
def two_sum(lst, K):
    lst.sort()

    for i in range(len(lst)):
        target = K - lst[i]
        j = binary_search(lst, target)

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
        #  if there's another number that's the same value as lst[i].
        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(lst) and lst[j + 1] == target:
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            return True
    return False

def binary_search(num_list, target):
    lo = 0
    hi = len(num_list)
    ind = bisect_left(num_list, target, lo, hi)

    if 0 <= ind < hi and num_list[ind] == target:
        return ind
    return -1

print(two_sum([10,4,3,9,2], 11))
print(two_sum([10,4,3,9,2], 50))

num_list = [10,30,50,60,60]
target = 42
index = bisect_left(num_list,target,0,len(num_list))
print("Index : Equals target and index <=0 or > len :", index, num_list[index]== target, index <=0, index > len(num_list))
