# DSCI510 Project Part 2
- The script is the python script designed to extract data from the Api source.




## General information:
- File name: scraper.py
- Api source: [https://imdb-api.com/en/API/BoxOfficeAllTime/k_pv17fc8j]
- Program needed to run the script: python
- This script is also runnable from the command line (terminal)



## Function:
- This particular script contains code that scrapes the movies that are "Best Box Office of All Time" from IMdb Api database. The script is be runnable from the command line with three different inputs: 



## Instructions:

1. First of all, the user needs to turn on terminal

2. Then, the user needs to activate python program and identify the correct file path where the script is saved on their electronic tablet. The first command line input, "scraper.py" will print out the entire dataset extrated from the Api source. 

- Input format: python + file path + scraper.py
- one example would be: python /Users/Naomi/Desktop/scraper.py
- expected results: the complete scraped dataset as rows of data

3. Next, a user can use the second command line "--scrape N" to print the first N entries of data from the scraped dataset. (premise: N is a integer number). 

- Input format: python + file path + scraper.py --scrape N
- one example would be: python /Users/Naomi/Desktop/scraper.py --scrape 3; In this case, 3 entries of data will be printed.
- expected results: N rows of data from the scraped dataset will be printed. (if N is bigger than the total number of rows, only partial of the dataset will printed. For example 10 rows of data)

4. Finally, after the scraping, the user might want to save the scraped dataset. The last command line is "--static"，and it will help save the complete scraped dataset from the Api source into a .csv file passed as input. 

- Input format: python + file path + scraper.py --static + intended file path + name.csv
- one example would be: python /Users/Naomi/Desktop/scraper.py --static /Users/Naomi/Desktop/api-scraped.csv 
- expected results: the .csv file will appear in the folder chosen by the user



## Additional notes:

1. The "+" sign in the "Input format" mentioned above is not included in the command line code. The complete command line should always be composed of "python" followed by "file path" (e.g./Users/Naomi/Desktop) and then followed by "/scraper.py". The inputs themselves follows "/scraper.py" and is connected by " --" (There's no addition space after " --". e.g. " --scrape 3" " --static")

2. The examples above are applied succeccfully on the contributer's tablet and the users' paths might vary.



## Contributor:
- Naomi Deng 
- naizheng@usc.edu





