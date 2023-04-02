from doit4u import DoIt4U
import time
import pandas as pd

# Create the agent
doit = DoIt4U()

# Example #1: Factorial function
print("---- Example #1: Factorial function ----")

print(
    doit.forme(
        "Write me a factorial function that takes a number as input and returns the factorial of that number."
    )(5))

# Example #2: Calculate the area of a circle
print("---- Example #2: Calculate the area of a circle ----")
time.sleep(1)
for i in range(1, 10):
    print(
        "Radius: ", i, "Area:",
        doit.forme(
            "Write me a function that takes the radius of a circle as input and returns the area of the circle."
        )(i))

# Example #3: Use of a library
print("---- Example #3: Operation on a dataframe ----")
time.sleep(1)
df = pd.DataFrame({
    "a": [1, 1, 3, 4],
    "b": ['a', 'a', 'b', 'b'],
    "c": [1, 2, 3, 4],
    "d": [-1, -2, -3, -4]
})

print(
    doit.forme(
        ''' Write me a function that takes a dataframe and a list of column names as input,
        Then aggregate the dataframe by the input list of names,
        Then get the the mean and maximum of the other columns by group as results,
        Then sort the results in reversed by order of the first column in the input list,
        Then return the aggregated result.
    ''')(df, ['a', 'b']))
