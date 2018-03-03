import os.path
import operator
from operator import itemgetter
from collections import OrderedDict

# Given   : file with inlink graph adjacency list representation
# example of txt file :
#
# Effect  : initializes the inlinks webgraph dictionary
''' initializes / populates  [Possible wrong use of word] '''

def load_inlink_webgraph(filename):
    inlink_dict = dict()
    values = []
    count = 1
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename) as f:
            line = f.readline()
            while line:
                key = line.split()[0]
                values = line.split()
                values.pop(0)
                inlink_dict[key] = values
                #print(key)
                #print(values)
                #print(line.split())
                #print("Line {}:    Key : {}     |     {}".format(count,key,line.strip()))
                line = f.readline()
                count += 1
    return inlink_dict

###############################################################################
''' Compute all outlinks of a page'''
# Given   :
# Returns :
def compute_outlinks(page,inlink_graph):
    outlinks = []  # list of outlinks (webpage docIDs)
    for key,value in inlink_graph.items():
        for pg in value:
            if pg == page:
                if key not in outlinks:
                    outlinks.append(key)
    return outlinks

###############################################################################

# Given   :
# Returns :

def compute_outlinks_graph(inlink_graph):
    outlink_dict = dict()
    for page in inlink_graph:
        outlinks = compute_outlinks(page,inlink_graph)
        outlink_dict[page] = outlinks
    return outlink_dict

###############################################################################

# Given   :
# Returns :

def find_sinks(outlink_graph):
    sink = []
    for page in outlink_graph:
        if(len(outlink_graph[page])==0):
            sink.append(page)
    return set(sink)

###############################################################################

# Given  :
# Effect :
def print_graph(webgraph):
    print('\n==========================================================================================================')
    for key, value in webgraph.items() :
        print("  {}".format(key).ljust(30),value)
    print('===========================================================================================================')

###############################################################################

# Given  :
# Effect :
def print_pageranks(PR):
    #sortedPR = sorted(PR.items(), key=operator.itemgetter(1), reverse=True)
    #sortedPR = sorted(PR.items(), key=lambda x: x[1])
    sortedPR = OrderedDict(sorted(PR.items(), key=itemgetter(1),reverse=True))
    print('\n==================================== Page Ranks==========================================================')
    for key, value in sortedPR.items() :
        print(" Page:  {}".format(key).ljust(50)," PageRank:  {}".format(value))
    print('===========================================================================================================')

###############################################################################

# Given  :
# Effect : create path if it does not exist
def createPath(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
            os.makedirs(dir)

###############################################################################
# Given  :
# Effect :
def top_n_PR(n,filename,PRdict):
    # create path if it does not exist
    createPath("../output/"+filename.split('.txt')[0]+"/")
    f = open("../output/"+filename.split('.txt')[0]+"/"+filename.split('.txt')[0]+"_Top"+str(n)+"PageRanks.txt","w")
    i = 1
    sortedPR = OrderedDict(sorted(PRdict.items(), key=itemgetter(1),reverse=True))
    for page,rank in sortedPR.items():
        if i > n:
            break
        f.write(str(page).ljust(48)
        +'{}'.format(rank)+"\n")
        i +=1
    f.close()
    print("\n"+filename.split('.txt')[0]+"_Top"+str(n)+"PageRanks.txt created.")


###############################################################################

# Given  :
# Effect :
def top_n_inlinks(n,filename,inlink_dict):
    # create path if it does not exist
    createPath("../output/"+filename.split('.txt')[0]+"/")
    f = open("../output/"+filename.split('.txt')[0]+"/"+filename.split('.txt')[0]+"_Top"+str(n)+"Inlinks.txt","w")
    i = 1
    sorted_dict = OrderedDict(sorted(inlink_dict.items(), key=lambda x: len(x[1]),reverse=True))
    for page,inlinks in sorted_dict.items():
        if i > n:
            break
        f.write(str(page).ljust(48)
        +'{}'.format(len(inlinks))+"\n")
        i +=1
    f.close()
    print("\n"+filename.split('.txt')[0]+"_Top"+str(n)+"Inlinks.txt created.")

###############################################################################


# Given   :
# Effect  :

def webgraph_Stats(webgraph):
    sink = [] # outlink count = 0
    source = [] # inlinks count is 0
    in_count = 0
    out_count = 0
    max_inlinks = 0
    max_outlinks = 0
    #avg_inlinks
    #avg_outlinks

    print("\n\t Web Graph Stats . . . . . . . . . .   [Computing - plz wait for 5 secs at max]")
    print('\n\tNodes    : ',len(webgraph))
    for key, values in webgraph.items():
        outlnk = len(compute_outlinks(key,webgraph))
        out_count+=outlnk
        in_count+=len(values)
        if outlnk == 0:
            sink.append(key)
        if len(values) == 0:
            source.append(key)
        if(len(values) > max_inlinks):
            max_inlinks = len(values)
        if(outlnk > max_outlinks):
            max_outlinks = outlnk
    print('\tSinks    : ',len(sink))
    ## print('\t',sink)
    print('\tSources  : ',len(source))
    ## print('\t',source)
    print('\tMax number of inlinks for any node  : ',max_inlinks)
    print('\tMax number of outlinks for any node : ',max_outlinks)
    print('\tAverage inlinks per node            : ',(in_count/len(webgraph)))
    print('\tAverage outlinks per node           : ',(out_count/len(webgraph)))

###############################################################################
