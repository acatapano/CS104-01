avergae = 0.0
numberOfTests = 0
score = 0
scoreCount = 0
total = 0

numberOfTests = int(input("Please enter the number of tests you want to average: "))
score = int(input("Please enter a score: "))
scoreCount = scoreCount + 1
total = total + score   #Can also be total += score
average = total/scoreCount
print("The average is ", average)
