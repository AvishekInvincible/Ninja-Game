import pygame,random,time
from actualbutton import ActualButton
class problemMath():
    
    def __init__(self,age,moving_right,moving_left,shoot):#Create a constructor 
        #Set the variables 
        self.age = age 
        self.t = 10
        self.moving_right = moving_right
        self.moving_left = moving_left
        self.shoot = shoot
            
    def gen_two_nums(self): #This function generate two random numbers every time
        if self.age>0:
            if self.age<=15:
                return  random.randint(0, 15),random.randint(0, 15) 
            else:
                return random.randint(0, 20),random.randint(0, 20)       
    def generate_problem(self): #This function create the problem 
        arthmetic = ['*','+','-'] #Different operators 
        chosen_arth = random.choice(arthmetic) #Chosing them randomly
        i,j = self.gen_two_nums() #Getting two random numbers 
        Question  = f'What is {i} {chosen_arth} {j} = ?' #Combining it into an question 
        Answer = f'{i}{chosen_arth}{j}' #Combining it into an answer  
        return Question,eval(Answer) 
    def right(self,a,b): #This checks if the answer is right 
        if len(str(a)) == len(str(b)):
            if int(a)==int(b):
                return True
            else:
                return False
        else:
            return False
    def problem_win(self):
        clock = pygame.time.Clock()#Start the clock
        FPS = 200#Set the FPS to 200 initially 
        num = 0
        width = 1280
        Height = 800
        pygame.init()#initilise the font 
        Screen = pygame.display.set_mode((width,Height))#create the screen 
        pygame.display.set_caption('Solve the problem ')#Set the window title 
        def get_font(size):#Return the font
            return pygame.font.Font("FONTS/HACKED.ttf",size)
        run = True
        input_rect = pygame.Rect(600,350,80,80)#rectangle for input 
        color = pygame.Color('red')#Set the color
        text = ''#No text at first for the input field
        Question,Answer = self.generate_problem() #Get the question and answer
        while run:
            clock.tick(FPS)#Start the FPS 

            position = pygame.mouse.get_pos()#get the mouse position 
            #Create the buttons using the actual button class
            SUBMIT_BUTTON = ActualButton(image=None, position=(640, 460),
                            text_input="SUBMIT", font=get_font(40), color_base="White", hovering_color="Green")
            Question_text = get_font(80).render(f"{Question}", True, "White")
            Question_Rect = Question_text.get_rect(center=(640, 260))
            mins, secs = divmod(self.t, 60) #seperate the minuted and seconds 
            timer_text = get_font(50).render('{:02d}:{:02d}'.format(mins, secs),True,"White") #Display the timer text 
            time.sleep(1) #Sleep for 1 second 
            self.t -= 1 #Remove the second
            timer_rect  = timer_text.get_rect(center=(1200, 260)) #Create the rect 
                       
            for event in pygame.event.get():#Check for any event 
                if event.type ==pygame.QUIT:# Check if event is quit
                    pygame.quit()#Then quit pygame 
                if event.type == pygame.KEYDOWN:#If event is keydown 
                    
                    if event.key == pygame.K_BACKSPACE:#If backspace key pressed 
                       
                        text =text[:-1]#Then remove the last word 
                    else:
                        text+=event.unicode#else write the text 
                        p = text.isalpha() #if the text is alphabetic boolean 
                        if p:  #if p is true 
                            text = '' #then set text to empty 
                    if event.key == pygame.K_RETURN:#if return key pressed 
                        run =False#Go to options window 
                        
                if event.type == pygame.MOUSEBUTTONDOWN:#Check if mouse key got pressed 
                    if SUBMIT_BUTTON.checkForInput(event.pos):#if submit button pressed 
                        run =False
                
                
                
            Screen.fill((0,0,0))#Fill the screen black 
            #Creating the text and displaying the text on the screen 
            Text = get_font(50).render('Solve the Problem',True, "#b68f40")
            text_rect = Text.get_rect(center=(640,100))
            Screen.blit(Text,text_rect)
            pygame.draw.rect(Screen,color,input_rect)
            text_surface = get_font(60).render(text,True,(255,255,255))
            Screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
            input_rect.w = max(80,text_surface.get_width()+10)
            Screen.blit(Question_text,Question_Rect)
            Screen.blit(timer_text,timer_rect)
            SUBMIT_BUTTON.changeColor(position)#change the color when hovering over the button 
            SUBMIT_BUTTON.update(Screen)#Updates the screen 
            
            pygame.display.update()#Update the pygame window 
            if self.t == 0: #if time is 0 
                self.t = 10 #Reset the time
                with open('Text_files/high.txt','w') as w: #Open the file and remove 1 score 
                    xx= int(line)-1
                    w.write(str(xx))
                self.problem_win() #Play the window again
            
        try: #try this 
            
            text = text.split()[0]  #Split the text 
            if int(text)!=int(Answer): #If the answer is not right then reduce the score 
                with open('Text_files/high.txt','r') as f :
                    line = f.read()
                with open('Text_files/high.txt','w') as w:
                    xx= int(line)-1
                    w.write(str(xx))
                

            else :#If the answer is  right then increase the score 
                with open('Text_files/high.txt','r') as f :
                    line = f.read()
                with open('Text_files/high.txt','w') as w:
                    xx= int(line)+1
                    w.write(str(xx))
           
                run= False #Break the while loop 
                return True #Return true 
        except: # if there is no answer then 
            #Open the files and reduce the score 
            with open('Text_files/high.txt','r') as f :
                    line = f.read()
            with open('Text_files/high.txt','w') as w:
                xx= int(line)-1
                w.write(str(xx))
            
            return False #Return false 
