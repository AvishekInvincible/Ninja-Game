import pygame
class TextButton():
    def __init__(self, X_Value, y_Value, image, scale):
            #Create the constructor 
            #Set all the variables 
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) #Transform the image 
            self.rect = self.image.get_rect()# Craete a rect 
            self.rect.topleft = (X_Value, y_Value) # Set the top left of the rect to the x and y value 
            self.clicked = False #clicked to false 
            
            
            
            
    def draw(self, surface): #Draws the button on the screen 
            click = False #The variable to give the click 

            #get mouse position
            pos = pygame.mouse.get_pos() 

            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    click = True
                    self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0: # Check if the mnouse got not pressed 
                self.clicked = False #set to false 

            #draw button
            surface.blit(self.image, (self.rect.X_Value, self.rect.y_Value)) #display the button on the screen 
            return click #return the value
