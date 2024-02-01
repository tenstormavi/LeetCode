"""
Minimum Health
==============

Alex and Charlie are playing an online video game. Initially, there are m players in the first level, and there are
next n levels. Each level introduces a new player (along with the players from the previous level). Each player has
some strength which determines the difficulty of beating this player. To pass any level, select any available players
and beat them.

Alex has completed the game and beaten the rank the strongest player at every level. Now it's Charlie's
turn to play. Whenever a player is beaten, Charlie's health decreases by the amount of strength of that player. So the
initial health of Charlie must be greater than or equal to the sum of the strengths of players that are beaten
throughout the game. Charlie does not want to lose to Alex, so Charlie decided to also beat the rank the strongest
player at each level. What is the minimum initial health that Charlie needs to start with in order to do this?
"""

import heapq


def getMinimumHealth(initial_player, new_player, rank):
    health_needed = 0
    # Max Heap
    heap = []
    heapq.heapify(heap)

    for initial_p in initial_player:
        heapq.heappush(heap, -1 * initial_p)
    # health needed at the first level
    rank_largest = heapq.nsmallest(rank, heap)
    health_needed += rank_largest[-1]

    for new_p in new_player:
        heapq.heappush(heap, -1 * new_p)
        # health needed with each new player introduced
        rank_largest = heapq.nsmallest(rank, heap)
        health_needed += rank_largest[-1]

    return -1 * health_needed

print(getMinimumHealth([1,2], [3,4], 2))
print(getMinimumHealth([1,1,3], [2,2,4], 2))
print(getMinimumHealth([1,2,3], [6,5,4], 1))
