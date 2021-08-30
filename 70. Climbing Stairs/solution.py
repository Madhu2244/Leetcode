class Solution(object):
    def climbStairs(self, n):
        self.cnt = 0
        cache = {}
        def simulation(current_step):
            if current_step in cache:
                return cache[current_step]
            if current_step == n:
                return 1
            if current_step > n:
                return 0
            cache[current_step] = simulation(current_step + 1) + simulation(current_step + 2)
            return simulation(current_step + 1) + simulation(current_step + 2)
        
        return simulation(0)
        #print(cache)    
        
        
    
