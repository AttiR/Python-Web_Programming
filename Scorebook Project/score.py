# Python program to organize Palyers matches and score data
# Lists Concept

players = ["Asad", "Umar", "Gondal", "Pankaj"]
scores = [10, 4, 56, 89]

# combining scores in 2D lists
scorebook = [["Asad", 10], ["Umar", 4], ["Gondal", 56], ["Pankaj", 89]]
print(scorebook)

# Adding extra player in list
scorebook.append(["Tariq", 87])
scorebook.append(["Bara", 20])

# Modification of lists
# correction in scores of Pankaj
scorebook[3][1] = 67
print(scorebook)

# Remove score form player one and add comment "welldone"
scorebook[0].remove(10)
scorebook[0].append("weldone")
print(scorebook)
