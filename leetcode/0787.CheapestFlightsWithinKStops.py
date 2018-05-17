class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        scr_price_dict = {}
        for flight in flights:
            if flight[0] in scr_price_dict:
                scr_price_dict[flight[0]].append((flight[1], flight[2]))
            else:
                scr_price_dict[flight[0]] = [(flight[1], flight[2])]
        step = 0
        min_price = float('inf')
        pre_cities = [(src, 0)]
        visited_prices ={}
        while step <= K:
            step += 1
            for i in range(len(pre_cities)):
                city, total_price = pre_cities.pop(0)
                if city in visited_prices and visited_prices[city] < total_price:
                    continue
                else:
                    visited_prices[city]=total_price
                for c, price in scr_price_dict.get(city,[]):
                    if c == dst:
                        min_price = min(min_price, price + total_price)
                    else:
                        pre_cities.append((c, price + total_price))
        if min_price == float('inf'):
            return -1
        return min_price