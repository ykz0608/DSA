{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# HW3 BINARY TREE\n",
    "## 學習歷程：\n",
    "\n",
    "### 二元搜索樹(Binary Search Tree)是基於二元樹的一種延伸，二元搜索樹的應用範圍很廣，可以利用在搜索、排序和提供資料集合基本結構，發展其他資料結構，所以也是重要的資料結構之一。\n",
    "\n",
    "### 定義\n",
    "\n",
    "定義除了繼承二元樹的定義外，二元搜索樹本身也有額外的定義，但可能會看到幾種不同的說法，而較多數人使用的定義如下：\n",
    "\n",
    "* 左子樹不為空，則左子樹的所有節點的鍵值(Key)小於根節點的鍵值。\n",
    "* 右子樹不為空，則右子樹的所有節點的鍵值(Key)大於根節點的鍵值。\n",
    "* 左右子樹也都是二元搜索樹。\n",
    "* 節點不會有重複的鍵值。\n",
    "這個定義是樹中的節點都具有Key-value pair情況，有時候可能會其他變化：\n",
    "    * 沒有鍵值，而用值(Value)來比較。\n",
    "    * 允許重複的資料，此時會出現等於的情況，則將定義1.改成小於等於或者定義2.改成大於等於。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 作業格式"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definition for a binary tree node.\n",
    "class TreeNode(object):\n",
    "    def __init__(self,x):\n",
    "        self.val = x\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "        \"\"\"\n",
    "        :type val: int\n",
    "        :type left: TreeNode or None\n",
    "        :type right: TreeNode or None\n",
    "        \"\"\"\n",
    "class Solution(object):\n",
    "    def insert(self, root, val):\n",
    "        \"\"\"\n",
    "        :type root: TreeNode\n",
    "        :type val: int\n",
    "        :rtype: TreeNode(inserted node)\n",
    "        \"\"\"\n",
    "    def delete(self, root, target):\n",
    "        \"\"\"\n",
    "        :type root: TreeNode\n",
    "        :type target: int\n",
    "        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())\n",
    "        \"\"\"\n",
    "    def search(self, root, target):\n",
    "        \"\"\"\n",
    "        :type root: TreeNode\n",
    "        :type target: int\n",
    "        :rtype: TreeNode(searched node)\n",
    "        \"\"\"\n",
    "    def modify(self, root, target, new_val):\n",
    "        \"\"\"\n",
    "        :type root: TreeNode\n",
    "        :type target: int\n",
    "        :type new_val: int\n",
    "        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())\n",
    "        \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "自己尝试寫一次:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "class TreeNode(object):\n",
    "    def __init__(self, x):\n",
    "        self.val = x\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "class Solution(object):\n",
    "    def insert(self, root, val):\n",
    "        if root == None:\n",
    "            root = TreeNode(val)\n",
    "        elif val < root.val:\n",
    "            root.left = self.insert(root.left, val)\n",
    "        elif val > root.val:\n",
    "            root.right = self.insert(root.right, val)\n",
    "        return root\n",
    "    \n",
    "    def printTree(self, root):\n",
    "        # 打印二叉搜索树\n",
    "        if root == None:\n",
    "            return \n",
    "        self.printTree(root.left)\n",
    "        print(root.val, end = ' ')\n",
    "        self.printTree(root.right)\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-5 3 5 6 7 8 10 True False <__main__.TreeNode object at 0x000001FAD4D23148>\n"
     ]
    }
   ],
   "source": [
    "bst = Solution()\n",
    "root = TreeNode(5)\n",
    "bstest1 = bst.insert(root, 3)\n",
    "bstest2 = bst.insert(root, 3)\n",
    "bstest3 = bst.insert(root, -5)\n",
    "bstest4 = bst.insert(root, 8)\n",
    "bstest5 = bst.insert(root, 7)\n",
    "bstest6 = bst.insert(root, 6)\n",
    "bstest7 = bst.insert(root, 10)\n",
    "\n",
    "bst.printTree(root)\n",
    "print(Solution().insert(root,5)==root,end = ' ')\n",
    "print(Solution().insert(root,3)==root.left,end = ' ')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "雖然成功但發現少一個重複的值“3”\n",
    "少寫重複的值要怎麽處理"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "class TreeNode(object):\n",
    "    def __init__(self, x):\n",
    "        self.val = x\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "class Solution(object):\n",
    "    def insert(self, root, val):\n",
    "        if root == None:\n",
    "            root = TreeNode(val)\n",
    "        elif val <= root.val:\n",
    "            root.left = self.insert(root.left, val)\n",
    "        elif val > root.val:\n",
    "            root.right = self.insert(root.right, val)\n",
    "        return root\n",
    "    \n",
    "    def printTree(self, root):\n",
    "        # 打印二叉搜索树\n",
    "        if root == None:\n",
    "            return \n",
    "        self.printTree(root.left)\n",
    "        print(root.val, end = ' ')\n",
    "        self.printTree(root.right)\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "bst = Solution()\n",
    "root = TreeNode(5)\n",
    "bstest1 = bst.insert(root, 3)\n",
    "bstest1 = bst.insert(root, 3)\n",
    "bstest1 = bst.insert(root, -5)\n",
    "bstest1 = bst.insert(root, 8)\n",
    "bstest1 = bst.insert(root, 7)\n",
    "bstest1 = bst.insert(root, 6)\n",
    "bstest1 = bst.insert(root, 10)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "a=Solution().preorder(bstest1)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, [-5, 3, 3], [8, 7, 6, 10]]\n",
      "True\n",
      "False\n",
      "False\n",
      "-----------------\n",
      "True\n",
      "False\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "class TreeNode(object):\n",
    "    def __init__(self, x):\n",
    "        self.val = x\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "class Solution(object):\n",
    "    def insert(self, root, val):\n",
    "        if root == None:\n",
    "            root = TreeNode(val)\n",
    "        elif val <= root.val:\n",
    "            root.left = self.insert(root.left, val)\n",
    "        elif val > root.val:\n",
    "            root.right = self.insert(root.right, val)\n",
    "        return root\n",
    "    \n",
    "   \n",
    "    def preorder(self,root):\n",
    "        if root is None:return []\n",
    "        result=[root.val]\n",
    "        resultl=self.preorder(root.left)\n",
    "        resultr=self.preorder(root.right)\n",
    "        return result+resultl+resultr\n",
    "    \n",
    "    def preorder2(self,root):\n",
    "        if root is None:return []\n",
    "        result=[]\n",
    "        result.append(root.val)\n",
    "        result.append(self.preorder(root.left))\n",
    "        result.append(self.preorder(root.right))\n",
    "        return result\n",
    "    \n",
    "    def preorder1(self,root,arr):\n",
    "        if not root:return []\n",
    "        arr.append(root.val)\n",
    "        self.preorder1(root.left)        \n",
    "        self.preorder1(root.right)\n",
    "\n",
    "    \n",
    "    def search(self, root, target):\n",
    "        if root == None:\n",
    "            return False\n",
    "        if root.val == target:\n",
    "            return root\n",
    "        elif target <= root.val:\n",
    "            return self.search(root.left,target)\n",
    "        elif target > root.val:\n",
    "            return self.search(root.right,target)\n",
    "    \n",
    "\n",
    "bst = Solution()\n",
    "root = TreeNode(5)\n",
    "bstest1 = bst.insert(root, -5)\n",
    "bstest1 = bst.insert(root, 3)\n",
    "bstest1 = bst.insert(root, 3)\n",
    "bstest1 = bst.insert(root, 8)\n",
    "bstest1 = bst.insert(root, 7)\n",
    "bstest1 = bst.insert(root, 10)\n",
    "bstest1 = bst.insert(root, 6)\n",
    "\n",
    "\n",
    "\n",
    "a=Solution().preorder2(bstest1)\n",
    "print(a)\n",
    "print(Solution().insert(root,5)==root)\n",
    "print(Solution().insert(root,7)==root.right.left.left)\n",
    "print(Solution().insert(root,-5)==root.left)\n",
    "print(\"-----------------\")\n",
    "print(Solution().search(root,3)==root.left.right)\n",
    "print(Solution().search(root,3)==root.left.right.left)\n",
    "print(Solution().search(root,5)==root)\n",
    "print(Solution().search(root,8)==root.right)\n",
    "print(Solution().search(root,-5)==root.left)\n",
    "print(Solution().search(root,7)==root.right.left)\n",
    "print(Solution().search(root,10)==root.right.right)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "root error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-5 3 3 5 6 7 8 8 10 11 57 True True "
     ]
    }
   ],
   "source": [
    "bst = Solution()\n",
    "root = TreeNode(5)\n",
    "bstest1 = bst.insert(root, 3)\n",
    "bstest2 = bst.insert(root, 3)\n",
    "bstest3 = bst.insert(root, -5)\n",
    "bstest4 = bst.insert(root, 8)\n",
    "bstest5 = bst.insert(root, 7)\n",
    "bstest6 = bst.insert(root, 6)\n",
    "bstest7 = bst.insert(root, 10)\n",
    "bstest8 = bst.insert(root, 8)\n",
    "bstest9 = bst.insert(root, 11)\n",
    "bstest10 = bst.insert(root, 57)\n",
    "\n",
    "\n",
    "bst.printTree(root)\n",
    "print(Solution().insert(root,5)==root,end = ' ')\n",
    "print(Solution().insert(root,8)==root,end = ' ')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 參考資料\n",
    "\n",
    "### 參考網站:\n",
    ">* https://emn178.pixnet.net/blog/post/94574434\n",
    ">* "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'bstree'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-20-4bd655a10d82>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mpybst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdraw\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mplot_tree\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pybst\\draw.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     19\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnetworkx\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnx\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 21\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mbstree\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mbst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     22\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0m_get_pos_list\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtree\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'bstree'"
     ]
    }
   ],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
