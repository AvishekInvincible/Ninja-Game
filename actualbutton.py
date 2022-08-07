import pygame
class ActualButton():
    def __init__(self, image, position, text_input, font, color_base, hovering_color): # Creating a constructor 
        self.image = image 
        self.x_position = position[0]
        self.y_position = position[1]
        self.font = font
        self.color_base, self.hovering_color = color_base, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.color_base) # Using the font to get the text rendered with the font
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_position, self.y_position)) # creating image rectangle using the x and y positionitions provided
        self.text_rect = self.text.get_rect(center=(self.x_position, self.y_position))# creating text rectangle using the x and y positionitions provided

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect) # This allows to display the image onto the screen if there is one image 
        screen.blit(self.text, self.text_rect) #This displays the text onto the image 
       

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom): 
            click = pygame.mixer.Sound('Music/button.wav') # Loads the music from the files using pygame mixer 
            click.set_volume(0.09) # Setting the volume for the button to 0.09 
            click.play() # Then play once if the button got clicked 
            print('Play')
            return True
        return False

    def changeColor(self, position):
        
        
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            
        else:
            self.text = self.font.render(self.text_input, True, self.color_base)
