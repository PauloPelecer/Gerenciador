import os, time, re

img = ['image.png', 'image.mp4']

#abrir pasta
def OpenFolder():
    dir = os.path.join('..') #os.path.abspath('..')
    filename = os.listdir(dir)
    return filename
#localizar arquivos
def Reagrup(dir):
  dir = os.path.join('..', dir)
  if not os.path.isdir(dir):
    os.mkdir(dir)
    
#separar arquivos
def SelectFile(arq):
  listImg = ['.png', '.jpeg','.jpg']
  listVid = ['.mp4','.webm']
  listDoc = ['.pdf','.log','.txt']
  print ('separando Imagen')
#SelectFile(img)
  
#apagar Arquivos iguais

