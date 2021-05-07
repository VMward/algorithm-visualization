class Tree:
    class Solution:
        def deleteTreeNodes(self, nodes: int, parent: list[int], value: list[int]) -> int:
            '''
            invert the tree to normal

            dfs(i) = trunkedSubtreeSum, trunkedSubTreeSize
            '''

            def dfs(i):
                if i not in child:
                    return value[i], 1 if value[i] != 0 else 0

                tot = value[i]
                size = 1
                for j in child[i]:
                    s, n = dfs(j)
                    if s != 0:
                        tot += s
                        size += n
                return tot, size if tot != 0 else 0

            child = dict(list)
            for i, p in enumerate(parent):
                child[p].append(i)

            _, count = dfs(0)
            return count