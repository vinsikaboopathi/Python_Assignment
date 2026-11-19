# Python Programming Assignment

## Assignment 01 – Fundamentals of Python Programming

This assignment focuses on basic Python programming concepts such as string operations, conditional statements, Boolean logic, comparison operators, lists, and tuples.

## Q1 – Username Validation System

The program validates a username based on the following rules:

- Username must contain at least 5 characters.
- Username must not contain only spaces.
- Username must not be equal to "admin", ignoring uppercase and lowercase.

### Sample Output

Enter username: Anjali123  
Valid username.

Enter username: abc  
Invalid username: Username must contain at least 5 characters.

Enter username: ADMIN  
Invalid username: Username cannot be admin.

---

## Q2 – Student Marks Analysis

Sample marks:

[78, 35, 92, 40, 61]

The program:

- Creates a list and converts it into a tuple.
- Displays their data types.
- Finds the highest and lowest marks.
- Counts students scoring at least 40.
- Checks whether all marks are within the valid range of 0 to 100.
- Demonstrates the difference between a list and a tuple.

### Sample Output

List: [78, 35, 92, 40, 61]

List type: <class 'list'>

Tuple: (78, 35, 92, 40, 61)

Tuple type: <class 'tuple'>

Highest mark: 92

Lowest mark: 35

Students scoring at least 40: 4

All marks are valid: True

Modified list: [100, 35, 92, 40, 61]

---

## Q3 – Online Shopping Discount Eligibility

The program calculates discount eligibility based on order amount and membership.

### Discount Rules

- Orders of ₹5,000 or more receive a 15% discount.
- Members with orders from ₹2,000 to below ₹5,000 receive a 10% discount.
- Other valid orders receive no discount.
- Orders below ₹0 or above ₹1,00,000 are invalid.

### Sample Output

#### Test 1

Original amount: 6000.0  
Discount percentage: 15 %  
Discount amount: 900.0  
Final payable amount: 5100.0  
Eligibility status: Eligible for discount

#### Test 2

Original amount: 3000.0  
Discount percentage: 10 %  
Discount amount: 300.0  
Final payable amount: 2700.0  
Eligibility status: Eligible for discount

#### Test 3

Original amount: 1500.0  
Discount percentage: 0 %  
Discount amount: 0.0  
Final payable amount: 1500.0  
Eligibility status: Not eligible for discount

#### Test 4

Invalid order amount.

## Files Included

- Q1.py
- Q2.py
- Q3.py

## Conclusion

This assignment helped in understanding and applying basic Python programming concepts through practical problems.
