class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if newInterval is None:
            return intervals
        
        result = []
        
        for start, end in intervals:
            # If newInterval already inserted, just add remaining intervals
            if newInterval is None:
                result.append([start, end])
            
            # Case 1: newInterval ends before current interval starts
            elif newInterval[1] < start:
                result.append(newInterval)
                result.append([start, end])
                newInterval = None  # Mark as inserted
            
            # Case 2: Current interval ends before newInterval starts
            elif end < newInterval[0]:
                result.append([start, end])
            
            # Case 3: Overlap → merge
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        # Add newInterval if not yet inserted
        if newInterval:
            result.append(newInterval)
        
        return result