class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        # k+1 because k counts the airports you stop at in between, not the number of flights you take
        for i in range(k+1): 
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
                
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]