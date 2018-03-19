## FizzBuzz

### Specifications
_NOTE: You should alread have a public repository called `data-structures-and-algorithms_
- Create a branch in your repository called `fizzbuzz`.
    - **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- On your `fizzbuzz` branch create a file called `fizzbuzz.py`.
    - **If you call it anything else, you will get ZERO CREDIT with NO COMMENTS**
- Include any language-specific configuration files required for this challenge or data structure to become an individual component, module, library, etc.
    - _Note: You can find an example of this configuration for your course in the [configs/]() directory._

### Feature Tasks
- Write a function which accepts `n` as an argument, and prints the following logic to standard out:
    - If `n` is divisible by `3`, print `fizz`
    - If `n` is divisible by `5`, print `buzz`
    - If `n` is divisible by `3` and `5`, print `fizzbuzz`
    - Else print `n`

### Testing
- Write at least three test assertions for each method that you define. Your methods should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

### Example
```
< fizzbuzz(20)
> 1
> 2
> fizz
> 4
> buzz
> fizz
> 7
> 8
> fizz
> buzz
> 11
> fizz
> 13
> 14
> fizzbuzz
> 16
> 17
> fizz
> 19
> buzz
```

### Challenge / Data Structur Documentation
```md
# FizzBuzz
Fizz buzz is a group word game for children to teach them about division.[1] Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", and any number divisible by five with the word "buzz".

## Challenge
Write a function which accepts `n` as an argument, and prints the following logic to standard out:
    - If `n` is divisible by `3`, print `fizz`
    - If `n` is divisible by `5`, print `buzz`
    - If `n` is divisible by `3` and `5`, print `fizzbuzz`
    - Else print `n`
```

### Example Pseudocode
```
ALGORITHM FizzBuzz(n)
// Input ←  a non-negative integer n
// Output ←  no return

for i ←  0 to n do
if i mod 3 AND i mod 5
output ←  “Fizzbuzz”
else if i mod 3
          	output ←  “Fizz”
else if i mod 5
          	output ←  “Buzz”
else
          	output ←  i
```

### Submission Instructions
1. Create a pull request from your `fizzbzz` branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents) of the specifications above, with the actual specifications you completed checked off.
3. Submitting your completed work to Canvas:
    - Copy the link to your open pull request and paste it into the corresponding Canvas assignment.
    - Using the File Upload feature, upload a photo of your completed pseudocode whiteboarding exercise.
    - Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge `fizzbuzz` into `master`
