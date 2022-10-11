import bpg
import pygame
class Image(bpg.Component):
    def __init__(self,path) -> None:
    
        self.image = pygame.image.load(path).convert()
    @property
    def width(self) -> int:
        return self.image.get_width()
    @property
    def height(self) -> int:
        return self.image.get_height()
        
    def onAdd(self, objWindow) -> None:
        objWindow.window.blit(self.image,(self.x,self.y))
    def onDraw(self, objWindow) -> None:
        self.onAdd(objWindow)
class Button(bpg.Component):
    '''
    @deprecated
    // Never really worked as intentional. Be sure to 
    '''
    def __init__(self,x:int=0,y: int=0,sizeX: int=100,sizeY: int=50, color: tuple=(0,0,0)):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.buttonActive = False
    def onAdd(self, objWindow) -> None:
        pygame.draw.rect(objWindow.window,self.color,(self.x,self.y,self.x+self.sizeX,self.y+self.sizeY))
    def onDraw(self, objWindow) -> None:
        self.onAdd(objWindow)
        for e in objWindow.events:
            if e.type == pygame.MOUSEBUTTONUP:
                #print("Hi!")
                mousePos = pygame.mouse.get_pos()
                if mousePos[0] < self.x+self.sizeX and mousePos[0] > self.x and mousePos[1] < self.y+self.sizeY and mousePos[1] > self.y:
                    self.buttonActive = True
                    print("Hello!")
                else:
                    self.buttonActive = False
    def onClose(self, objWindow) -> None:
        self.buttonActive = False
    def getbuttonActive(self):
        return self.buttonActive