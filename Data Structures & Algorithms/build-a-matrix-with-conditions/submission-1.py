class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(node, adj, visit, path, order):
            if node in path:
                return False
            
            if node in visit:
                return True

            visit.add(node)
            path.add(node)

            for nei in adj[node]:
                if not dfs(nei, adj, visit, path, order):
                    return False

            order.append(node)
            path.remove(node)

            return True
        
        def topo_sort(edges):
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)

            visit, path = set(), set()
            order = []

            for src in range(1, k+1):
                if not dfs(src, adj, visit, path, order):
                    return []

            return order[::-1] #reverse


        row_order = topo_sort(rowConditions)
        if not row_order: return []

        col_order = topo_sort(colConditions)
        if not col_order: return []
    
        val_to_row = {num: i for i, num in enumerate(row_order)}
        val_to_col = {num: i for i, num in enumerate(col_order)}

        res = [[0]*k for _ in range(k)]
        for num in range(1, k+1):
            r, c = val_to_row[num], val_to_col[num]
            res[r][c] = num

        return res