CS 6200 INFORMATION RETRIEVAL Spring 2018
Assignment 2

Author : Srijit Ravishankar
NUID : 001282238

SUMMARY :
		** The given instructions contains software installations and running the program that is suitable in MAC environment ** 


GENERAL INSTRUCTIONS :
1. Install Python v.3.6.1


INSTRUCTIONS TO RUN THE PROGRAM : 
1. Open Terminal
2. Navigate to the desired directory
3. Enter the command "python Task2.py"
4. Enter the file name of the graph to generate the page rank and perplexity values. (In this case G1.txt and/or G2.txt)


OTHER INSTRUCTIONS :

G1.txt and G2.txt are the graphs generated from BFS and DFS respectively. 
The graph follows the pattern 

D1 D2 D3 D4
D2 D5 D6
D3 D7 D8

Where, D1 is the webpage docID which is the article title directly extracted from the URL (e.g., Renewable_energy is the docID for https://en.wikipedia.org/wiki/Renewable_energy). Each line indicates the in-­link relationship, which means that D1 has three in-­coming links from D2, D3, and D4 respectively.

The file "SIMPLE_STATISTICS_TASK1" has the statistics over G1 and G2 with the proportion of pages with no inLinks and pages with no outLinks.


Running Task2.py generates 4 files :
1. G1_PAGE_RANK_FOR_TOP_50_PAGES
2. G1_PERPLEXITY_VALUES
3. G2_PAGE_RANK_FOR_TOP_50_PAGES
4. G2_PERPLEXITY_VALUES

"QUALITATIVE_ANALYSIS_AND_SPECULATION_TASK3"  examines the Top 10 page rank and the Top 10 by inLink counts for G1 and G2. It also has details on how the page rank works and inference from the mentioned results.