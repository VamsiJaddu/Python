scores = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 110 , 66 , 40 , 1]

######## sum of the list
result = sum(scores)
print(result)

#### for loop to iterate over the list and print each score
total = 0
for score in scores:
    total += score
print(f"{total} is the total of the scores so far")


######## max of the list
result = max(scores)
print(result)

###### for loop to iterate over the list and print each score
heighest = 0
for score in scores:
   if heighest < score:
      heighest = score
print(f"{heighest} is the heighest score so far")

######## min of the list
result = min(scores)
print(result)

###### for loop to iterate over the list and print each score
lowest = scores[0]
for score in scores:
   if lowest > score:
      lowest = score

print(f"{lowest} is the lowest score so far")

