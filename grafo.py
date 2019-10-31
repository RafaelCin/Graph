import numpy as np

class Grafo():
  def __init__(self, objiter, directed = False, listaOfAdj = {}):
    self.directed = directed
    self.listOfAdj = self.createGraphVtr(objiter)
  
  def createGraphVtr(self, obj):
    dic = {}
    for element in obj:
      n0 = element[0]
      n1 = element[1]
      if (n0 in dic) is False:
        if len(element) > 2:
          dic.update({n0: [(n1,element[2])]})
        else:
          dic.update({n0: [n1]})
      else:
        if len(element) > 2:
          dic[n0].append((n1,element[2]))
        else:
          dic[n0].append(n1)
      if self.directed == False:
        if (n1 in dic) is False:
          if len(element) > 2:
            dic.update({n1: [(n0,element[2])]})
          else:
            dic.update({n1: [n0]})
        else:
          if len(element) > 2:
            dic[n1].append((n0,element[2]))
          else:
            dic[n1].append(n0)
    return dic
  def __str__(self):
    lis = []
    i = 0
    keysH = ''
    # print('Matriz de adjacência')
    # for j in self.keys:
    #   keysH += str(j) + '    ' 
    # print('   ',keysH)
    # for element in self.mtxOfAdj:
    #   for element1 in element:
    #     lis.append(element1)
    #   print(str(self.keys[i]) + ' ' + str(lis))
    #   lis = []
    #   i += 1
    print('Lista de Adjacencia')
    for key in self.listOfAdj:
      print(str(key) + ':', self.listOfAdj[key])
    
  def __repr__(self):
    v = Grafo(((0,1),(0,2),(0,3),(1,2),(2,3)))
    return v

  def __getitem__(self, vert):
    listOfTup = []
    lis = self.listOfAdj
    for element in lis[vert]:
      listOfTup.append((vert, element))
    print(listOfTup)
    return listOfTup
    
  def transformMtx(self):
    mtx = np.zeros((len(self.listOfAdj), len(self.listOfAdj)))
    lisAdj = self.listOfAdj
    for key in lisAdj:
      for i in lisAdj[key]:
        if type(i) == type((0,1)):
          mtx[key][i[0]] = i[1]
        else:
          mtx[key][i] += 1
    print(mtx)

  def addVer(self, ver, ver2Lig):
    if (ver in self.listOfAdj) is False:
      if (ver2Lig in self.listOfAdj) is True:
        dic = self.listOfAdj
        dic.update({ver: [ver2Lig]})
        if self.directed is False:
          dic[ver2Lig].append(ver)
        print(dic)
      else:
        print('ver not exist')
    else:
      print('ver already exists')
    return ver
   
  
  def addEdge(self, edge, weight = 1):
    ver1 = edge[0]
    ver2 = edge[1]
    if (ver2 in self.listOfAdj[ver1]) is False:
      if (ver1 in self.listOfAdj) and (ver2 in self.listOfAdj):
        newDic = self.listOfAdj
        newDic[ver1].append(ver2)
        if self.directed is False:
          newDic[ver2].append(ver1)
        print(newDic)
      else:
        print('Error, cannot add this edge')
    else:
      print('edge already exists')
    return ''

  def ligVer(self, tupleOfVer):
    lig = False
    ver1 = tupleOfVer[0]
    ver2 = tupleOfVer[1]
    if (ver1 in self.listOfAdj) and (ver2 in self.listOfAdj):
      if (ver1 in self.listOfAdj[ver2]) or (ver2 in self.listOfAdj[ver1]):
        lig = True
    print(lig)
    return lig
  
  def entraceDegree(self, ver):
    degree = 0
    dic = self.listOfAdj
    for element in dic[ver]:
      # (1,0) apenas para pegar o type tuple
      if type(element) == type((1,0)):
        degree += element[1]
      else:
        degree += 1
    print(degree)
    return degree
  
  def exitDegree(self, ver):
    degree = 0
    dic = self.listOfAdj
    for element in dic:
      for i in dic[element]:
        if type(i) == type((1,0)):
          if i[0] == ver:
            degree += i[1]
        else:
          if i == ver:
            degree += 1
    print(degree)
    return degree
  
  
  def biggestEdge(self):
    biggest = 0
    dic = self.listOfAdj
    for element in dic:
      for i in dic[element]:
        if type(i) == type((1,0)):
          if biggest < i[1]:
            biggest = i[1]
        else:
          if biggest < 1:
            biggest = 1
    print(biggest)
    return biggest

  def smallerEdge(self):
    smaller = self.biggestEdge()
    dic = self.listOfAdj
    for element in dic:
      for i in dic[element]:
        if type(i) == type((1,0)):
          if smaller > i[1]:
            smaller = i[1]
        else:
          if smaller > 1:
            smaller = 1
    print(smaller)
    return smaller
  

  def adjacent(self, ver):
    dic = self.listOfAdj
    listOfAdjc = [] 
    if ver in dic:
      for element in dic[ver]:
        if type(element) == type((1,0)):
          listOfAdjc.append(element[0])
        else:
          listOfAdjc.append(element)
    print(listOfAdjc)
    return listOfAdjc
  

  def widthSearch(self, ver):
    queue = []
    width = {}
    dad = {}
    
    queue.append(ver)
    dad[ver] = None
    width[ver] = 1

    while len(queue):
      newVer = queue.pop(0)
      for neibor in  self.listOfAdj.get(newVer):
        if not width.get(neibor):
          queue.append(neibor)
          width[neibor] = 1
          dad[neibor] = newVer
    return dad     
    
  def dfs(self, ver):
    marked = []
    dad = {}
    for element in self.listOfAdj[ver]:
      if (element in marked) is False:
        self.dfs2(element, dad, marked)
    print(dad)
  
  def dfs2(self, ver, dad, marked):
    marked.append(ver)
    for element in self.listOfAdj[ver]:
      if (element in marked) is False:
        dad[element] = ver
        self.dfs2(element, dad, marked)
    

grafo = Grafo(((0,1),(0,2),(0,3),(1,2),(2,3)))
grafo.__str__()
grafo.__repr__()
grafo.__getitem__(0)
grafo.transformMtx()
grafo.addVer(9,0)
grafo.addEdge((3,1))
grafo.ligVer((9,1))
grafo.entraceDegree(0)
grafo.exitDegree(0)
grafo.biggestEdge()
grafo.smallerEdge()
grafo.adjacent(0)
print(grafo.widthSearch(9))
grafo.dfs(9)

      
       
    

      
      
    