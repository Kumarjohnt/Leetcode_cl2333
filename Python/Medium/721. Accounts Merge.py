class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        d = {} #email:index
        parent = list(range(len(accounts)))
        
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in d:
                    d[email] = i
                else:
                    x, y = find(i), find(d[email])
                    parent[x] = y
        
        tmp = collections.defaultdict(set) #index:email
        for i in range(len(accounts)):
            tmp[find(i)] = tmp[find(i)].union(set(accounts[i][1:])) 
        
        result = []
        for key, value in tmp.items():
            result.append([accounts[key][0]] +sorted(list(value)))
            
        return result
        
       