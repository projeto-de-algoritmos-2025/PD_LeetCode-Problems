from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Junta os jobs em uma lista de tuplas e ordena por endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        
        # DP[i] = lucro máximo considerando os primeiros i jobs
        dp = [0] * (n + 1)
        ends = [job[1] for job in jobs]  # Para busca binária
        
        for i in range(1, n + 1):
            start, end, prof = jobs[i - 1]
            
            # Encontra o último job que termina antes do atual começar
            index = bisect.bisect_right(ends, start, 0, i - 1)
            
            # dp[i] = max(não escolher esse job, escolher esse + dp do último compatível)
            dp[i] = max(dp[i - 1], dp[index] + prof)
        
        return dp[n]
