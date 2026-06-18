# Polynomial vs. Exponential
#     Broadly speaking, algorithms can be classified into two categories:

#         "Polynomial time"
#         "Exponential time"


            # Poly_Expo_time/picNotes/poly&expoTime.png


                    # Technically O(n!) is "factorial" time, but let's lump them together for simplicity


# An algorithm runs in "Polynomial time" if its runtime does not grow faster than n^k, where k is 
#   any constant (e.g. n^2, n^3, etc) and n is the size of the input. Polynomial-time algorithms 
#   can be useful if they're not too slow.


# In comparison, exponential-time algorithms are almost always too slow to be practical. 
#   (However, sometimes you're trying to force someone to be slow, like in the case of cryptography and 
#   security). Even when n is as low as 20, 2^n is already over a million!
        # n 	n^2 	2^n
        # 2 	4 	    4
        # 3 	9 	    8
        # 4 	16 	    16
        # 5 	25 	    32
        # 6 	36 	    64
        # 7 	49 	    128
        # 8 	64 	    256
        # 9 	81 	    512
        # 10 	100 	1024
        # 11 	121 	2048
        # 12 	144 	4096
        # 13 	169 	8192
        # 14 	196 	16384
        # 15 	225 	32768
        # 16 	256 	65536
        # 17 	289 	131072
        # 18 	324 	262144
        # 19 	361 	524288
        # 20 	400 	1048576

# Polynomial algorithms are faster than exponential algorithms



# Polynomial Time = P 
#     Back in the 1970s, some computer scientists wanted to come up with a good, descriptive name for the 
#     set of polynomial time algorithms. After much deliberation, they settled on the letter P (naming things 
#     is hard).

# The hand-wavy takeaway is that:
#     Problems that fall into class P are practical to solve on computers.
#     Problems that don't fall into P are hard, slow, and impractical.

# Algorithms in P are More practical to solve with computers than algorithms not in P



# Reduction to P
#     Let's take an exponential time algorithm and fix it up so it can run in polynomial time!

# The Fibonacci sequence is a sequence of numbers where each number is the sum of the two numbers before it. Like this:
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# We want a function that, given an index in the sequence, returns the Fibonacci number at that index. 
# For example:
#     fib(0) -> 0
#     fib(1) -> 1
#     fib(2) -> 1
#     fib(3) -> 2
#     fib(4) -> 3
#     fib(5) -> 5
#     fib(6) -> 8
#     fib(7) -> 13


# Here are the implementation details to do it in polynomial time:
#     The input n represents the index of the desired Fibonacci number.
#     If n is less than or equal to 1, then return n.
#     Initialize three variables: grandparent = 0, parent = 1, and a placeholder current to store the new Fibonacci number at each step.
#     Write a loop that iterates n - 1 times. (For example, if n = 2, one iteration occurs.)
#     Inside the loop:
#         Set current = parent + grandparent
#         Adjust the ancestor values (parent and grandparent) to maintain the sequence.
#     Once the loop completes, return current.


def fib(n):
    if n <= 1:
        return n
    grandparent = 0
    parent = 1
    current = None
    for _ in range(n - 1):
        current = parent + grandparent
        grandparent, parent = parent, current
    return current


print(fib(6))



def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)




# Order K^N – Exponential
#     O(K^N) – where K represents a constant branching factor, e.g. 3^N – is the first Big O class that we've dealt with that falls into the scary exponential category of algorithms.

#     Algorithms that grow at an exponential rate become impossible to compute after so little scale-up that they're usually almost worthless in practicality.
#     Letter Combinations of a Phone Number

#     LockedIn's advertising team wants to help influencers launch paid campaigns using vanity phone numbers (think 1-800-FLOWERS).

#     In order for this to work, we need to be able to take a phone number and calculate all possible sequences of letters that it could represent. Then the ad team can give influencers numbers that make brand-friendly words.

            # Poly_Expo_time/picNotes/phoneKeyBoard.jpg

#     Each digit can represent three or four different letters. For this reason, the number of letter sequences associated with a string of digits grows very quickly as the number of digits increases. The possibilities either triple (3^N) or quadruple (4^N) with each additional digit.
#     Example number 	Possible letter sequences
#         "6" 	3 (m, n, o)
#         "67" 	12 (mp, mq, mr...)
#         "678" 	36 (mpt, mpu, mpv...)
#         "6789" 	144 (mptw, mptx...)
#         "345-6789" 	3,888

#     A 7-digit phone number will produce between 2,187 (3^7) and 16,384 (4^7) letter sequences – though usually closer to the low end of that range.

#     It's a good thing phone numbers are short! If you had a 32-digit phone number, it could form at least ~1.85 quadrillion letter sequences (assuming 3^N).

#     Unfortunately, if we want to check all the possible combinations from a given number, there's no real shortcut for us to take – we're stuck with an exponential-class algorithm.


