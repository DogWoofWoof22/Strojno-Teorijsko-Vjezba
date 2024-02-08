import pygame
import tkinter
import tkinter.filedialog
import sys
from pygame.rect import Rect

class Menu:
    def __init__(self) -> None:
        pass
    
    def DrawButtonWithText(self,screen,x_pos,y_pos,width,height,primaryColor,hoverColor,text):

        if x_pos <= self.mousePosition[0] <= x_pos+width and y_pos <= self.mousePosition[1] <= y_pos+height: 
            rect = pygame.draw.rect(screen,hoverColor,[x_pos,y_pos,width,height]) 
        else: 
            rect = pygame.draw.rect(screen,primaryColor,[x_pos,y_pos,width,height])
        text = pygame.font.SysFont('Corbel',20).render(text , True , (0,0,0))
        screen.blit(text , text.get_rect(center = rect.center)) 

    def MainMenu(self):
        pygame.init()
        display = (200, 200)
        screen = pygame.display.set_mode(display)
        run = True
        while run:
            for ev in pygame.event.get(): 
          
                if ev.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                    
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    
                    if 0 <= self.mousePosition[1] <= 40: 
                        pygame.quit()
                        return 1
                    if 40 < self.mousePosition[1] <= 80: 
                        pygame.quit()
                        return 2
                    if 80 < self.mousePosition[1] <= 120: 
                        pygame.quit()
                        return 3
                    if 120 < self.mousePosition[1] <= 160: 
                        pygame.quit()
                        return 4
                        

                        
            screen.fill((0,0,0)) 
            self.mousePosition = pygame.mouse.get_pos()


            #Create data source button
            self.DrawButtonWithText(screen,0,0,200,40,(255,255,255),(200,200,200),"Choose Data Source")

            #Create topics button
            self.DrawButtonWithText(screen,0,40,200,40,(255,255,255),(200,200,200),"Choose Topics")

            #Create mode button
            self.DrawButtonWithText(screen,0,80,200,40,(255,255,255),(200,200,200),"Choose Mode")

            #Create start button
            self.DrawButtonWithText(screen,0,120,200,40,(255,255,255),(200,200,200),"Start")
            pygame.display.update()
        
        pygame.quit()

    
def prompt_file():
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name