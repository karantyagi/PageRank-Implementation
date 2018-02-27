#// P is the set of all pages; |P| = N
#// S is the set of sink nodes, i.e., pages that have no out links
#// M(p) is the set of pages that link to page p
#// L(q) is the number of out-links from page q
#// d is the PageRank damping/teleportation factor; use d = 0.85 as is typical

#foreach page p in P
#  PR(p) = 1/N                          /* initial value */

#while PageRank has not converged do
#  sinkPR = 0
#  foreach page p in S                  /* calculate total sink PR */
#    sinkPR += PR(p)
#  foreach page p in P
#    newPR(p) = (1-d)/N                 /* teleportation */
#    newPR(p) += d*sinkPR/N             /* spread remaining sink PR evenly */
#    foreach page q in M(p)             /* pages pointing to p */
#      newPR(p) += d*PR(q)/L(q)         /* add share of PageRank from in-links */
#  foreach page p
#    PR(p) = newPR(p)

#return PR
