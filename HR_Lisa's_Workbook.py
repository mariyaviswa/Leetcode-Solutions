"""
Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters.
Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located.
The format of Lisa's book is as follows:

There are n chapters in Lisa's workbook, numbered from 1 to n.
The ith chapter has arr[i] problems, numbered from 1 to arr[i].
Each page can hold up to k problems. Only a chapter's last page of exercises may contain fewer than k problems.
Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
The page number indexing starts at 1.
Given the details for Lisa's workbook, can you count its number of special problems?

Example
-------
arr = [4,2]
k = 3

Lisa's workbook contains arr[1] = 4 problems for chapter 1, and arr[2] = 2 problems for chapter 2. Each page can hold k = 3 problems.

The first page will hold  3 problems for chapter 1. Problem 1 is on page 1, so it is special. Page 2 contains only Chapter 1,
Problem 4, so no special problem is on page . Chapter 2 problems start on page 3 and there are 2 problems.
Since there is no problem 3 on page 3, there is no special problem on that page either. There is 1 special problem in her workbook.

Note : for better explanation see the hackerrank page diagram

one-line explain : if the page number in the list of problems(i.e, 1,2,3) then it's the special problem

Example: page No 1 then it contains problems = [1,2,3]. Now we can see the page number in the problems list then it's the special problem

"""


def workbook(n, k, arr):
    # Write your code here
    page = 1
    values = {}  # store each pages problems so that can count easily the special problems
    for num in arr:
        if num <= k:  # if the chapter's problem less than or equal to k
            values[page] = [x for x in range(1, num + 1)]
            page += 1
        else:  # if not
            problems = 1
            while problems <= num:
                # Then add the k problems in  each page until loop terminate
                values[page] = [x for x in range(problems, problems + k) if x <= num]
                problems += k
                page += 1
    length = len(values.keys())  # find the total pages
    count = 0
    for n in range(1, length + 1):
        if n in values[n]:
            count += 1  # count the special problems
    return count


first_multiple_input = input().rstrip().split()
Total_problems = int(first_multiple_input[0])
problem_limit = int(first_multiple_input[1])
problems_count = list(map(int, input().rstrip().split()))
print(workbook(Total_problems, problem_limit, problems_count))
