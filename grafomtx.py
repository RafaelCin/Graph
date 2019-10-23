import numpy as np

class GraphMtx():
  def __init__(self, objiter, directed = False, listaOfAdj = {}, mtxOfAdj = None, keys=None):
    self.directed = directed
    graphNKeys = self.createGraphMtx(objiter)
    self.mtxOfAdj = graphNKeys[0]
    self.keys = graphNKeys[1]
  
  def createGraphMtx(self, obj):
    mtx = []
    for element in obj:
      if (element[1] in mtx) is False:
        mtx.append(element[1])
      if (element[0] in mtx)  is False:
        mtx.append(element[0])
    mtxAdj = np.zeros((len(mtx), len(mtx)))
    mtx.sort()
    finalMtx = self.buildMtx(obj, mtx)
    return finalMtx
  def buildMtx(self, obj, mtx):
    mtxAdj = np.zeros((len(mtx), len(mtx)))
    for element in obj:
      n0 = element[0]
      n1 = element[1]
      ind0 = mtx.index(n0)
      ind1 = mtx.index(n1)
      mtxAdj[ind0][ind1] += 1
      if self.directed == False:
        mtxAdj[ind1][ind0] += 1
    return mtxAdj, mtx
  
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
  
  # Adicionar um vertice, adcionar uma aresta, se dois vertices estao ligados
  # Grau de entrada, grau de saida, adjacente, menor aresta, maior aresta

  def addVer(self, ver):
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
    newMtx[len(self.keys) - 1][len(self.keys) - 1] = 1
    self.mtxOfAdj = newMtx
    print(newMtx)


graph = GraphMtx(((0,1),(0,2),(0,3),(1,2),(2,3)))
graph.__str__()
graph.__getitem__(3)
graph.addVer(9)