# Solving the monty hall problem using a bayesian network approach
This is a little experiment/practice on using bayesian networks to infer the probability of unknown variables using python and pomegranate. In this example we can infer certain statistical probabilities given observed events. The material here was largely derived from the following material:

[Video covering the code](https://www.youtube.com/watch?v=SkC8S3wuIfg)  
[Blogpost](https://www.edureka.co/blog/bayesian-networks/)  
[Post about solving the monty hall problem using bayes rule](https://towardsdatascience.com/solving-the-monty-hall-problem-with-bayes-theorem-893289953e16)  
[Pomegranate documentation on bayesian networks](https://pomegranate.readthedocs.io/en/latest/BayesianNetwork.html)  

## What is a Bayesian Network?
A Bayesian Network is a type of **Probabilistic Graphical Modelling** (or **PGM** for short) technique that's used to compute uncertainties by using the concept of probability.

A **graphical model** or **probabilistic graphical model** is a probabilistic model for which a graph expresses the conditional dependence structure between random variables. You can think of the edges between the nodes as _conditional probabilities_.

Bayesian networks are based around the main concept of probability. They use this concept to model uncertainties by using a graph-like structure. For this we use a special graph structure called a **Directed Acyclic Graph**.

A Directed Acyclic Graph, or DAG for short, is a directed graph that _does not_ contain any cycles. In such a graph a node can be dependent on other nodes, depending on the direction of it's connected edges it can either be a parent or a child of another node.

In the context of a bayesian network, the edges represent relations between the nodes. In particular, these are conditional probabilities. The nodes themselves represent random variables.

The output of such a graph will be the _(un)certainty of a certain event occuring, based on the conditional probability distributions of each random variable_. This distribution is represented by a conditional probability table.

these random variables are like booleans, either they "occur" or not. The probability that they occur however is _not_ boolean, but rather expressed as a value between 0.0 and 1.0.

Some random variables will be **independent**, and thus not have a conditional probability. Other variables are **dependent** on one or multiple other variables, and thus have a **conditional probability**. In the graph structure these 2 types of variables are represented as child or parent nodes.