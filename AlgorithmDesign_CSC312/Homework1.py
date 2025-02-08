#Problem 1:
# 1.1
# Read m and n, then read m lines into a set (this will eliminate all duplicates)
# Unpacks the set using the star expression, then group all of them into a list
# Use Tim Sort algorithm (which is the python sorted() function):
#     Uses Insertion Sort for small subarrays (typically < 64 elements)
#     Uses Merge Sort for larger sections
#     Takes advantage of pre-existing order in the data
# Then print out the nth first element in the list

# 1.2
# Reading m and n: O(1)
# Reading m lines (converting the input into interger is O(1)): O(m)
# Unpacking the set and group them into a list: O(m)
# Tim Sort: O(m log(m))
# Print out n numbers with map(),join(),and create a new list with n elements: O(n)
# ==> Final time complexity: O(m log(m))

# 1.3 must submit a .py file
m,n=map(int,input().split())
numbers=sorted([*{int(input())for _ in' '*m}])
print(f"{n} smallest numbers are: {' '.join(map(str,numbers[:n]))}")
