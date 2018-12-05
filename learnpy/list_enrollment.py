#Define a function, enrollment_stats() , that takes, as an input, a list of lists where each
#individual list contains three elements: (a) the name of a university, (b) the total number
#of enrolled students, and (c) the annual tuition fees.
#Sample list:
#universities = [
#['California Institute of Technology', 2175, 37704],
#['Harvard', 19627, 39849],
#['Massachusetts Institute of Technology', 10566, 40732],
#['Princeton', 7802, 37000],
#['Rice', 5879, 35551],
#['Stanford', 19535, 40569],
#['Yale', 11701, 40500]
#]
#This function should return two lists: the first containing all of the student enrollment
#values and the second containing all of the tuition fees.
#Next, define a mean() and a median() function. Both functions should take a single list
#as an argument and return the mean and median from the values in each list. Use the
#return values from enrollment_stats() as arguments for each function. Challenge
#yourself by finding a way to sum all the values in a list without using the built-in
#'sum()' function for calculating the mean.
#At some point you should calculate the total students enrolled and the total tuition paid.
#Finally, output all values:

def enrollment_stats(students_tuition_lists):
    enrollment_numbers = []
    tuition_fees = []

    for n in range(0, len(students_tuition_lists)):
        enrollment_numbers.append(students_tuition_lists[n][1])
        tuition_fees.append(students_tuition_lists[n][2])    
    return enrollment_numbers, tuition_fees

def mean(to_calc_list):
    sum = 0
    for n in range(0, len(to_calc_list)):
        sum += to_calc_list[n]
    return sum/len(to_calc_list)
    
def median(to_calc_list):
    median_index = (len(to_calc_list) + 1)/2
    to_calc_list.sort()
    return to_calc_list[int(median_index)-1]
    
universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]
enrolled_students_list, tuition_fees_list = enrollment_stats(universities)
total_enrolled_students = sum(enrolled_students_list)
sum_tuition_fees = sum(tuition_fees_list)

average_number_of_students_enrolled = int(mean(enrolled_students_list))
median_students = median(enrolled_students_list)

average_tuition_fees = mean(tuition_fees_list)
median_tuition_fees = median(tuition_fees_list)


print(f"Enrolled students list : {enrolled_students_list}")
print(f"Tuition Fees list : {tuition_fees_list}")
print(f"Total Enrolled students : {total_enrolled_students}")
print(f"Sum of fees : {sum_tuition_fees}")
print(f"Avg # of students : {average_number_of_students_enrolled}")
print(f"Median students :  {median_students}")
print(f"Average fees : {average_tuition_fees}")
print(f"Median fees : {median_tuition_fees}")
