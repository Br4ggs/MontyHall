import math
from pomegranate import *

# first we define the probabilty distributions for both the guest, the prize, and monty
guest = DiscreteDistribution( { 'A': 1./3, 'B': 1./3, 'C': 1./3 } )
prize = DiscreteDistribution( { 'A': 1./3, 'B': 1./3, 'C': 1./3 } )

# monty's values are conditional, and are distributed in a conditional probability table
#
# the first value represents the guest choice, the second value the prize choice, and finally 
# the third value represents monty's choice, followed by the probability of that scenario happening.
#
# these probabilities are actually fairly easy to explain, as they're based on some
# simple behavioural restrictions for monty:
# -monty cannot open a door the guest has already opened (makes sense)
# -monty can also not open a door where the prize is behind (also makes sense)
#
# this is the reason why in certain scenarios, e.g.:
# the guest picks door A and the prize is behind door C, monty will have to pick door B.
# Thus the scenario A, C, B has a probability of 1.0, whereas A, C, A and A, C, C both have
# a probability of 0.0

monty = ConditionalProbabilityTable(
    [[ 'A', 'A', 'A', 0.0 ],
    [ 'A', 'A', 'B', 0.5 ],
    [ 'A', 'A', 'C', 0.5 ],
    [ 'A', 'B', 'A', 0.0 ],
    [ 'A', 'B', 'B', 0.0 ],
    [ 'A', 'B', 'C', 1.0 ],
    [ 'A', 'C', 'A', 0.0 ],
    [ 'A', 'C', 'B', 1.0 ],
    [ 'A', 'C', 'C', 0.0 ],
    [ 'B', 'A', 'A', 0.0 ],
    [ 'B', 'A', 'B', 0.0 ],
    [ 'B', 'A', 'C', 1.0 ],
    [ 'B', 'B', 'A', 0.5 ],
    [ 'B', 'B', 'B', 0.0 ],
    [ 'B', 'B', 'C', 0.5 ],
    [ 'B', 'C', 'A', 1.0 ],
    [ 'B', 'C', 'B', 0.0 ],
    [ 'B', 'C', 'C', 0.0 ],
    [ 'C', 'A', 'A', 0.0 ],
    [ 'C', 'A', 'B', 1.0 ],
    [ 'C', 'A', 'C', 0.0 ],
    [ 'C', 'B', 'A', 1.0 ],
    [ 'C', 'B', 'B', 0.0 ],
    [ 'C', 'B', 'C', 0.0 ],
    [ 'C', 'C', 'A', 0.5 ],
    [ 'C', 'C', 'B', 0.5 ],
    [ 'C', 'C', 'C', 0.0 ]],
    [guest, prize])

# then we turn these into nodes using Pomegranate
s1 = Node(guest, name="guest")
s2 = Node(prize, name="prize")
s3 = Node(monty, name="monty")

# and create a bayesian network with these nodes
model = BayesianNetwork("Monty Hall Problem")
model.add_states(s1, s2, s3)
model.add_edge(s1, s3)
model.add_edge(s2, s3)
model.bake()

# finally we want to predict the probabilities of behind which door the prize is
# for this we have the observations that guest pick door A, and monty opens door B
beliefs = model.predict_proba({ 'guest': 'A', 'monty': 'B' })
beliefs = map(str, beliefs)

# and then we print the result :)
print("".join("{}\n{}\n".format( state.name, belief ) for state, belief in zip(model.states, beliefs )))