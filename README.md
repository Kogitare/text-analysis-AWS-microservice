# Description
Text-analysis tool, which uses local files to find integers and count words (or character sets) made using latin alphabet. The files are:
- `./input/text_in.txt` file as input,
- `./output/output.csv` file as output for numbers. Contains 3 columns:
  - **_previous Fibonacci number_** - with integers preceding **_observed number_** in fibonacci sequence,
  - **_observed number_** - integers from the text file (if an integer is not in fibonacci sequence, then preceding and consecutive cell is blank),
  - **_next Fibonacci number_** - with integers consecutive to **_observed number_** in fibonacci sequence;
- `./output/output.json` file as output for words. Contains every latin-based word and how many of it were in the text file.