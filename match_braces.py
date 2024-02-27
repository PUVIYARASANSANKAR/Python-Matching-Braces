# Write a Program to Match the braces in the given string.
# An input string would be taken from the user which can contain any of the 6 characters (,),[,],{,} in any order.
# If there is any other character in the string Print "INVALID INPUTS".
# The number of ( and ), [ and ], { and } should be made equal in the string by appending the missing characters.
# Identify the missing braces and append them to end of the input string to make the opening and closing braces equal.
# Sample Input 1: {[][]() []

# Sample Output : INVALID INPUTS (The input contains a Space)

 

# Sample Input 2 :  }[()[]

# Sample Output: }[()[]{] (The last 2 characters { and ] are appended to match the unmatched } and [

 

# Sample Input 3 : }}}[[[(((

# Sample Output : }}}[[[(((}}}[[[))) (The Last 9 characters are appended to match the unmatched 9 characters.
#output:  }}}[[[((()))]]]{{{ 



##OUTPUT:


def matching_braces(input_string):
    brace_counts = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}  

    valid_chars = set(['(', ')', '[', ']', '{', '}'])           # check only valid inputs
    for char in input_string:
        if char not in valid_chars:
            return f"INVALID INPUTS.\n The input contains {char}"

    for char in input_string:
        if char in brace_counts:
            brace_counts[char] += 1

    # check the balancing of braces
    if brace_counts['('] != brace_counts[')'] or brace_counts['['] != brace_counts[']'] or brace_counts['{'] != brace_counts['}']:
        output = input_string
        explanation = "Explanation: The following characters were appended to balance the braces:\n"
        for brace, count in brace_counts.items():
            if count < brace_counts[get_matching_brace(brace)]:
                num_missing = brace_counts[get_matching_brace(brace)] - count
                output += brace * num_missing
                explanation += f"The Last {len(brace * num_missing)} characters such as  {brace * num_missing} to match the unmatched {get_matching_brace(brace)} braces.\n"
        return output +"\n"+ explanation
    else:
        explanation= "Braces are Perfectly Balanced.\n"
        return input_string+"\n"+ explanation

def get_matching_brace(brace):
    if brace == '(':
        return ')'
    elif brace == ')':
        return '('
    elif brace == '[':
        return ']'
    elif brace == ']':
        return '['
    elif brace == '{':
        return '}'
    elif brace == '}':
        return '{'


input_string = input("Enter a braces: ")
output = matching_braces(input_string)
print("Output:", output)
