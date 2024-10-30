import math

# Data
nums = [2, 3, 9, 8, 5, 50, 100, 26, 98, 500]
n = len(nums)

# Sort the data set
sorted_nums = sorted(nums)

# Quartiles
Q1 = sorted_nums[n // 4]

# Q2 (median)
if n % 2 == 0:
    median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
else:
    median = sorted_nums[n // 2]

# Q3
Q3 = sorted_nums[(3 * n) // 4]

# IQR
IQR = Q3 - Q1

# Whiskers for box plot calculation
low_whisker = Q1 - (1.5 * IQR)
high_whisker = Q3 + (1.5 * IQR)

# Mean
mean = sum(nums) / n

# Identify and classify outliers
low_end_outliers = [x for x in nums if x < low_whisker]
high_end_outliers = [x for x in nums if x > high_whisker]


# Sample Variance (avg of the squared deviations from the mean and divided by n-1)
# Calculate the sum of squared deviations from the mean
sum_squared_deviations = sum((x - mean) ** 2 for x in nums)

# Calculate the sample variance
sample_var = sum_squared_deviations / (n - 1)

# Sample standard deviation
standard_dev = math.sqrt(sample_var)



"""
"A test score of 85 was obtained by a student. 
If the class has a mean score of 70 and a standard deviation of 10, how unusual is the student's score? 
Is it above or below average, and how many standard deviations away is it from the mean?"
"""
# The z score is separate from the dataset
# Z score (how far a particular data point is from mean)
z_score = (85-70)/10

# Print the results
print(f"The mean is {mean}\n")
print(f"Q1 is {Q1}\n")
print(f"The median is {median}")
print(f"Q3 is {Q3}")
print(f"IQR is {IQR}\n")
print(f"Low whisker is {low_whisker}")
print(f"High whisker is {high_whisker}\n")


# Print low and high-end outliers separately
if low_end_outliers:
    print(f"Low-end outliers: {low_end_outliers}")
else:
    print("No low-end outliers\n")

if high_end_outliers:
    print(f"High-end outliers: {high_end_outliers}\n")
else:
    print("No high-end outliers\n")

print(f"The sample variance is: {sample_var}\n")

print(f"Standard Deviation {standard_dev}\n")

print(f"The z score is separate from the dataset {z_score}\n")