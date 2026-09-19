# Grade Classifier
A simple program that reads a numeric score (0-100) and reports the corresponding letter grade.

## Setup
-python -m venv .venv
-source .venv/bin/activate  # Windows: .venv\Scripts\activate
-pip install -r requirements.txt

## Run
python lab1.py

## Example
Enter a score from 0-100: 85
Grade: B

Enter a score from 0-100: abc
'abc' is not a valid number. Please enter a number between 0 and 100.

Enter a score from 0-100: 150
150.0 is out of range. Please enter a value between 0 and 100.

## Known limitations
- Only accepts a single score per run; does not support batch input from a file.
- Does not round or format decimal scores (e.g. 89.999 is treated as below 90).
