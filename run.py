# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

oe = search.GPSProblem('O', 'E'
                       , search.romania)

uo = search.GPSProblem('U', 'O'
                       , search.romania)

es = search.GPSProblem('E', 'S'
                       , search.romania)

er = search.GPSProblem('E', 'R'
                       , search.romania)


print("#######FROM A TO B#######")
print("######Breadth Search#######")
print(search.breadth_first_graph_search(ab).path())
print("######Depth Search#######")
print(search.depth_first_graph_search(ab).path())
print("######Branch and Bound#######")
print(search.RAMACOT_search(ab).path())
print("######Branch and Bound with hint#######")
print(search.RAMACOTHINT_search(ab).path())
print("###################################")
print("#######FROM O TO E#######")
print("######Branch and Bound#######")
print(search.RAMACOT_search(oe).path())
print("######Branch and Bound with hint#######")
print(search.RAMACOTHINT_search(oe).path())
print("###################################")
print("#######FROM U TO O#######")
print("######Branch and Bound#######")
print(search.RAMACOT_search(uo).path())
print("######Branch and Bound with hint#######")
print(search.RAMACOTHINT_search(uo).path())
print("###################################")
print("#######FROM E TO S#######")
print("######Branch and Bound#######")
print(search.RAMACOT_search(es).path())
print("######Branch and Bound with hint#######")
print(search.RAMACOTHINT_search(es).path())
print("###################################")
print("#######FROM E TO R#######")
print("######Branch and Bound#######")
print(search.RAMACOT_search(er).path())
print("######Branch and Bound with hint#######")
print(search.RAMACOTHINT_search(er).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
