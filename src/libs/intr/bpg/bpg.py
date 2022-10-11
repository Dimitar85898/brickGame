import pygame
class Position:
    x = 0
    y = 0
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
class Component:
    x = 0
    y = 0
    def __init__(self):
        pass
    def onDraw(self,objWindow) -> None:
        pass
    def onAdd(self,objWindow) -> None:
        '''
        !!!!THIS SHOULD NOT BE USED OUTSIDE OF THE WINDOW CLASS WITH add() METHOD!!!!
        '''
        pass
    def setPos(self,arg) -> None:
        if type(arg) == tuple:
            x = arg[0]
            y = arg[1]
        elif type(arg) == Position:
            x = arg.x
            y = arg.y
        else:
            raise Exception("Parameter Object Not Recognised. List of posible arguments:\n- tuple\n- Position")
        self.x = x
        self.y = y
class Window:
    window = None
    components = []
    redrawOnAdd = True
    updateOnRedraw = True
    @property
    def width(self) -> int:
        return self.window.get_width()
    @property
    def height(self) -> int:
        return self.window.get_height()
    def setIcon(self,iconPath) -> None:
        a = pygame.image.load(iconPath).convert()
        pygame.display.set_icon(a)
    def setTitle(self,title) -> None:
        pygame.display.set_caption(title)
    def __init__(self,*args) -> None:
        self.window = pygame.display.set_mode(args)
        self.size = args[0]
    def add(self,objComponent) -> None:
        objComponent.onAdd(self)
        self.components.append(objComponent)
        if self.redrawOnAdd:
            self.redraw()
    def updateSprites(self,i=0,all=False) -> None:
        if all:
            for comp in self.components:
                comp.onDraw(self) 
        else:
            self.components[i].onDraw(self)
            
    def redraw(self) -> None:
        pygame.display.update()
        self.window.fill((0,0,0))
        if self.updateOnRedraw:
            self.updateSprites(all=True)
    
        