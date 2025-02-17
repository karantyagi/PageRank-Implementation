''' Implementation of page rank algorithm

 // P is the set of all pages; |P| = N
 // S is the set of sink nodes, i.e., pages that have no out links
 // M(p) is the set (without duplicates) of pages that link to page p
 // L(q) is the number of out-links (without duplicates) from page q
 // d is the PageRank damping/teleportation factor; use d = 0.85 as a fairly typical value

 foreach page p in P
   PR(p) = 1/N                          /* initial value */

 while PageRank has not converged do
   sinkPR = 0
   foreach page p in S                  /* calculate total sink PR */
     sinkPR += PR(p)
   foreach page p in P
     newPR(p) = (1-d)/N                 /* teleportation */
     newPR(p) += d*sinkPR/N             /* spread remaining sink PR evenly */
     foreach page q in M(p)             /* pages pointing to p */
       newPR(p) += d*PR(q)/L(q)         /* add share of PageRank from in-links */
   foreach page p
     PR(p) = newPR(p)

 return PR
'''

from utils import *
import math
import operator
import sys
import pprint
import os.path

''' DESCRIPTION

    The webgraph consists of webpages(wikipedia articles) and links (inlinks and outlinks).

    A webpage is represented as a list having [url, level] where:
    url (string) is the url of the wepage in the format
    level (int) is the level of the node in the BFS search,
    We also have another data structure: List of nodes, example 'crawled_urls'
    and 'processed' are list of nodes.

    Any downloaded webpage is a document.
    Every document has a unique docID, which is the webpage title directly
    extracted from the URL of the webpage.
    Example:
    docID for webpage "https://en.wikipedia.org/wiki/Solar_Eclipse" is
    Solar_Eclipse

    A Document is represented as a dictionary with docID as the key and its
    inlinks as the values.

    Crawled webpage/url :

    Frontier :

    crawled_urls :

    Here a webpage is a node in the inlinks webgrapgh.
    Webpage/page is represented as a docID(string)


'''
# -------------------------------------------------------------------------

filename = str(sys.argv[1])


inlink_graph = dict() # dictionary consisting of webpages and thier inlinks
outlink_graph= dict() # dictionary consisting of webpages and thier outlinks
P = {}                # the set of all pages
S = {}                # the set of sink nodes(webpages with 0 outlinks)
L = dict()            # outlinks dictionary with page as key and the no.of
                      # outlinks(without duplicates) as value.

# M(p) is the set (without duplicates) of pages that link to page
# M(p) = set(inlink_graph[p])
''' use mylist = list(set(mylist)) for unique no of outlinks ..'''
PR = dict()              # PageRank dictionary - pages as keys and
                         # their respective page ranks as their value
newPR = dict()           # dictionary for temporary page ranks calculation

d = 0.85                # d is damping/teleportation factor

## Loading inlink webGraph
inlink_graph = load_inlink_webgraph(filename)
outlink_graph = compute_outlinks_graph(inlink_graph)

# test - print inlink webGraph
print('\n\n\t\t\tInlinks webgraph dictionary\n')
#print_graph(inlink_graph)

# test - print outlink webGraph
print('\n\n\t\t\tOutlinks webgraph dictionary\n')
#print_graph(outlink_graph)

## Finding all Pages
P = set(inlink_graph.keys()) # set of all pages
N = len(P)
## print("\n  Pages",P)
print("\n  No. of Pages : ",N)


## Finding Sinks
S = find_sinks(outlink_graph)
## print("\n  Sinks",S)

# page is the key
# value is a list of outlinks for the given page
for page,outlinks in outlink_graph.items():
    L[page] = len(set(outlinks))
## print("\n  Number of outlinks per page \n\n ",L,"\n")

convergence = False

def entropy():
    sum = 0.0
    for i,pagerank in PR.items():
        sum += PR[i]*(math.log(PR[i])/math.log(2))
    sum = sum*-1
    return sum

def perplexity():
    return math.pow(2,entropy())

def perplx_change(lst):
    return abs(lst[len(lst)-1] - lst[len(lst)-2])

def converged(perpx_list):
    print(" ===== convergence func called=====")
    if len(perpx_list) > 4:
        count = 0
        for i in range(len(perpx_list)-1,(len(perpx_list)-6),-1):
            if abs(perplx_list[i] - perplx_list[i-1]) < 1:
                count +=1
                #print(abs(perplx_list[i] - perplx_list[i-1]))
                print("Consecutive iteration : {} - {}".format(i,i-1))
                if count == 4:
                    print("convergence reached")
                    return True
                continue
            else:
                return False
    else:
        return False

## initial page rank values
for p in P:
    PR[p]=1.0/N

## calculate the page rank of each page till the page ranks converge


perplx_list = []
# create path if it does not exist
createPath("../output/"+filename.split('.txt')[0]+"/")
perpxFile = open("../output/"+filename.split('.txt')[0]+"/"+filename.split('.txt')[0]+"_perplexity_details.txt","w")
iteration = 0

# initial perplexity value
perplx_list.append(perplexity())

perpxFile.write("Iteration".ljust(14)+"Perplexity after iteration".ljust(30)+"Change in perplexity\n\n")
#perpxFile.write("\n Iteration  |  Perplexity value after iteration\n\n")
perpxFile.write("Round 0".ljust(14)+str(perplx_list[0]).ljust(30)+"Initial Perplexity")

while not convergence:
    iteration += 1                  ## start as 1st iteration
    sinkPR = 0
    for s in S:                     ## Calculating total sink values
        sinkPR += PR[s]
    for p in P:
        newPR[p] = (1.0 - d)/N     ## Teleportation
        newPR[p] += d*sinkPR/N  ## Spreading remaining sink PR evenly
        for q in set(inlink_graph[p]):
            newPR[p] += d*PR[q]/L[q]

    for page in P:
        PR[page] = newPR[page]

    # computing new perplexity values
    perplx_list.append(perplexity())
    perpxFile.write(("\nRound {}".format(iteration).ljust(15)
    +str(perplx_list[iteration]).ljust(30)
    +str(perplx_change(perplx_list))))

    print("***** perplexity list length : ",len(perplx_list))
    if converged(perplx_list):
        convergence = True  # convergence achieved, halt now


perpxFile.write("\n\nConvergence achieved")
perpxFile.close()
print("\n",filename.split('.txt')[0]+"_perplexity_details.txt created.\n")

## print_pageranks(PR)
#print(perplx_list)

webgraph_Stats(inlink_graph)
top_n_PR(50,filename,PR)
top_n_inlinks(50,filename,inlink_graph)
