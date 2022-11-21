#Function Prompt

int_list = (1,2,5,4,3)

def sort_tup(list):
  #list.append(6)
  return sorted(list)

print(sort_tup(int_list))

# How does this solution ensure data immutability?
   ## We created the initial data inot a variable into a tuple to ensure it is 
   ## immutable. 

# Is this solution a pure function? Why or why not?
   ## Yes, it serves on purpose, and that is too sort the tuple

# Is this solution a higher order function? Why or why not?
  ##No.it does not accept a function as an argument.

# Would it have been easier to solve this problem using a different programming style?
  ## Not Really. The solutions is pretty concise and uses a built in method
  ## to sort through the tuple

# Why in particular is functional programming a helpful paradigm when solving this problem?
  ## Because we are asked to fulfill a simple function and purpose to sort the       ## array, and no matter what list is passed, it will always return that list 
  ## sorted, and unchanged.

