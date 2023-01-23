from include import System
import re, os

diretorio_image = os.path.join('..','Imagens')
diretorio_video = os.path.join('..','Videos')

diretorio_Doc = os.path.join('..','Documentos')

diretorio_music = os.path.join('..','Musicas')

diretorio_etc = os.path.join('..','Outros')

diretorio_dow = os.path.join('..')

def SelectMovie(list):
  for video in list:
    with open(os.path.join(diretorio_dow, video), 'rb') as data:
      readData = data.read()
      data.close()
    os.remove(os.path.join(diretorio_dow,video))
    with open(os.path.join(diretorio_video, video), 'wb') as fileImg:
      fileImg.write(readData)
      fileImg.close()

def SelectMusic(list):
  for music in list:
    with open(os.path.join(diretorio_dow, music), 'rb') as data:
      readData = data.read()
      data.close()
    os.remove(os.path.join(diretorio_dow,music))
    with open(os.path.join(diretorio_music, music), 'wb') as fileImg:
      fileImg.write(readData)
      fileImg.close()
      

def SelectImage(list):
  for imgs in list:
    with open(os.path.join(diretorio_dow, imgs), 'rb') as data:
      readData = data.read()
      data.close()
    os.remove(os.path.join(diretorio_dow,imgs))
    with open(os.path.join(diretorio_image, imgs), 'wb') as fileImg:
      fileImg.write(readData)
      fileImg.close()
      

def SelectDocuments(list):
  for doc in list:
    with open(os.path.join(diretorio_dow, doc), 'rb') as data:
      readData = data.read()
      data.close()
    os.remove(os.path.join(diretorio_dow,doc))
    with open(os.path.join(diretorio_Doc, doc), 'wb') as fileImg:
      fileImg.write(readData)
      fileImg.close()
      

def SelectOutros(list):
  for outro in list:
    with open(os.path.join(diretorio_dow, outro), 'rb') as data:
      readData = data.read()
      data.close()
    os.remove(os.path.join(diretorio_dow,outro))
    with open(os.path.join(diretorio_etc, outro), 'wb') as fileImg:
      fileImg.write(readData)
      fileImg.close()

class app:
  def __init__(self):
    self.dir_imgs = os.path.join('..','Imagens')
    self.dir_Download = os.path.join('..')
    self.itens = System.OpenFolder()
    
  def run(self):
    for file in self.itens:
      
      self.documents = re.findall(r'.*\.log|.*\.pdf|.*\.txt', file)
      
      self.videos = re.findall(r'.*\.mp4|.*\.webm', file)
      
      self.musicas = re.findall(r'.*\.mp3|.*\.m4a', file)
      
      self.images = re.findall(r'.*\.png|\.*.jpeg|.*\.jpg', file)
      
      self.outros = re.findall(r'.*\.rar|.*\.iso|.*\.zip|.*\.apk', file)
      
      if self.images == []:
        if self.musicas == []:
          if self.documents == []:
            if self.videos == []:
              if self.outros == []:
                pass
              else:
                SelectOutros(self.outros)
            else:
              SelectMovie(self.videos)
          else:
            SelectDocuments(self.documents)
        else:
          SelectMusic(self.musicas)
      else:
        SelectImage(self.images)
    print ('Concluido!')
      
          
    
if __name__ == '__main__':
  System.Reagrup("Imagens")
  System.Reagrup("Videos")
  System.Reagrup("Musicas")
  System.Reagrup("Documentos")
  System.Reagrup("Outros")
  
  app().run()
    
