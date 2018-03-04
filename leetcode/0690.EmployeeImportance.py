"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    dic = {}

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        for e in employees:
            self.dic[e.id] = e
        return self.dfs(id)

    def dfs(self, id):
        e = self.dic.get(id)
        total = e.importance
        for cid in e.subordinates:
            total += self.dfs(cid)
        return total