def letter_combinations(digits: str) -> list[str]:
    def letter_combinations(digits: str) -> list[str]:
    # Mapping of digits to letters
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # If the input string is empty, return an empty list
    if not digits:
        return []
        
    # Define a result list to hold the output strings. 
    # Have it contain just an empty string to start.
    result = [""]
    
    # Iterate over the input digits
    for digit in digits:
        # If the digit is any invalid character, raise a ValueError
        if digit not in digit_to_letters:
            raise ValueError(f"invalid digit: {digit}")
            
        # Get the string of letters that can be represented by the current digit
        letters = digit_to_letters[digit]
        
        # Define a new_result list – empty to start with
        new_result = []
        
        # Enter two nested for loops
        for combo in result:
            for letter in letters:
                # Append combo + letter to new_result
                new_result.append(combo + letter)
                
        # Set result equal to new_result
        result = new_result
        
    # After the main loop, return the result
    return result
    



digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}



# Reality Check
    # Let's return to the hypothetical 32-digit phone number, which could form ~1.85 quadrillion letter sequences at minimum – assuming the four-letter digits (7 and 9) never appear.

# Even if we could process 1 million of those possible combinations per second, getting through all of them would take over 58 years. And if we wanted to store all those strings, it would be 60+ petabytes of data!

# Though maybe storage will be cheap in the next century...




# Big O Categories Review

#     Big-O 	     Name 	        Description

#     O(1) 	         constant 	    Best The algorithm always takes the same amount of time, regardless of how much data there is. Example: Looking up an item in a list by index
#     O(log(n)) 	 logarithmic 	Great Algorithms that remove a percentage of the total steps with each iteration. Very fast, even with large amounts of data. Example: Binary search
#     O(n) 	         linear 	    Good 100 items, 100 units of work. 200 items, 200 units of work. This is usually the case for a single, non-nested loop. Example: unsorted array search.
#     O(n*log(n))   "linearithmic" 	Okay This is slightly worse than linear, but not too bad. Example: mergesort and other "fast" sorting algorithms.
#     O(n^2) 	     quadratic 	    Slow The amount of work is the square of the input size. 10 inputs, 100 units of work. 100 Inputs, 10,000 units of work. Example: A nested for loop to find all the ordered pairs in a list.
#     O(n^3) 	     cubic 	S       lower If you have 100 items, this does 100^3 = 1,000,000 units of work. Example: A triple nested for loop to find all the ordered triples in a list.
#     O(2^n) 	     exponential 	Horrible We want to avoid this kind of algorithm at all costs. Adding one to the input doubles the amount of steps. Example: Brute-force guessing results of a sequence of n coin flips.
#     O(n!) 	     factorial 	    Even More Horrible The algorithm becomes so slow so fast, that it is practically unusable. Example: Generating all the permutations of a list

        # Poly_Expo_time/picNotes/BigO.png


# Which algorithm tends to be fastest? 
#   O(n^2) 
#   O(n*log(n)) 
#   O(n) 
#   O(2^n)
        # ANS: O(n)

# names is an array of strings 
# def get_name_at_index(names: list[str], i: int) -> str: 
#   return names[i] 
# 
# What is the Big O complexity of the function?
    # O(1)


# Consider the following code. It calculates the number of times a given number can be divided by 2 before becoming less than or equal to 1.

# def naive_log2(x: int) -> int:
# 	count = 0
# 	while x > 1:
# 		x /= 2
# 		count += 1
# 	return count

    # O(log x) linearithmic
        # why
            # The execution time grows logarithmically relative to the input value x. 
            # In Big O notation, we drop the constant base, resulting in O(log x)


            # {should understand it latter}


Complexity Quiz - Example 3

Consider the following function for two questions:

#  halvedSections returns a list of lists.
#  For example, n=12 results in:
#    [
#       [0 1 2 3 4 5 6 7 8 9 10 11 12]
#       [0 1 2 3 4 5 6]
#       [0 1 2 3]
#       [0 1]
#    ]
def halved_sections(n: int) -> int:
    rows = []
    i = n
    while i > 0:
        col = []
        for j in range(i+1):
            col.append(j)
        rows.append(col)
        i //= 2
    return rows

# It has a specific time complexity of:

# T(n) = O(n + n/2 + n/4 + ... 1)


# T(n)=O(n) (Linear Time)

# Why it isn't O(nlogn)
#     It's easy to look at a nested loop where the outer loop halves and think "O(nlogn)." However, because the inner loop's bound (i) drops by half every single time, the vast majority of the total work is done in the very first iteration. Every subsequent iteration combined does less work than that initial step!




# What is an equivalent (but not fully reduced) way to express the complexity?
#     An equivalent, unreduced way to express the complexity O(2n) is O(n + n).

# What is the most reduced form of the function's complexity?
    # O(n)  # we drop constt in big 0



# Exponential Growth Sequences
#     At LockedIn, we are interested in simulating the exponential growth of an influencer's followers over a 
#     certain period with an adjustable growth factor.



# Assignment
#     Complete the exponential_growth function. Given the initial followers count n, growth factor factor, and number of days days, return a list containing the exponential growth of followers for each day.

#     For example:

#     - Initial followers: 10
#     - Growth factor: 2
#     - Days: 4

#     Growth sequence: [10, 20, 40, 80, 160]

def exponential_growth(n: int, factor: int, days: int) -> list[int]:
    pass
