# Description
Text-analysis microservice, based on AWS, which can process a text file from request, and create two files:
- **json** file, with latin based **words** and their **amounts**,
- **csv** file, with sorted **integers** and their preceding and consequent **fibonacci integers** (if the original integer is fibonacci, if not, there is nothing in those columns).
![](docs/microservice_architecture.png)

# API endpoint -  /analyzeText
POST request specs:
  - text/plain content type,
  - maximum 500KB,
  - right amount of integers and words,
  - lack of too long integers.

Responds with 200 code when successful.

# Corner cases
- too big file slows down the function
  - SOLUTION: max 500KB file size
- too many words slow down the function
  - SOLUTION: 2500 maximum distinct words
- too big numbers and too many numbers
  - SOLUTION: quadratic function based on function performance data, that gives time approximation based on integer length, which is used to reject lists of integers, that would take too long to process
![](docs/quadratic%20function.png)
- request with no data or wrong data
  - SOLUTION: request parsing
- request gets parsed even when quadratic function was supposed to stop it
  - (TEMP)SOLUTION: change of timeout on lambda to 30 seconds