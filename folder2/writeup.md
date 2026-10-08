Sabrina Sullivan 
September 18, 2026 
Homework 2 
Part 1 
1.  A datasheet for a dataset is a document that explains important information about a 
dataset. It describes how the data was collected, what it is used for, who created it, and its limitations. It helps people understand the data before they use it.  
2.  The authors think datasets are important because they make datasets more transparent and easier to understand. They help users identify potential biases, limitations, and ethical concerns. They also help prevent datasets from being misused.  
3.  The process was iterative because the author repeatedly revised their guidelines based on feedback and what they learned during development. It was incremental because they built the guidelines step by step, gradually adding questions and making improvements. This helped them create a more useful and complete framework.  
4.  First questions could be “What are the limitations of the dataset?” and this question would help users understand the weaknesses of the data. For example, a dataset collected from a college might not represent all college students everywhere. This can prevent people from making inaccurate generalizations. Another question could be “Who funded the creation of the dataset?” and this question helps users understand whether the people funding the dataset might have influenced how the data was collected and it could reveal biases and conflicts of interest. 
Part 3 
1.  The bug in pick_dinner occurs when both is_weekday and have_eggs are False. In this 
case, neither condition runs, so the variable dinner is never assigned a value. This causes an UnboundLocalError when the function tries to return dinner. I fixed the problem by adding an else statement that assigns dinner the value “Something else” when neither condition is true.  
2.  The error in quadratic_formula happens when the number inside the square root is 
negative. For example, the inputs (1,0,1) cause a ValueError because the square root 
becomes math.sqrt(-4). I fixed the function by using an if statement to check if the 
number inside the square root is negative. If it is, the function prints a message and stops instead of causing an error.  
3.  The first bug was that the temperature check used and instead of or, so the program could never identify an invalid temperature. Another bug was that the function used return statements, which meant that some weather advice would not be displayed unless the function’s result was printed. When the temperature was above 50 degrees and it was both raining and sunny, the function only returned one piece of advice instead of both. I fixed these problems by changing and to or and using print() statements to display the weather advice.  
 
Part 5: 

Question: Write a Python program that helps a student plan their schedule for a campus event. Your program should use functions to calculate how much time the student has available and determine whether they can attend the event. 
Your program must include the following functions: 
Function 1: available_time 
Write a function called available_time(start_time, end_time) that takes two integers representing the time a student is free to study or attend an event. The times should be represented in hours using a 24-hour clock. Return the number of hours the student is available. Assume the end time is later than the start time. 
Function 2: can_attend 
Write a function called can_attend(available_hours, event_length) that takes the number of hours the student is available and the length of the event. Return True if the student has enough time to attend the event. Return False if the student does not have enough time. 
Write driver code that: Asks the user what time they become available. Asks the user what time they need to leave. Asks the user how long the event will last. Calls the available_time() function to calculate the student's free time. Calls the can_attend() function to determine whether the student can attend. Prints the amount of free time and a message explaining whether the student can attend the event. 
Test your program with at least three different sets of inputs, including one where the student does not have enough time. 
 
Explanation of Question: 
This question assesses a student’s ability to write and use functions in Python. It requires students to create functions with parameters, return values, and calls to those functions from the main part of the program. The most challenging part for students may be understanding how information is passed into a function and how the returned result can be used by another function. Students may also struggle withkeeping track of which parts of the program belong inside a function and which belong in the driver code.
