from typing import List
import bisect
from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Ordena os eventos por start time
        events.sort()
        n = len(events)
        starts = [e[0] for e in events]
        
        @lru_cache(maxsize=None)
        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0
            
            # Pula o evento atual
            skip = dp(i + 1, remaining)
            
            # Busca o próximo evento que não se sobrepõe
            next_i = bisect.bisect_right(starts, events[i][1])
            take = events[i][2] + dp(next_i, remaining - 1)
            
            return max(skip, take)
        
        return dp(0, k)
