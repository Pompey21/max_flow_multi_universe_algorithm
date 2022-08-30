# max_flow_multi_universe_algorithm
Here is my implementation of the Max Flow algorithm for the multi- source and sink problems! 
I've implemented the Edmond-Karp algorithm with a slight modification for handling multiple sources and sinks simultaneously, 
while preserving the Time as well as Space complexity to the linear standards!

## What is Max Flow problem?
In optimization theory, maximum flow problems involve finding a feasible flow through a flow network that obtains the maximum possible flow rate. The complication lies in edges having different weights, meaning that we need to find the minimal possible flow considering all paths that flow via that given node as well as how their flow can be distributed amongst other paths.

For more information, here is a good resource: https://en.wikipedia.org/wiki/Maximum_flow_problem

## What is Edmond-Karp algorithm?
Edmond-Karp algorithm is an implementation of the Ford-Fulkerson method for computing the maximum flow in a flow network in a very efficient O(|V||E|^2) time. The difference, or improvement, when compared to the Ford-Fulkerson method is the search order when finding the augmenting path - in Edmond-Karp algorithm it is defiend! The path found must be a shortest path that has available capacity.

## Why should I care?
Network Flow problems are more common than we migh imagine. Its applications are seen throughout and it surely is one of those algorithms that can be re-used numerous times. It seems that in a World with more information flow than ever, we always want to optimise our systems to attend to our needs. However, as it is often the case the hardware components advancements do not always follow with the same pace. Therefore, we need to be more pragmatic when dealing with the information -> this is when we can try to translate the problem into a Max Flow one:)

