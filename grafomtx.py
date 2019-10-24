import numpy as np

class GraphMtx():
  def __init__(self, objiter, directed = False, listaOfAdj = {}, mtxOfAdj = None, keys=None, wheght=None):
    self.directed = directed
    graphNKeys = self.createGraphMtx(objiter)
    self.mtxOfAdj = graphNKeys[0]
    self.keys = graphNKeys[1]
    self.weight = graphNKeys[2]
  
  def createGraphMtx(self, obj):
    mtx = []
    weight = []
    for element in obj:
      if len(element) > 2:
        weight.append(element[2])
      if (element[1] in mtx) is False:
        mtx.append(element[1])
      if (element[0] in mtx)  is False:
        mtx.append(element[0])
    mtxAdj = np.zeros((len(mtx), len(mtx)))
    mtx.sort()
    finalMtx = self.buildMtx(obj, mtx, weight)
    return finalMtx
  def buildMtx(self, obj, mtx, weight):
    mtxAdj = np.zeros((len(mtx), len(mtx)))
    for element in obj:
      n0 = element[0]
      n1 = element[1]
      ind0 = mtx.index(n0)
      ind1 = mtx.index(n1)
      if len(element) < 3:
        mtxAdj[ind0][ind1] += 1
        if self.directed == False:
          mtxAdj[ind1][ind0] += 1
      else:
        mtxAdj[ind0][ind1] += element[2]
        if self.directed == False:
          mtxAdj[ind1][ind0] += element[2]
    return mtxAdj, mtx, weight
  
  def __str__(self):
    lis = []
    i = 0
    keysH = ''
    for j in self.keys:
      keysH += str(j) + '    ' 
    print('   ',keysH)
    for element in self.mtxOfAdj:
      for element1 in element:
        lis.append(element1)
      print(str(self.keys[i]) + ' ' + str(lis))
      lis = []
      i += 1
  
  def __getitem__(self, ver):
    if (ver in self.keys) is False:
      print('Invalid Ver')
      return ''
    else:
      listOfTup = []
      indx = 0
      elementMtx = self.mtxOfAdj[self.keys.index(ver)] 
      for element in elementMtx:
        if element > 0:
          listOfTup.append((ver,self.keys[indx]))
        indx += 1
      print(listOfTup)
    return listOfTup

  def transformVtr(self):
    dic = {}
    auxLis = []
    indxL = 0
    indxC = 0
    mtx = self.mtxOfAdj
    for element in mtx: 
      for i in element:
        if i > 0:
          auxLis.append(self.keys[indxL])
        indxL +=1
      dic.update({self.keys[indxC]: auxLis})
      indxC += 1
      indxL = 0
      auxLis = []
    print(dic)
  
  # Adicionar um vertice (feito), adcionar uma aresta(feito), se dois vertices estao ligados(feito)
  # Grau de entrada(feito), grau de saida(feito), adjacente(feito), menor aresta(feito), maior aresta(feito)

  def addVer(self, ver, ligVer):
    indxi = 0
    indxj = 0
    mtx = self.mtxOfAdj
    self.keys.append(ver)
    newMtx = np.zeros((len(self.keys), len(self.keys)))
    for i in mtx:
      for j in i:
        if j > 0:
          newMtx[indxi][indxj] = j
        indxj += 1
      indxj = 0
      indxi += 1
    # newMtx[len(self.keys) - 1][len(self.keys) - 1] = 1
    if ligVer in self.keys:
      print(self.keys.index(ver))
      newMtx[self.keys.index(ligVer)][self.keys.index(ver)] += 1
      if self.directed is False:
         newMtx[self.keys.index(ver)][self.keys.index(ligVer)] += 1
    else:
      print('vertice dado para ligação inexistente')
    self.mtxOfAdj = newMtx
    print(newMtx)
  
  def addEdge(self, edge):
    for element in edge:
      if (element in self.keys) is False:
        print('Key do not exist in Graph')
        return ''
    if self.directed == True or edge[0] == edge[1]:
      indx1 = self.keys.index(edge[0])
      indx2 = self.keys.index(edge[1])
      self.mtxOfAdj[indx1][indx2] += 1
    else:
      indx1 = self.keys.index(edge[0])
      indx2 = self.keys.index(edge[1])
      self.mtxOfAdj[indx1][indx2] += 1
      self.mtxOfAdj[indx2][indx1] += 1
    print(self.mtxOfAdj)
  
  def verLig(self, ver1, ver2):
    ligation = False
    if (ver1 in self.keys) and (ver2 in self.keys):
      if self.mtxOfAdj[self.keys.index(ver2)][self.keys.index(ver1)] > 0 and self.mtxOfAdj[self.keys.index(ver1)][self.keys.index(ver2)]:
        ligation = True
    else:
      ligation = 'some ver or both do not exist'
    print(ligation)
    return ligation
  
  def exitDegree(self, ver):
    degree = 0
    if (ver in self.keys) is True: 
      for element in self.mtxOfAdj:
        degree += element[self.keys.index(ver)]
    print(degree)
    return degree
  
  def entranceDeg(self, ver):
    degree = 0
    if (ver in self.keys) is True:
      for element in self.mtxOfAdj[self.keys.index(ver)]:
        degree += element
    print(degree)
    return degree

  def biggestEdge(self):
    biggest = 0
    listOfEdges = []
    indxC = 0
    indxL = 0
    for element in self.mtxOfAdj:
      for number in element:
        if number > biggest:
          biggest = number
          listOfEdges = [(self.keys[indxC],self.keys[indxL])]
        elif number == biggest:
          listOfEdges += [(self.keys[indxC],self.keys[indxL])]
        indxL += 1
      indxL = 0
      indxC += 1
    print(listOfEdges)
    print(biggest)
    return listOfEdges

  def smallerEdge(self):
    listOfEdges = []
    smaller = self.mtxOfAdj[0][0]
    indxC = 0
    indxL = 0
    for element in self.mtxOfAdj:
      for number in element:
        
        if number < smaller:
          smaller = number
          listOfEdges = [(self.keys[indxC],self.keys[indxL])]
        elif number == smaller:
          listOfEdges += [(self.keys[indxC],self.keys[indxL])]
        indxL += 1
      indxL = 0
      indxC += 1
    print(smaller)
    print(listOfEdges)
    return listOfEdges

  def adjecent(self, ver):
    listOfAdjc = []
    indx = self.keys.index(ver)
    indx2 = 0
    for element in self.mtxOfAdj:
      if element[indx] > 0:
        listOfAdjc.append(self.keys[indx2])
      indx2 += 1
    print(listOfAdjc)
    return listOfAdjc

    

    





    
    


      
    



graph = GraphMtx(((0,1,2),(0,2,7),(0,3,4),(1,2,1),(2,3,12)))
graph.__str__()
graph.__getitem__(3)
graph.addVer(9,0)
graph.addEdge((2,2))
graph.verLig(1,2)
graph.exitDegree(0)
graph.entranceDeg(0)
graph.biggestEdge()
graph.smallerEdge()
graph.adjecent(0)