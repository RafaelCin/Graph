import numpy as np

class Grafo():
  def __init__(self, objiter, directed = False, listaOfAdj = {}, mtxOfAdj = None, keys=None):
    self.directed = directed
    self.listOfAdj = self.createGraphVtr(objiter)
    graphNKeys = self.createGraphMtx(objiter)
    self.mtxOfAdj = graphNKeys[0]
    self.keys = graphNKeys[1]
  
  def createGraphVtr(self, obj):
    dic = {}
    for element in obj:
      n0 = element[0]
      n1 = element[1]
      if (n0 in dic) is False:
        dic.update({n0: [n1]})
      else:
        dic[n0].append(n1)
      if self.directed == False:
        if (n1 in dic) is False:
          dic.update({n1: [n0]})
        else:
          dic[n1].append(n0)
    return dic
  def __str__(self):
    lis = []
    i = 0
    keysH = ''
    print('Matriz de adjacência')
    for j in self.keys:
      keysH += str(j) + '    ' 
    print('   ',keysH)
    for element in self.mtxOfAdj:
      for element1 in element:
        lis.append(element1)
      print(str(self.keys[i]) + ' ' + str(lis))
      lis = []
      i += 1
    print('Lista de Adjacencia')
    for key in self.listOfAdj:
      print(str(key) + ':', self.listOfAdj[key])
    

  def createGraphMtx(self, obj):
    mtx = []
    for element in obj:
      if (element[1] in mtx) is False:
        mtx.append(element[1])
      if (element[0] in mtx)  is False:
        mtx.append(element[0])
    mtxAdj = np.zeros((len(mtx), len(mtx)))
    mtx.sort()
    # for element in obj:
    #   n0 = element[0]
    #   n1 = element[1]
    #   ind0 = mtx.index(n0)
    #   ind1 = mtx.index(n1)
    #   mtxAdj[ind0][ind1] += 1
    #   if self.directed == False:
    #     mtxAdj[ind1][ind0] += 1
    # return mtxAdj, mtx
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

  def __getitem__(self, vert):
    listOfTup = []
    lis = self.listOfAdj
    for element in lis[vert]:
      listOfTup.append((vert, element))
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
  def transformMtx(self):
    mtx = np.zeros((len(self.keys), len(self.keys)))
    lisAdj = self.listOfAdj
    for key in lisAdj:
      for i in lisAdj[key]:
        mtx[key][i] += 1
    print(mtx)

# Adicionar um vertice, adcionar uma aresta, se dois vertices estao ligados
# Grau de entrada, grau de saida, adjacente, menor aresta, maior aresta
  def addVer(self, ver):
    lisAdj = self.listOfAdj
    lisAdj.update({ver: []})
    if self.directed:
      lisAdj[self.keys[len(self.keys) - 1]].append(ver)
    else:
      lisAdj[self.keys[len(self.keys) - 1]].append(ver)
      lisAdj[ver].append(self.keys[len(self.keys) - 1])
    print(lisAdj)
    
    

grafo = Grafo(((0,1),(0,2),(0,3),(1,2),(2,3)))
grafo.__str__()
grafo.__getitem__(0)
grafo.transformVtr()
grafo.transformMtx()
grafo.addVer(9)
      
       
    

      
      
    