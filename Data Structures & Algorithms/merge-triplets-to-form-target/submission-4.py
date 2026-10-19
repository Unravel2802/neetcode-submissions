class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False] * 3

        for i in range(len(triplets)):
            triplet = triplets[i]

            if any(triplet[j] > target[j] for j in range(3)):
                continue
            
            for j in range(3):
                if triplet[j] == target[j]:
                    found[j] = True
        
        return all(found)