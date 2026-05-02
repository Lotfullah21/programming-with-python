# Aliasing
subjects = ["Artificial Intelligence", "Machine Learning", "Deep Learning"]
AI_subjecs = subjects
print(subjects)
print(AI_subjecs)
# change the last element
AI_subjecs[-1] = "Python"
# we can see, it changes both of the lists present here
print("AI_SUBJECTS = ", subjects)
print("SUBJECTS = ", AI_subjecs)

subjects.append("Computer Vision")
print(subjects)

# NOT EQUAL
print("---- NOT EQUAL ----\n")
maths = ["algebra", "calculus", "statistics"]
science = ["algebra", "calculus", "statistics"]
print("is maths == science?", maths == science)
print("maths = ", maths)
maths[-1] = "Probability"
print("maths = ", maths)
print("science = ", science)

# Cloning
L1 = [1, 2, 3, 4, 5]
L2 = L1[:]
print("L1 = ", L1, "\nL2 = ", L2)
L2[2] = 10
L1[2] = 12
print("L1 = ", L1, "\nL2 = ", L2)
