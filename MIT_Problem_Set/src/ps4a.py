# Problem Set 4A -------------> Permutations of a String
# Name: <Rituram Ojha>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]

    first_char = sequence[0]
    remaining_permutations = get_permutations(sequence[1:])

    # This will store all the permutations including the first character
    permutations = []

    # For each permutation of the remaining characters,
    # insert the first character into every possible position
    for perm in remaining_permutations:
        for i in range(len(perm) + 1):
            # Insert the first character at position i
            new_permutation = perm[:i] + first_char + perm[i:]
            permutations.append(new_permutation)

    return permutations


if __name__ == '__main__':
    #    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    test_input = 'abcd'
    perm = get_permutations(test_input)
    print(f"\nPermutations of {test_input}:\n {perm}")
