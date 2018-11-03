#divide and conquer algorithm
#Breaks list into smaller parts, sorts, and then merges
"""When splitting the data, we divide the input to our sort in half.
We then recursively call the sort on each of those halves, which cuts the halves into quarters.
This process continues until all of the lists contain only a single element. Then we begin merging."""

"""When merging two single-element lists, we check if the first element is smaller or larger than the other.
Then we return the two-element list with the smaller element followed by the larger element."""
#Best worst and average time is the same
#Doesn't touch original list, makes a new temp array for every iteration
