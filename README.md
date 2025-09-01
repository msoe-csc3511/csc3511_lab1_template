## Introduction

For this assignment, will be asked to answer questions and/or write some code.  Provide complete answers to all written questions:  When asked for examples, be specific.  Submit your answers in a document separate from code.

Include source files for all programs in your submission.  Follow good styling for programming questions and provide complete documentation (comment blocks, inline comments for complicated code, etc.).

The purpose of this assignment is to:

1. Research and practice with different byte encodings for data
2. Refresh your understanding of the python programming language

Work on the assignment is to be done with ***your assigned group***.  You are welcome to collaborate with class members, but the submitted assignment must be the work of only your group.

## Background and References

In a computer network, data is transferred between end-points (typically a computer/phone or other electronic device) through one or more messages.  Messages typically consist of a series of bytes in a particular format.  A message format is a description of the context associated with the bytes so that the sender and receiver can interpret the data contained within the message.

The following resources might be useful:

- Geeks for Geeks - Computer Networks - [https://www.geeksforgeeks.org/basics-computer-networking](https://www.geeksforgeeks.org/basics-computer-networking)
- Geeks for Geeks - Network Terminology - [https://www.geeksforgeeks.org/introduction-to-basic-networking-terminology/](https://www.geeksforgeeks.org/introduction-to-basic-networking-terminology/)

## Project Description

### Data Encoding

As a human we often think of data in terms of numbers, letters, words, or other symbols to give that data context (relational tables, graphs, drawings, etc.).  However, to a computer data is represented as electrical signals passing through wires or silicon microprocessors.  These electrical signals typically have to modes, high voltage or low voltage (i.e. on or off, high or low, 0 or 1), in other words binary.  This requires us to figure out how to represent all data in terms two numbers: 0 or 1.

#### Number Bases and Encodings Research

Numbers are typically represented in a computer in binary (base 2).

***SUBMISSION REQUIREMENT:*** Research number bases (cite your sources), then answer the following questions:

1. What is a number base?
2. How do you convert between number bases?
3. What different number bases are useful for storing data in a computer?

#### Practice with Number Bases

Using what you know answer the following:

1. Convert 1837 from base 10 to base 2 - show your work
2. Convert 101011001 from base 2 to base 10 - show your work
3. Convert 738 from base 10 to base 8 - show your work
4. Convert 738 from base 10 to base 16 - show your work
5. Convert 18AA from base 16 to base 10 - show your work

#### Data Representation - Bits and Bytes

***SUBMISSION REQUIREMENT:*** Research bits and bytes (cite your sources), then answer the following questions:

1. What is binary digit (bit)?
2. What is a byte?
3. What is a nibble?
4. What is meant by endian?
5. What is big endian?
6. What is small endian?
7. How many numbers can be represented in 15 bits?
8. What is 2's complement?  How are numbers represented in bytes using 2's complement?
9. What is floating point?  How are numbers represented in bytes using floating point?

#### Data Representation - ASCII

***SUBMISSION REQUIREMENT:*** Research ASCII encoding for string characters, then answer the following questions:

1. What is ASCII?
2. When was ASCII developed?
3. What was ASCII modeled after?
4. How many bytes is each character in ASCII?
5. How is a string in ASCII character encoding terminated?
6. Convert the following strings to ASCII Hexadecimal
   1. Hello
   2. World
   3. abc123
   4. Up!Down

***SUBMISSION REQUIREMENT:*** Research other character encodings, name and describe **2** other character encodings.
- How does each differ from ASCII?
- What are they useful for?

### Python Practice

Python is a 'high level', general purpose, scripting language that will be used during this course.  This section is intended to familiarize (or refresh) your understanding of python by writing some functions/scripts.  Refer to the Python/Java 'cheat sheet' for help.

Located in your [src](src) directory are the following files:

- [deg_to_rad.py](src/deg_to_rad.py)
- [sort.py](src/sort.py)
- [compress.py](src/compress.py)
- [base_convert.py](src/base_convert.py)
- [str_to_hex.py](src/str_to_hex.py)

Use these files to implement the following:

1. Degrees to Radians - Without using a library function that does it, write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. The function should convert the radians into degrees and then return that value.
2. Sort a list - Without using a library function that does it, write a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: 'asc', 'desc', and 'none'.
   - If the second parameter is 'asc' return a copy of the list sorted in ascending order
   - If the second parameter is 'desc' return a copy of the list sorted in descending order
   - If the second parameter is 'none' return a copy of the list sorted the list unmodified.
   - NOTE: This function should ***NOT*** modify the input list.  It should return a copy
3. Simple string compression - Without using a library function, write a function in Python that accepts one string parameter. This parameter should be compressed as follows:
   - Count every contiguous repeating character
   - Preceded every character with its count
   - Return the resulting string
   <br/>
   For example, the string 'abbbcccccddd' should be compressed to '1a3b5c3d'.
4. Convert to a different number base - Without using a library function that does it, write a function in Python that accepts two parameters.  The first will be a positive integer in base 10 (NOTE: zero is a positive number).  The second parameter will be a positive integer greater than or equal to 2 and less than or equal to 10.  Convert the first parameter to the base of the second parameter and prints out the new value.
5. Convert a string to hexadecimal - Without using a library function that does it, write a function in Python that accepts one string parameter. Each character in the string should be converted to ASCII hexadecimal and printed out (using capital letters A-F for values > 10).  Print a space between each byte.  Do ***NOT*** print a space at the end of the string
   <br/>
   For example, the string 'aamm' should be printed out as `61 61 6D 6D`

## Deliverables

When you are ready to submit your assignment prepare your repository:

- Make sure your names, assignment name, and section number are in comments on ALL submitted files.
- Make sure you have completed all activities and answered all questions.
- Make sure you cite your sources for all research.
- Make sure your assignment code is commented thoroughly.
- Include in your submission, a set of suggestions for improvement and/or what you enjoyed about this assignment.
- Make sure all files are committed and pushed to the main branch of your repository.

***NOTE***: Do not forget to 'add', 'commit', and 'push' all new files and changes to your repository before submitting.

### Additional Submission Notes

If/when using resources from material outside what was presented in class (e.g., Google search, Stack Overflow, etc.) document the resource used in your submission.  Include exact URLs for web pages where appropriate.

NOTE: Sources that are not original research and/or unreliable sources are not to be used.  For example:

- Wikipedia is not a reliable source, nor does it present original research: [https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_is_not_a_reliable_source](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_is_not_a_reliable_source)
- ChatGPT is not a reliable source: [https://thecodebytes.com/is-chatgpt-reliable-heres-why-its-not/](https://thecodebytes.com/is-chatgpt-reliable-heres-why-its-not/)

For more information, please see the [MSOE CS Code of Conduct](https://msoe.s3.amazonaws.com/files/resources/swecsc-computing-code-of-conduct.pdf).

To submit, copy the URL for your repository and submit the link to Canvas.

## Grading Criteria

- (5 Points) Submitted files follow submission guidelines
    - Only the requested files were submitted
    - Files are contain name, assignment, section
    - Sources outside of course material are cited
- (5 Points) Suggestions
    - List of suggestions for improvement and/or what you enjoyed about this assignment
- (5 Points) Code Structure 
  - Readable code/file structure 
  - Code is well documented
- (7 Points) Number Bases and Encodings Research
- (8 Points) Practice with Number Bases
- (10 Points) Data Representation - Bits and Bytes
- (10 Points) Data Representation - ASCII
- (50 Points) Completion of Python Practice