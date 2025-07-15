# Last updated: 7/15/2025, 4:46:41 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count,i,j = 0,0,0
        p = len(players)
        t = len(trainers)
        while i < p and j< t:
            
            if players[i]<= trainers[j]:
                count += 1
                i+=1
                j+=1
            else:
                j+=1
                
        return count
        