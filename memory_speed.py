O(1) O(n) O(n^2)


# O(1)  X
def test(arr):
  a = 1
  b = 2
  lst = [1, 2, 3]	


# O(n)
def test(arr):
  lst = []
  
  for el in arr:
    lst.append(el * 2)
  
# O(n^2)
def test(arr):

  lst = []

  for el in arr:
    lst2 = arr
    lst.append(lst2)
