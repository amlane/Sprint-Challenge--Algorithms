#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)
We have 1 loop that will terminate based on how many times it takes to increment A to equal N.
The means the runtime for this psuedocode will grow at the same rate as N. For instance if N is 1 the loop will only have to run 1 time. If N is 2, the function will loop 2 times. If N is 10, it loops 10 times. Etc etc.

b) O(n^2)
We are looping through the same input list twice with the for and while loops, which makes this code block an O(n^2) solution. The runtime for this code will grow quickly as the number of inputs increase and probably isn't an ideal solution if the numbers of inputs will be a large number. For instance if n is 2, this loop will only need to run 1 time. If n is 4, the loop will need to run 8 times. If n is 10, will need to run 40 times. If n is 25, this loop will run 125 times. You can see the runtime is increasing at a much faster rate than the rate than n increases.

c) O(n)
This is a recursive solution that is looping based on the number of bunnies. Depending on the number of bunnies we have (n) will determine how many times we have to call this function.
We can test this by increasing our number of inputs and checking how many times the function is called. If we input 2 bunnies, we see the function is called 2 times. If we input 4, we see the function is called 4 times. Same with 10 bunnies, we loop the function 10 times.

## Exercise II
