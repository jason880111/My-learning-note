{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def quicksort(mylist):\n",
    "    smaller = []\n",
    "    bigger = []\n",
    "\n",
    "    if len(mylist) <= 1:\n",
    "        return mylist\n",
    "\n",
    "    else:\n",
    "        pivot = mylist[0] #第一個數為pivot\n",
    "        for i in mylist:\n",
    "            if i < pivot: #比基準值小的數\n",
    "                smaller.append(i)\n",
    "            elif i > pivot: #比基準值大的數\n",
    "                bigger.append(i)\n",
    "\n",
    "    smaller = quicksort(smaller)\n",
    "    bigger = quicksort(bigger)\n",
    "    return smaller + [pivot] + bigger"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "list = [5, -8, -15, -23, 0, 3, 14, -5, 10, 28]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-23, -15, -8, -5, 0, 3, 5, 10, 14, 28]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "quicksort(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
