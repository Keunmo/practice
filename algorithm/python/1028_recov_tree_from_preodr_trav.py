# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if len(S)==0:
            return None
        lvlist=[]   # (lv,node) 형식의 튜플.
        lv = 1
        S=S.split('-')
        node = TreeNode(S[0])
        lvlist.append((0,node)) 
        # lvlist 의 첫번째 요소를 반복문 밖에서 수동으로 추가하는 이유: 
        # lv를 공백 합으로 계산하는데 S.split 하면 첫번째 lv0이랑 두번째 lv1의 공백이 둘 다 0이라서.
        # 그래서 for문 안에서 두번째 요소부터 돌고 lv는 1부터 시작함.
        for i in S[1:]:
            if i.isdigit():
                node = TreeNode(i)
                lvlist.append((lv,node))
                lv=1
            if not i.isdigit():
                lv+=1
        stk=[]
        stk.append(lvlist[0])
        # 스택 첫번째 요소 밖에서 추가하는 이유는 for 안에서 스택의 top과 비교하는 작업을 해주기 때문.
        for i in lvlist[1:]:
            if stk[-1][0] + 1 == i[0]:      #stk top lv+1 == i lv
                stk[-1][1].left = i[1]      #stk top node.left = i node. 처음 만나는 자식노드니까 무조건 left.
                stk.append(i)
            else:
                while not stk[-1][0] + 1 == i[0]:   #stk top lv+1 이 i lv가 될때까지 pop. ==부모노드 나올때까지 pop.
                    stk.pop()
                stk[-1][1].right = i[1]     #stk top node.right = i node. else로 넘어와서 부모에 걸렸다는건 left가 무조건 차있다는 거니까 right.
                stk.append(i)
        return lvlist[0][1]                 #root node 반환.

            
            
            
            