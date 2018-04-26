{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0\n",
      "0.0\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\"\\nSets=OrderSets()\\nSum=0\\nfor i in range(len(X0)):\\n\\tif X0[i] < 0.00001:\\n\\t\\tZ=0\\n#\\t        print(i+1,Sets[i],0)\\n\\telse:\\n\\t\\tprob=float(format(X0.item(i),'.5f'))\\n                print prob \\n                Sum=Sum+prob\\n#               print Sum\\n#\\t\\tprint(i+1,Sets[i],prob)\\nprint Sum\\nF=np.zeros((32,32))#,np.dtype('float64'))\\n#print \\nList=[i for i in range(16,32)]\\nList1=[i for i in range(48,64)]\\nList=List+List1\\nprint len(List)\\nfor i in range(len(List)):\\n    for j in range(len(List)):\\n        F[i,j]=C[List[i],List[j]]*X0[List[j]]-C[List[j],List[i]]*X0[List[i]]\\n        \\n\\n\\n#print F\\nprintZeroIndex(F,32)\\n#print Sum\\n#print max(y)\\n#X=C*X0\\n#print distance(X0,Xvi )\\n#print X\\n#print max(y)\\n#print X\\n#print B*X\\n#print max(y)\\n\\n#print B\\n#print A\\n\""
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import math \n",
    "import random\n",
    "from numpy import linalg \n",
    "from numpy import real\n",
    "from scipy import linalg, matrix\n",
    "from sympy import Matrix\n",
    "A={0:(0,1), 1:(2,3), 2:(0,2), 3:(0,3), 4:(1,2), 5:(1,3)}\n",
    "\n",
    "kex=3\n",
    "kin=0.5\n",
    "\n",
    "\n",
    "def distance(X1,X2):\n",
    "\tSum=0.0\n",
    "\tfor i in range(len(X1)):\n",
    "\t\tSum=Sum+(X1[i]-X2[i])*(X1[i]-X2[i])\n",
    "\treturn math.sqrt(Sum/len(X1))\n",
    "\n",
    "### Sorting things ### \n",
    "def getKey(item):\n",
    "    return item[0]\n",
    "\n",
    "\n",
    "### Generating all sets of states, 00, 01, 10, 11  ### \n",
    "def OrderSets():\n",
    "#\tList=[0]*6\n",
    "\tAllset=[]\n",
    "\tList=[]\n",
    "#\tAllset.append(List)\n",
    "#\tprint Allset\n",
    "\tNewSet=[]\n",
    "\tSet(Allset,List,0)\n",
    "\tfor i in range(len(Allset)):\n",
    "#\t\tprint list(reversed(Allset[i]))\n",
    "\t\tNewSet.append(Allset[i])\n",
    "#\t\tprint Allset[i]\n",
    "#\t\tNewSet.append(list(reversed(Allset[i])))\n",
    "#\tprint list(reversed(NewSet))\n",
    "\treturn NewSet\n",
    "#\treturn NewSet\n",
    "\n",
    "\n",
    "\n",
    "## Generating all sets of states 00, 10, 01, 11 ##\n",
    "def AllSets():\n",
    "#\tList=[0]*6\n",
    "\tAllset=[]\n",
    "\tList=[]\n",
    "#\tAllset.append(List)\n",
    "#\tprint Allset\n",
    "\tNewSet=[]\n",
    "\tSet(Allset,List,0)\n",
    "\tfor i in range(len(Allset)):\n",
    "#\t\tprint list(reversed(Allset[i]))\n",
    "#\t\tprint Allset[i]\n",
    "\t\tNewSet.append(list(reversed(Allset[i])))\n",
    "#\tprint list(reversed(NewSet))\n",
    "\treturn NewSet\n",
    "\n",
    "def Set(Allset,List,index):\n",
    "#\tprint index\n",
    "\tif len(List)==6:\n",
    "\t\tAllset.append(List)\n",
    "\telse:\n",
    "\t\tfor i in range(2):\n",
    "\t\t\tSet(Allset,List+[i],index+1)\n",
    "## Indexing the states ## \n",
    "\n",
    "## Indexing the states ## \n",
    "def state(N1):\n",
    "\tN=list(reversed(N1))\n",
    "\tL=2**N[0]\n",
    "\tfor i in range(1,len(N)):\n",
    "\t\tL=L+N[i]*(2**((i)*N[i]))\n",
    "\treturn L-1\n",
    "\n",
    "\n",
    "\n",
    "## Measuring transition probability ##\n",
    "def stay(N1,k):\n",
    "\tL1=state(N1)\n",
    "\tprob=0\n",
    "\tif k[0]==kin:\n",
    "\t\tprob=prob+1\n",
    "\tif k[1]==kin:\n",
    "\t\tprob=prob+1\n",
    "\tif k[2]==kex:\n",
    "\t\tprob=prob+1\n",
    "\tif k[3]==kex:\n",
    "\t\tprob=prob+1\n",
    "\tprob=float(format(prob,'.5f'))\n",
    "\tif prob==0:\n",
    "\t\tprob=0\n",
    "\treturn (L1,prob)\n",
    "\n",
    "def Tran(N1,N2,k):\n",
    "\tprob=0\n",
    "\tL1=state(N1)\n",
    "\tL2=state(N2)\n",
    "\n",
    "\tindex=[]\n",
    "\tfor i in range(len(N1)):\n",
    "\t\tif N1[i]!=N2[i]:\n",
    "                        prob=0\n",
    "#\t\t\tindex.append(i)\n",
    "\t\t\tif N1[i]==0:\n",
    "#\t\t\t\tprint i\n",
    "\t\t\t\tif i in range(2,6):\n",
    "\t\t\t\t\t(x,y)=A[i]\n",
    "\t\t\t\t\tprob=1.0/(3-k[y])\n",
    "                                        if k[x]==0:\n",
    "                                            prob=prob+1.0/(3-k[x])\n",
    "\n",
    "\t\t\t\tif i==0:\n",
    "                                        prob=0\n",
    "\t\t\t\t\t(x,y)=A[i]\n",
    "                                        if k[x]==0:\n",
    "                                            prob=prob+1.0/(3-k[x])\n",
    "                                        if k[y]==0:\n",
    "\t\t\t\t\t    prob=prob+1.0/(3-k[y])\n",
    "\t\t\t\tif i==1:\n",
    "\t\t\t\t\t(x,y)=A[i]\t\n",
    "#\t\t\t\t\tprint A[i]\t\t\t\t\n",
    "\t\t\t\t\tprob=1.0/(3-k[y])+1.0/(3-k[x])\n",
    "#\t\t\t\t\tprint prob\n",
    "\n",
    "\t\t\telse:\n",
    "\t\t\t\tif i in range(2,6):\n",
    "\t\t\t\t\t(x,y)=A[i]\n",
    "                                        if k[x]!=0:\n",
    "\t\t\t\t\t    prob=1.0/(k[x])\n",
    "\n",
    "\t\t\t\tif i==0:\n",
    "\t\t\t\t\t(x,y)=A[i]\n",
    "#\t\t\t\t\tprint(x,y)\n",
    "#\t\t\t\t\tprint(k[x],k[y])\t\t\t\t\t\n",
    "\t\t\t\t\tprob=1.0/(k[y])+1.0/(k[x])\n",
    "\n",
    "\t\t\t\tif i==1:\n",
    "\t\t\t\t\tprob=0\n",
    "\tprob=float(format(prob,'.2f'))\n",
    "\tif prob==0:\n",
    "\t\tprob=0\n",
    "\treturn (L2,prob)\n",
    "\n",
    "\n",
    "\n",
    "## Measuring the row related state N1 in W matrix ## \n",
    "def Nb(N1, W):\n",
    "\tL1=state(N1)\n",
    "\tNeig=[]\n",
    "\tk=[0]*4\n",
    "#\tNeig.append(N1)\n",
    "\tfor i in range(len(N1)):\n",
    "\t\tNeig.append(N1[:i]+[1-N1[i]]+N1[i+1:])\n",
    "\n",
    "\tk[0]=N1[0]+N1[2]+N1[3]\n",
    "\tk[1]=N1[0]+N1[4]+N1[5]\n",
    "\tk[2]=N1[2]+N1[4]+N1[1]\t\n",
    "\tk[3]=N1[3]+N1[5]+N1[1]\t\n",
    "\n",
    "\tGrand=[]\n",
    "\tGrand.append(stay(N1,k))\n",
    "\tfor i in Neig:\n",
    "\t\tZ=Tran(N1,i,k)\n",
    "\t\tGrand.append(Z)\n",
    "\tGrand1=sorted(Grand,key=getKey)\t\n",
    "\ts=''\n",
    "\tfor i in range(len(Grand1)-1):\n",
    "\t\t(x,y)=Grand1[i]\n",
    "\t\tW[L1][x]=y\n",
    "\t\ts=s+'('+str(L1)+','+str(x)+') = '+str(y)+'&'\n",
    "\t(x,y)=Grand1[len(Grand1)-1]\n",
    "\tW[L1][x]=y\t\n",
    "\ts=s+'('+str(L1)+','+str(x)+') = '+str(y)+\" \\\\\"\t\n",
    "\ts=s+\"\\\\\"\n",
    "#\tprint s\n",
    "\n",
    "\ts1=\"Transition from state \" +str(L1)+\", \"+\"$\"+str(N1)+\"$:\"\n",
    "#\tprint s1\n",
    "\n",
    "\ts2=\"\\\\begin{equation} \\\\nonumber \\n\"+\"W(\"+str(L1)+\",:)=c\\n\"+\"\\\\begin{pmatrix}\\n\"\n",
    "\ts3=s+\"\\n\"+\"\\end{pmatrix} \\n\"+\"\\end{equation} \\n\"\n",
    "\n",
    "\tS=s1+\"\\n\"+s2+s3\n",
    "\n",
    "## returning W matrix ## \n",
    "\n",
    "def WMatrix():\n",
    "\tW=np.zeros((64, 64))\n",
    "\tNew=OrderSets()\n",
    "\tfor i in New:\n",
    "\t\tNb(i, W)\n",
    "\treturn W \n",
    "\n",
    "\n",
    "## Printing W Matrix in Latex Format ## \n",
    "\n",
    "def printZeroIndex(W, size):\n",
    "\ts=''\n",
    "\tfor i in range(0,size):\n",
    "\t\tfor j in range(0,size):\n",
    "                        W[i,j]=float(format(W[i,j],'.5f'))\n",
    "                        \n",
    "#\t\t\tprint W[i,j]\n",
    "\t\t\tif W[i,j]==1.0:\n",
    "#\t\t\t\tprint W[i][j]\n",
    "\t\t\t\twxy=\"1\"\t\t\t\t\t\t\n",
    "\t\t\telif W[i,j]==0.0:\n",
    "\t\t\t\twxy=\"0\"\t\t\t\n",
    "\t\t\telif W[i,j]==0.33:\n",
    "\t\t\t\twxy=\"\\\\frac{1}{3}\"\n",
    "\t\t\telif W[i,j]==1.5:\n",
    "\t\t\t\twxy=\"\\\\frac{3}{2}\"\n",
    "\t\t\telif W[i,j]==2.0:\n",
    "\t\t\t\twxy=\"2\"\n",
    "\t\t\telif W[i,j]==0.83:\n",
    "\t\t\t\twxy=\"\\\\frac{5}{6}\"\t\t\t\t\n",
    "\t\t\telif W[i,j]==0.67:\n",
    "\t\t\t\twxy=\"\\\\frac{2}{3}\"\n",
    "\t\t\telif W[i,j]==1.33:\n",
    "\t\t\t\twxy=\"\\\\frac{4}{3}\"\n",
    "\t\t\telif W[i,j]==0.5:\n",
    "\t\t\t\twxy=\"\\\\frac{1}{2}\"\n",
    "\t\t\telse:\n",
    "\t\t\t\twxy=str(W[i,j])\n",
    "\t\t\tif j!=size-1:\n",
    "\t\t\t\ts=s+wxy+\"&\"\t\t\t\t\t\t\t\t\n",
    "\t\t\telse:\n",
    "\t\t\t\ts=s+wxy+\" \\\\\"+\"\\\\\"+\"\\n\"\n",
    "\tprint s\n",
    "\n",
    "\n",
    "'''\n",
    "\t\t\tif W[i][j]==0.0:\n",
    "\t\t\t\twxy=\"0\"\t\t\t\n",
    "\t\t\telif W[i][j]==0.33:\n",
    "\t\t\t\twxy=\" \\\\frac{1}{3} \"\n",
    "\t\t\telif W[i][j]==1.33:\n",
    "\t\t\t\twxy=\" \\\\frac{4}{3} \"\n",
    "\t\t\telif W[i][j]==0.5:\n",
    "\t\t\t\twxy=\" \\\\frac{1}{2} \"\n",
    "\t\t\telse:\n",
    "'''\t\t\t\t\n",
    "\n",
    "\n",
    "#print OrderSets()\n",
    "\n",
    "#print AllSets()\n",
    "W= WMatrix()\n",
    "\n",
    "print W[16,19]\n",
    "print W[19,16]\n",
    "#AllSets()\n",
    "#print W\n",
    "B=np.matrix(W)\n",
    "A=B.T\n",
    "#print A[16,16]\n",
    "#printZeroIndex(A[16:32,16:32],16)\n",
    "#for i in range(16,32):\n",
    "#\tfor j in range(16,32):\n",
    "#\t\tprint(i-15,j-15,A[i,j])\n",
    "#\tprint \"####\"\n",
    "\n",
    "C=A\n",
    "#A = np.matrix([[0.25,0.25,0.5] , [0.1,0.8,0.1] , [0.6,0.3,0.1]])\n",
    "#B = np.matrix([[0.25,0.25,0.5] , [0.1,0.8,0.1] , [0.6,0.3,0.1]])\n",
    "#print B\n",
    "X0 = np.random.random((64,1))\n",
    "#X0=np.matrix(X0)\n",
    "iterations = 20000\n",
    "#print X0\n",
    "for i in range (iterations):\n",
    "\ty = A*X0\n",
    "#\tprint y\n",
    "#\tprint max(y)\n",
    "\tX1=y/max(y)\n",
    "\tA = A*A\t\t\n",
    "\tif distance(X1,X0) < 10**-8:\n",
    "#\t\tprint i\n",
    "\t\tbreak\n",
    "\tX0=X1\t\n",
    "\n",
    "#print max(y)\n",
    "#print X0\n",
    "Sum=sum(X0)\n",
    "X0= X0/Sum\n",
    "#print sorted(X0)\n",
    "'''\n",
    "Sets=OrderSets()\n",
    "Sum=0\n",
    "for i in range(len(X0)):\n",
    "\tif X0[i] < 0.00001:\n",
    "\t\tZ=0\n",
    "#\t        print(i+1,Sets[i],0)\n",
    "\telse:\n",
    "\t\tprob=float(format(X0.item(i),'.5f'))\n",
    "                print prob \n",
    "                Sum=Sum+prob\n",
    "#               print Sum\n",
    "#\t\tprint(i+1,Sets[i],prob)\n",
    "print Sum\n",
    "F=np.zeros((32,32))#,np.dtype('float64'))\n",
    "#print \n",
    "List=[i for i in range(16,32)]\n",
    "List1=[i for i in range(48,64)]\n",
    "List=List+List1\n",
    "print len(List)\n",
    "for i in range(len(List)):\n",
    "    for j in range(len(List)):\n",
    "        F[i,j]=C[List[i],List[j]]*X0[List[j]]-C[List[j],List[i]]*X0[List[i]]\n",
    "        \n",
    "\n",
    "\n",
    "#print F\n",
    "printZeroIndex(F,32)\n",
    "#print Sum\n",
    "#print max(y)\n",
    "#X=C*X0\n",
    "#print distance(X0,Xvi )\n",
    "#print X\n",
    "#print max(y)\n",
    "#print X\n",
    "#print B*X\n",
    "#print max(y)\n",
    "\n",
    "#print B\n",
    "#print A\n",
    "'''\n",
    "\n",
    "\n",
    "#printZeroIndex(W,64)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0], [1, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [0, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1], [0, 0, 0, 1, 1, 1], [1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]\n",
      "[[4.72133270e-18]\n",
      " [3.11186411e-18]\n",
      " [3.11186411e-18]\n",
      " [1.47344242e-18]\n",
      " [3.11186411e-18]\n",
      " [1.98619352e-18]\n",
      " [1.66387230e-18]\n",
      " [1.17282102e-18]\n",
      " [3.11186411e-18]\n",
      " [1.66387230e-18]\n",
      " [1.98619352e-18]\n",
      " [1.17282102e-18]\n",
      " [1.47344242e-18]\n",
      " [1.17282102e-18]\n",
      " [1.17282102e-18]\n",
      " [7.25221389e-19]\n",
      " [4.78373005e-02]\n",
      " [4.21787077e-02]\n",
      " [4.21787077e-02]\n",
      " [4.60520786e-02]\n",
      " [4.21787077e-02]\n",
      " [6.14354480e-02]\n",
      " [3.47689850e-02]\n",
      " [6.64945156e-02]\n",
      " [4.21787077e-02]\n",
      " [3.47689850e-02]\n",
      " [6.14354480e-02]\n",
      " [6.64945156e-02]\n",
      " [4.60520786e-02]\n",
      " [6.64945156e-02]\n",
      " [6.64945156e-02]\n",
      " [1.36626221e-01]\n",
      " [1.59113331e-18]\n",
      " [5.65397461e-19]\n",
      " [5.65397461e-19]\n",
      " [3.59609879e-19]\n",
      " [5.65397461e-19]\n",
      " [2.36673534e-19]\n",
      " [1.65442637e-19]\n",
      " [1.11102635e-19]\n",
      " [5.65397461e-19]\n",
      " [1.65442637e-19]\n",
      " [2.36673534e-19]\n",
      " [1.11102635e-19]\n",
      " [3.59609879e-19]\n",
      " [1.11102635e-19]\n",
      " [1.11102635e-19]\n",
      " [8.23360450e-20]\n",
      " [1.12328992e-02]\n",
      " [6.42051116e-03]\n",
      " [6.42051116e-03]\n",
      " [6.67540890e-03]\n",
      " [6.42051116e-03]\n",
      " [5.39997506e-03]\n",
      " [2.44224784e-03]\n",
      " [5.06041521e-03]\n",
      " [6.42051116e-03]\n",
      " [2.44224784e-03]\n",
      " [5.39997506e-03]\n",
      " [5.06041521e-03]\n",
      " [6.67540890e-03]\n",
      " [5.06041521e-03]\n",
      " [5.06041521e-03]\n",
      " [1.01386942e-02]]\n"
     ]
    }
   ],
   "source": [
    "print AllSets()\n",
    "# Steady state X0 \n",
    "print X0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0&\\frac{2}{3}&\\frac{2}{3}&0&\\frac{2}{3}&0&0&0&\\frac{2}{3}&0&0&0&0&0&0&0&\\frac{2}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{2}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "1&0&0&\\frac{1}{3}&0&\\frac{5}{6}&0&0&0&\\frac{2}{3}&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "1&0&0&\\frac{1}{3}&0&0&\\frac{2}{3}&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&\\frac{1}{2}&\\frac{1}{2}&0&0&0&0&\\frac{5}{6}&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "1&0&0&0&0&\\frac{5}{6}&\\frac{2}{3}&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&1&0&0&1&0&0&\\frac{1}{3}&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&1&0&1&0&0&\\frac{1}{2}&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&1&0&\\frac{1}{2}&\\frac{1}{2}&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "1&0&0&0&0&0&0&0&0&\\frac{2}{3}&\\frac{5}{6}&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&1&0&0&0&0&0&0&1&0&0&\\frac{1}{2}&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&1&0&0&0&0&0&1&0&0&\\frac{1}{3}&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&1&0&0&0&0&0&\\frac{1}{2}&\\frac{1}{2}&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&0&0&0&\\frac{5}{6}&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&0&1&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&1&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&\\frac{1}{2}&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&2&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&\\frac{5}{6}&0&\\frac{5}{6}&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{2}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&\\frac{1}{2}&0&\\frac{4}{3}&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&\\frac{1}{2}&0&0&\\frac{5}{6}&0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&\\frac{1}{2}&0&0&0&0&\\frac{4}{3}&0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&\\frac{4}{3}&\\frac{5}{6}&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&1&1&0&\\frac{1}{2}&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&1&0&0&1&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&\\frac{1}{2}&\\frac{1}{2}&1&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&\\frac{5}{6}&\\frac{4}{3}&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&1&0&0&1&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&1&0&1&\\frac{1}{2}&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&\\frac{1}{2}&\\frac{1}{2}&1&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&0&0&0&\\frac{4}{3}&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&0&1&1&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&1&0&1&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&\\frac{1}{2}&\\frac{1}{2}&2&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "2&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&\\frac{1}{3}&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&\\frac{2}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&\\frac{1}{3}&0&\\frac{1}{2}&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&\\frac{1}{3}&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&\\frac{1}{3}&0&0&0&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&\\frac{1}{2}&\\frac{1}{3}&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&\\frac{1}{2}&0&0&\\frac{1}{3}&0&0&0&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&\\frac{1}{2}&0&0&\\frac{1}{2}&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&\\frac{1}{3}&\\frac{1}{3}&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&\\frac{1}{3}&\\frac{1}{2}&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&\\frac{1}{2}&0&0&\\frac{1}{2}&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&\\frac{1}{2}&0&0&\\frac{1}{3}&0&0&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&\\frac{4}{3}&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&\\frac{1}{3}&\\frac{1}{3}&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&0&0&0&\\frac{1}{2}&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&0&\\frac{1}{2}&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&\\frac{1}{2}&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{2}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&\\frac{1}{3}&\\frac{1}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&2 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&2&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&\\frac{1}{2}&0&\\frac{1}{2}&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&\\frac{1}{2}&0&1&0&0&0&\\frac{1}{2}&0&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&\\frac{1}{2}&0&0&\\frac{1}{2}&0&0&0&1&0&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&\\frac{1}{3}&0&0&0&0&1&0&0&0&1&0&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&1&\\frac{1}{2}&0&0&0&0&0&\\frac{1}{2}&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&\\frac{1}{2}&1&0&\\frac{1}{2}&0&0&0&0&0&\\frac{1}{2}&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&\\frac{1}{2}&0&0&1&0&0&0&0&0&0&1&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&\\frac{1}{3}&\\frac{1}{3}&1&0&0&0&0&0&0&0&1 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{3}{2}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&0&0&\\frac{1}{2}&1&0&\\frac{1}{2}&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&0&\\frac{1}{2}&0&0&1&0&1&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&\\frac{1}{2}&0&1&\\frac{1}{2}&0&0&\\frac{1}{2}&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{2}&0&0&0&0&0&\\frac{1}{3}&\\frac{1}{3}&1&0&0&0&1 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{4}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&0&0&0&1&1&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&0&\\frac{1}{2}&1&0&1 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{5}{6}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&\\frac{1}{2}&0&1&1 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{2}{3}&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&\\frac{1}{3}&0&0&0&\\frac{1}{3}&0&\\frac{1}{3}&\\frac{1}{3}&2 \\\\\n",
      "\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "#print W.shape[:]\n",
    "print printZeroIndex(W,64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "X1=[]\n",
    "\n",
    "for i in X0:\n",
    "    if i < 10**-15:\n",
    "        X1.append(0)\n",
    "    else:\n",
    "        X1.append(float(i))\n",
    "#Min=min(X1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.04783730051710981, 0.04217870773001027, 0.04217870773001027, 0.046052078623884295, 0.04217870773001027, 0.06143544800942617, 0.03476898495115282, 0.06649451558567822, 0.04217870773001026, 0.03476898495115281, 0.06143544800942618, 0.06649451558567822, 0.0460520786238843, 0.06649451558567822, 0.06649451558567822, 0.1366262205492723, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.011232899249198946, 0.006420511161062555, 0.006420511161062558, 0.006675408904404798, 0.006420511161062558, 0.005399975064529306, 0.0024422478431686493, 0.0050604152068030985, 0.006420511161062557, 0.0024422478431686493, 0.005399975064529306, 0.0050604152068030985, 0.0066754089044047974, 0.0050604152068030985, 0.0050604152068030985, 0.010138694157070794]\n"
     ]
    }
   ],
   "source": [
    "print X1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.04784\n",
      "0.04218\n",
      "0.04218\n",
      "0.04605\n",
      "0.04218\n",
      "0.06144\n",
      "0.03477\n",
      "0.06649\n",
      "0.04218\n",
      "0.03477\n",
      "0.06144\n",
      "0.06649\n",
      "0.04605\n",
      "0.06649\n",
      "0.06649\n",
      "0.13663\n",
      "0.01123\n",
      "0.00642\n",
      "0.00642\n",
      "0.00668\n",
      "0.00642\n",
      "0.0054\n",
      "0.00244\n",
      "0.00506\n",
      "0.00642\n",
      "0.00244\n",
      "0.0054\n",
      "0.00506\n",
      "0.00668\n",
      "0.00506\n",
      "0.00506\n",
      "0.01014\n",
      "1.0\n",
      "32\n",
      "0&0.00247&0.00247&0&0.00247&0&0&0&0.00247&0&0&0&0&0&0&0&-0.00959&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "-0.00247&0&0&0.00194&0&0.00534&0&0&0&-0.00024&0&0&0&0&0&0&0&-0.00429&0&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "-0.00247&0&0&0.00194&0&0&-0.00024&0&0&0&0.00534&0&0&0&0&0&0&0&-0.00429&0&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&-0.00194&-0.00194&0&0&0&0&0.00525&0&0&0&0.00525&0&0&0&0&0&0&0&-0.00632&0&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "-0.00247&0&0&0&0&0.00534&-0.00024&0&0&0&0&0&0.00194&0&0&0&0&0&0&0&-0.00429&0&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&-0.00534&0&0&-0.00534&0&0&0.00253&0&0&0&0&0&0.00253&0&0&0&0&0&0&0&0.0054&0&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0.00024&0&0.00024&0&0&-0.00152&0&0&0&0&0&0&-0.00152&0&0&0&0&0&0&0&0.00244&0&0&0&0&0&0&0&0&0 \\\\\n",
      "0&0&0&-0.00525&0&-0.00253&0.00152&0&0&0&0&0&0&0&0&0.00182&0&0&0&0&0&0&0&0.0042&0&0&0&0&0&0&0&0 \\\\\n",
      "-0.00247&0&0&0&0&0&0&0&0&-0.00024&0.00534&0&0.00194&0&0&0&0&0&0&0&0&0&0&0&-0.00429&0&0&0&0&0&0&0 \\\\\n",
      "0&0.00024&0&0&0&0&0&0&0.00024&0&0&-0.00152&0&-0.00152&0&0&0&0&0&0&0&0&0&0&0&0.00244&0&0&0&0&0&0 \\\\\n",
      "0&0&-0.00534&0&0&0&0&0&-0.00534&0&0&0.00253&0&0&0.00253&0&0&0&0&0&0&0&0&0&0&0&0.0054&0&0&0&0&0 \\\\\n",
      "0&0&0&-0.00525&0&0&0&0&0&0.00152&-0.00253&0&0&0&0&0.00182&0&0&0&0&0&0&0&0&0&0&0&0.0042&0&0&0&0 \\\\\n",
      "0&0&0&0&-0.00194&0&0&0&-0.00194&0&0&0&0&0.00525&0.00525&0&0&0&0&0&0&0&0&0&0&0&0&0&-0.00632&0&0&0 \\\\\n",
      "0&0&0&0&0&-0.00253&0&0&0&0.00152&0&0&-0.00525&0&0&0.00182&0&0&0&0&0&0&0&0&0&0&0&0&0&0.0042&0&0 \\\\\n",
      "0&0&0&0&0&0&0.00152&0&0&0&-0.00253&0&-0.00525&0&0&0.00182&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0.0042&0 \\\\\n",
      "0&0&0&0&0&0&0&-0.00182&0&0&0&-0.00182&0&-0.00182&-0.00182&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0.00679 \\\\\n",
      "0.00959&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&-0.00241&-0.00241&0&-0.00241&0&0&0&-0.00241&0&0&0&0&0&0&0 \\\\\n",
      "0&0.00429&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0.00241&0&0&-0.00101&0&-0.00372&0&0&0&-0.00199&0&0&0&0&0&0 \\\\\n",
      "0&0&0.00429&0&0&0&0&0&0&0&0&0&0&0&0&0&0.00241&0&0&-0.00101&0&0&-0.00199&0&0&0&-0.00372&0&0&0&0&0 \\\\\n",
      "0&0&0&0.00632&0&0&0&0&0&0&0&0&0&0&0&0&0&0.00101&0.00101&0&0&0&0&-0.00415&0&0&0&-0.00415&0&0&0&0 \\\\\n",
      "0&0&0&0&0.00429&0&0&0&0&0&0&0&0&0&0&0&0.00241&0&0&0&0&-0.00372&-0.00199&0&0&0&0&0&-0.00101&0&0&0 \\\\\n",
      "0&0&0&0&0&-0.0054&0&0&0&0&0&0&0&0&0&0&0&0.00372&0&0&0.00372&0&0&-0.00103&0&0&0&0&0&-0.00103&0&0 \\\\\n",
      "0&0&0&0&0&0&-0.00244&0&0&0&0&0&0&0&0&0&0&0&0.00199&0&0.00199&0&0&-0.00077&0&0&0&0&0&0&-0.00077&0 \\\\\n",
      "0&0&0&0&0&0&0&-0.0042&0&0&0&0&0&0&0&0&0&0&0&0.00415&0&0.00103&0.00077&0&0&0&0&0&0&0&0&-0.00171 \\\\\n",
      "0&0&0&0&0&0&0&0&0.00429&0&0&0&0&0&0&0&0.00241&0&0&0&0&0&0&0&0&-0.00199&-0.00372&0&-0.00101&0&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&-0.00244&0&0&0&0&0&0&0&0.00199&0&0&0&0&0&0&0.00199&0&0&-0.00077&0&-0.00077&0&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&-0.0054&0&0&0&0&0&0&0&0.00372&0&0&0&0&0&0.00372&0&0&-0.00103&0&0&-0.00103&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&-0.0042&0&0&0&0&0&0&0&0.00415&0&0&0&0&0&0.00077&0.00103&0&0&0&0&-0.00171 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0.00632&0&0&0&0&0&0&0&0.00101&0&0&0&0.00101&0&0&0&0&-0.00415&-0.00415&0 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&-0.0042&0&0&0&0&0&0&0&0.00103&0&0&0&0.00077&0&0&0.00415&0&0&-0.00171 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&-0.0042&0&0&0&0&0&0&0&0.00077&0&0&0&0.00103&0&0.00415&0&0&-0.00171 \\\\\n",
      "0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&-0.00679&0&0&0&0&0&0&0&0.00171&0&0&0&0.00171&0&0.00171&0.00171&0 \\\\\n",
      "\n"
     ]
    }
   ],
   "source": [
    "Sets=OrderSets()\n",
    "Sum=0\n",
    "for i in range(len(X0)):\n",
    "\tif X0[i] < 0.00001:\n",
    "\t\tZ=0\n",
    "#\t        print(i+1,Sets[i],0)\n",
    "\telse:\n",
    "\t\tprob=float(format(X0.item(i),'.5f'))\n",
    "                print prob \n",
    "                Sum=Sum+prob\n",
    "#               print Sum\n",
    "#\t\tprint(i+1,Sets[i],prob)\n",
    "print Sum\n",
    "F=np.zeros((32,32))#,np.dtype('float64'))\n",
    "#print \n",
    "List=[i for i in range(16,32)]\n",
    "List1=[i for i in range(48,64)]\n",
    "List=List+List1\n",
    "print len(List)\n",
    "for i in range(len(List)):\n",
    "    for j in range(len(List)):\n",
    "        F[i,j]=C[List[i],List[j]]*X0[List[j]]-C[List[j],List[i]]*X0[List[i]]\n",
    "        \n",
    "\n",
    "\n",
    "#print F\n",
    "printZeroIndex(F,32)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}