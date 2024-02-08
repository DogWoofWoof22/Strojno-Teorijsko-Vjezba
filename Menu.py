import pygame
import tkinter
import tkinter.filedialog
import sys
from pygame.rect import Rect

class Menu:
    def __init__(self) -> None:
        pass

    def PromptFile(self):
        top = tkinter.Tk()
        top.withdraw()
        self.FilePath = tkinter.filedialog.askdirectory(parent=top)
        top.destroy()
        return 

    def MouseDownEvent(self,buttons):
        for button in buttons:

            buttonData = button[0]
            buttonAction = button[1]

            if buttonData.left <= self.mousePosition[0] <= buttonData.right and buttonData.top <= self.mousePosition[1] <= buttonData.bottom: 
                
                return buttonAction()

    def QuitGameReturnPressedButton(self,buttonName = None):
        self.run = False
        if buttonName == None:
            return
        return buttonName
    
    def DrawButtonWithText(self,screen,x_pos,y_pos,width,height,primaryColor,hoverColor,text):

        if x_pos <= self.mousePosition[0] <= x_pos+width and y_pos <= self.mousePosition[1] <= y_pos+height: 
            rect = pygame.draw.rect(screen,hoverColor,[x_pos,y_pos,width,height]) 
        else: 
            rect = pygame.draw.rect(screen,primaryColor,[x_pos,y_pos,width,height])
        text = pygame.font.SysFont('Corbel',20).render(text , True , (0,0,0))
        screen.blit(text , text.get_rect(center = rect.center))

        return rect

    def CenterInfoText(self,screen,y_pos,textSize,textData):
        screenWidth = screen.get_rect().width
        chunkSize = screenWidth//(textSize//2)
        if len(textData) > chunkSize:
            iteration = 0
            while True:
                startIndex = chunkSize*iteration
                endIndex = chunkSize*(iteration+1)
                if endIndex >= len(textData):
                    endIndex = len(textData)-1
                    textChunk = textData[startIndex:endIndex]
                    text = pygame.font.SysFont('Corbel',textSize).render(textChunk , True , (255,255,255))
                    screen.blit(text , text.get_rect(centerx = screen.get_rect().centerx,centery = y_pos+iteration*textSize))
                    break
                textChunk = textData[startIndex:endIndex]
                text = pygame.font.SysFont('Corbel',textSize).render(textChunk , True , (255,255,255))
                screen.blit(text , text.get_rect(centerx = screen.get_rect().centerx,centery = y_pos+iteration*textSize))
                iteration += 1
        else:
            text = pygame.font.SysFont('Corbel',textSize).render(textData , True , (255,255,255))
            screen.blit(text , text.get_rect(centerx = screen.get_rect().centerx,centery = y_pos))

    
        

    def MainMenu(self):

        pygame.init()
        display = (200, 200)
        screen = pygame.display.set_mode(display)
        self.run = True
        buttons = []
        while self.run:

            for ev in pygame.event.get(): 
          
                if ev.type == pygame.QUIT:
                    
                    self.run = False
                    pygame.quit()
                    sys.exit()
                    
                if ev.type == pygame.MOUSEBUTTONDOWN:  

                    returnData = self.MouseDownEvent(buttons)
                        

                        
            screen.fill((0,0,0)) 
            self.mousePosition = pygame.mouse.get_pos()

            #Create data source button
            buttons.append([self.DrawButtonWithText(screen,0,0,200,40,(255,255,255),(200,200,200),"Choose Data Source"),lambda: self.QuitGameReturnPressedButton("Data Source")])

            #Create topics button
            buttons.append([self.DrawButtonWithText(screen,0,40,200,40,(255,255,255),(200,200,200),"Choose Topics"),lambda: self.QuitGameReturnPressedButton("Topics")])

            #Create mode button
            buttons.append([self.DrawButtonWithText(screen,0,80,200,40,(255,255,255),(200,200,200),"Choose Mode"),lambda: self.QuitGameReturnPressedButton("Mode")])

            #Create start button
            buttons.append([self.DrawButtonWithText(screen,0,120,200,40,(255,255,255),(200,200,200),"Start"),lambda: self.QuitGameReturnPressedButton("Start")])
            
            pygame.display.update()
        
        pygame.quit()
        return returnData

    def FilePathInput(self):
        pygame.init()
        display = (300, 210)
        screen = pygame.display.set_mode(display)
        self.run = True
        buttons = []
        self.FilePath = ""
        while self.run:
            for ev in pygame.event.get(): 
          
                if ev.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    sys.exit()
                
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    
                    returnData = self.MouseDownEvent(buttons)
                
                if ev.type == pygame.KEYDOWN: 
                    if ev.key == pygame.K_RETURN:
                        self.run = False
                        
            screen.fill((0,0,0)) 
            self.mousePosition = pygame.mouse.get_pos()

            #screen.blit(pygame.font.SysFont('Corbel',20).render('Please select data source :' , True , (255,255,255)) , (screen.get_rect().centerx,10))
            self.CenterInfoText(screen,30,20,"Please select data source :")
            self.CenterInfoText(screen,50,20,self.FilePath)

            #Create data source button
            buttons.append([self.DrawButtonWithText(screen,50,130,200,40,(255,255,255),(200,200,200),"Select File"),lambda: self.PromptFile()])

            #Create topics button
            buttons.append([self.DrawButtonWithText(screen,50,170,200,40,(255,255,255),(200,200,200),"Done"),lambda: self.QuitGameReturnPressedButton("Topics")])

            '''if 130 < mouse[1] <= 170: 
                pygame.draw.rect(screen,(200,200,200),[55,130,200,40]) 
            else: 
                pygame.draw.rect(screen,(255,255,255),[55,130,200,40])
            screen.blit(pygame.font.SysFont('Corbel',20).render('Select File' , True , (0,0,0)) , (120,140)) 

            if 170 < mouse[1] <= 210: 
                pygame.draw.rect(screen,(200,200,200),[55,170,200,40]) 
            else: 
                pygame.draw.rect(screen,(255,255,255),[55,170,200,40])
            screen.blit(pygame.font.SysFont('Corbel',20).render('Done' , True , (0,0,0)) , (130,180))
            '''
            pygame.display.flip()
        
        pygame.quit()
        return self.FilePath

    
