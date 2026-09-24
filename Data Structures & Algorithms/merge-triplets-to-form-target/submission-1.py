class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)

        found_x = found_y = found_z = False
        target_x, target_y, target_z = target


        for x, y , z in triplets:
            if x > target_x or y > target_y or z > target_z:
                continue
            
            if x == target_x:
                found_x = True
            if y == target_y:
                found_y = True
            if z == target_z:
                found_z = True    
        return found_x and found_y and found_z