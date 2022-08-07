from pygame import mixer
import os
import random
import csv,time
from textbutton import TextButton
from actualbutton import ActualButton
from Problem import problemMath
import pygame

global screen_height,screen_width #Create global variables

pygame.init() #Start the pygame
screen_width  = 1280 #The width for the window 
screen_height = 800 #The height for the window 
class Main:
    	
	pygame.font.init() #initilise the font 
	pygame.init()  #Start the pygame 
	buttonn = pygame.Rect(1200, 750, 50, 150) #Creates a rectangle
	get_font  =pygame.font.Font("FONTS/Sectar.ttf", 60)  #Gets the font 
	randomnum  = random.randint(1, 3)  #Creates a random number between 1 and 3 
	Background = pygame.image.load(f"assets/{randomnum}.jpg")  #loads the background image
	Background = pygame.transform.scale(Background,(screen_width,screen_height))  #transform the image

	global img,music_paused,STOP_MUSIC,Play_music # Set the varible to global top make it easier to access them 
 
	#Load the images and transform them to scale that would make them reusable 
	img  = pygame.image.load('assets/music1.png') 
	img  = pygame.transform.scale(img,(int(img.get_width()*0.2),int(img.get_height() * 0.2)))
	Play_music = pygame.image.load('assets/music1.png')
	Play_music  = pygame.transform.scale(Play_music,(int(Play_music.get_width()*0.2),int(Play_music.get_height() * 0.2)))
	img_rect = img.get_rect()
	xx = TextButton(1200,750,img,0.2)  #create a an object from text button class
	STOP_MUSIC = pygame.image.load('assets/Musicstop.png')
	STOP_MUSIC  = pygame.transform.scale(STOP_MUSIC,(int(STOP_MUSIC.get_width()*0.2),int(STOP_MUSIC.get_height() * 0.2)))
	xp = TextButton(1200,750,STOP_MUSIC,0.2)

	global music_paused #Create a global music variabel to control the music 
	
	music_paused = False

	get_font  =pygame.font.Font("FONTS/Sectar.ttf", 60)  #Load the font 
	def FPS_win():  #Creates a FPS window for changing the FPS
		FPS_CLOCK = pygame.time.Clock()  #Start the clock
		FPS = 60  #Set the FPS to 60 initially 
		pygame.init()#Start the pygame 
		Screen = pygame.display.set_mode((screen_width,screen_height)) #create the screen 
		pygame.display.set_caption('Settings')#Set the window title 
		def get_font(size): #Return the font 
			return pygame.font.Font("FONTS/HACKED.ttf",size)
		Play = True #Variable to True 
		input_rect = pygame.Rect(600,350,80,80) #rectangle for input 
		color = pygame.Color('blue') #Set the color to blue 
		text = '' #No text at first for the input field
		
		
		while Play:
			FPS_CLOCK.tick(FPS) #Start the FPS 

			position = pygame.mouse.get_pos() #get the mouse position 
			#Create the buttons using the actual button class
			DONE = ActualButton(image=None, position=(640, 460),
							text_input="DONE", font=get_font(40), color_base="White", hovering_color="Green")
			
			BACK = ActualButton(image=None, position=(640, 650),
									text_input="BACK", font=get_font(40), color_base="Red", hovering_color="Green")
		
			Screen.fill((0,0,0))#Fill the screen black 
			Text = get_font(50).render('Enter the FPS(40-240)',True, "#b68f40") #Get the text 
			text_rect = Text.get_rect(center=(640,100))#Get a rectangle for the text 
			Screen.blit(Text,text_rect) #display the text 
			Text1 = get_font(20).render('Please Only input Numbers ',True, "Red") #Warning for the user 
			text_rect1 = Text1.get_rect(center=(640,50)) #Get a rectangle for the text 
			Screen.blit(Text1,text_rect1)#display the text 
			BACK.changeColor(position) #change the color when hovering over the button 
			BACK.update(Screen)	#Updates the screen 
			pygame.draw.rect(Screen,color,input_rect) #Draw the rectangle for the input  
			text_surface = get_font(60).render(text,True,(255,255,255)) #Get the font 
			Screen.blit(text_surface,(input_rect.x+5,input_rect.y+5)) #Display the text and 
			input_rect.w = max(80,text_surface.get_width()+10)#increase the input field accoring to user input by increasing the width
			DONE.changeColor(position) #change the color when hovering over the button 
			DONE.update(Screen)#Updates the screen 
			
			T = open('Text_files/FPS.txt','w') #Open the FPS file 
			T.write(text) #Write the text to it
			for event in pygame.event.get(): #Check for any event 
				if event.type ==pygame.QUIT: # Check if event is quit
					pygame.quit() #Then quit pygame 
				if event.type == pygame.KEYDOWN:#If event is keydown 
					if event.key == pygame.K_ESCAPE: #if event is escape 
						Main.options() #Then go to options window 
						
					if event.key == pygame.K_BACKSPACE: #If backspace key pressed 
						
						text =text[:-1] #Then remove the last word 
					else:
						text+=event.unicode #else write the text 
						p = text.isalpha() #if the text is alphabetic boolean 
						if p:  #if p is true 
							text = '' #then set text to empty 

					if event.key == pygame.K_RETURN: #if return key pressed 
						Main.options() #Go to options window 
						
				if event.type == pygame.MOUSEBUTTONDOWN: #Check if mouse key got pressed 
					if DONE.checkForInput(event.pos): #if done button pressed 
						
						Main.options() #go to opeitons window 
					if BACK.checkForInput(position): # if the back button got pressed 
						Main.options()#go to opeitons window 
				
				
			
			pygame.display.update()  #Update the pygame window 
	def character_type():
		pygame.quit()
		pygame.init()#Start the pygame 
		screen = pygame.display.set_mode((screen_width,screen_height))#create the screen 
		screen.fill("black")#Fill the screen black 
		get_font  =pygame.font.Font("FONTS/HACKED.ttf", 40) #Load the font 
		Play =True#Variable to True
		with open('Text_files/info.txt','w') as xx: #Open the file in write mode
			
			while Play:
				OPTIONS_TEXT = get_font.render("Click on the Character You Want", True, "Red") #create the option text 
				
				OPTIONS_MOUSE_POS = pygame.mouse.get_pos() #get the mouse position
				#Create the buttons 
				OPTIONS_TYPE = ActualButton(image=None, position=(640, 360),
									text_input="Girl", font=get_font, color_base="White", hovering_color="Green") 
				OPTIONS_TYPE.changeColor(OPTIONS_MOUSE_POS)
				OPTIONS_TYPE.update(screen)
				OPTIONS_TYPE2 = ActualButton(image=None, position=(640, 500),
									text_input="Boy", font=get_font, color_base="White", hovering_color="Green")
				OPTIONS_TYPE2.changeColor(OPTIONS_MOUSE_POS)
				OPTIONS_TYPE2.update(screen)
				OPTIONS_BACK = ActualButton(image=None, position=(640, 650),
									text_input="BACK", font=get_font, color_base="Red", hovering_color="Green")
				OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 160))
				screen.blit(OPTIONS_TEXT, OPTIONS_RECT) #Display the text 
				OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS) #Change the color when hovering over the button 
				OPTIONS_BACK.update(screen) #update the button 

				for event in pygame.event.get():#Check for any event 
					if event.type == pygame.QUIT:# Check if event is quit
						Play =False#Then quit pygame 
					if event.type == pygame.MOUSEBUTTONDOWN:#Check if mouse key got pressed 
						if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):# if the back button got pressed 
							Main.options()#go to options window 
						if OPTIONS_TYPE.checkForInput(OPTIONS_MOUSE_POS):#if OPTION1 button pressed 
							xx.write('Girl') #write girl to the text file 
							time.sleep(2) #wait for 2 seconds 
							Main.options() #Go to the options window 
						if OPTIONS_TYPE2.checkForInput(OPTIONS_MOUSE_POS):#if OPTION1 button pressed 
							xx.write('Men')#write men to the text file 
							time.sleep(2)#wait for 2 seconds 
							Main.options()#Go to the options window 
				
				pygame.display.update()#Update the pygame window 
			pygame.quit()
	def pause(Name):
		pygame.init()# initialising the pygame 
		
		buttonn = pygame.Rect(1200, 750, 50, 150) #Create a button 
		get_font  =pygame.font.Font("FONTS/Sectar.ttf", 60) #get the font 
		screen = pygame.display.set_mode((screen_width, screen_height)) #create the screen 
		pygame.display.set_caption('PAUSED') #create caption 
		not_paused = True #Variable
		while not_paused: #Run the loop
			global img 
			pos = pygame.mouse.get_pos() #get the mouse position 
			img = pygame.image.load('/Users/avishekhimanshu/Desktop/NinjaGame/assets/pause.jpg')#Load the image 
			img  = pygame.transform.scale(img,(1280,800))#Transform the image
			pp = pygame.draw.rect(screen, "white", buttonn) #Create a rect around the image
			screen.blit(img,(0,0)) #Display the image at the background 
			MENU_TEXT =  get_font.render(f" {Name} ", True, "#b68f40") #Set the name of the window 
			MENU_RECT = MENU_TEXT.get_rect(center=(640, 100)) #Create a rect around it 
			#create buttons 
			CONTINUE = ActualButton(image=pygame.image.load("assets/Play Rect.png"), position=(640, 250),
									text_input="Continue", font=  get_font, color_base="#000000", hovering_color="green") 
			RESTART = ActualButton(image=pygame.image.load("assets/Options Rect.png"), position=(640, 400),
									text_input="Restart", font=  get_font, color_base="#000000", hovering_color="green")
			MAIN_BUTTON = ActualButton(image=pygame.image.load("assets/Options Rect.png"), position=(640, 550),
									text_input="Main Menu", font=  get_font, color_base="#000000", hovering_color="green")
			QUIT_BUTTON = ActualButton(image=pygame.image.load("assets/Options Rect.png"), position=(640, 700),
									text_input="Quit", font=  get_font, color_base="#000000", hovering_color="green")
			get_fontt  =pygame.font.Font("FONTS/Sectar.ttf", 25) #Get fonts 
			xx = open('Text_files/high.txt','r') #Open the score file 
			high_text =   get_fontt.render(f'HIGHSCORE:{xx.read()}',True,"white") #Render the score 
			high_rect = high_text.get_rect(center=(1100,100)) #Create a rect around the text 
			
			screen.blit(MENU_TEXT, MENU_RECT) # Display the title 
			screen.blit(high_text,high_rect) #display the high score 
			for button in [CONTINUE, RESTART,MAIN_BUTTON,QUIT_BUTTON]: #Loop through every button
				button.changeColor(pos) #Hovering color change
				button.update(screen) #Update the screen 

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					not_paused = False
				
				if event.type == pygame.MOUSEBUTTONDOWN: 
					
					if CONTINUE.checkForInput(pos):#If continue got pressed 
						not_paused =False #Stop the while loop 
					if RESTART.checkForInput(pos):   #If restart got pressed 
						play() #Then Play the function again
					if MAIN_BUTTON.checkForInput(pos): #If main menu got pressed 
						Main.main_menu() #Go to main menu
				 
					if QUIT_BUTTON.checkForInput(pos): #If quit got pressed 
				
						pygame.quit() #Quit pygame
						
						
						
			
			pygame.display.update()		
	def guide( ):
		pygame.init()#Start the pygame 
		screen = pygame.display.set_mode((screen_width, screen_height))#create the screen 
		pygame.display.set_caption('GUIDE')#Set the title to GUIDE
		screen.fill('white')#Fill the screen white 
		get_font  =pygame.font.Font("FONTS/HACKED.ttf", 40)#Load the font 
		Play =True
		key_img = pygame.image.load('keys.png') #Load the key png
		key_img = pygame.transform.scale(key_img, (key_img.get_width()*0.5,key_img.get_height()*0.5)) #Transform the key img
		while Play:
			
			
			PLAY_MOUSE_POS = pygame.mouse.get_pos() #get the mouse position
			screen.blit(key_img, (850,110)) #Displaying the image of keys 

			Guide_TEXT = get_font.render("Use Arrow Keys to Run the Ninja", True, "black") #Text 1
			Guide_TEXT2 = get_font.render("Kill The Enemies using your Maths and gain power ", True, "black")#Text 2
			Guide_TEXT3 = get_font.render("Try kill the every Wizard to get more stars ", True, "black")#Text 3
			Guide_RECT = Guide_TEXT.get_rect(center=(600, 200)) #RECT 1
			Guide_RECT2 = Guide_TEXT.get_rect(center=(520, 350))#RECT 2
			Guide_RECT3 = Guide_TEXT.get_rect(center=(600, 500))#RECT 3
			screen.blit(Guide_TEXT,Guide_RECT) #Display the text 
			screen.blit(Guide_TEXT2,Guide_RECT2)#Display the text 
			screen.blit(Guide_TEXT3,Guide_RECT3)#Display the text 

			Guide_BACK = ActualButton(image=None, position=(640, 700), #Create the button 
							text_input="BACK", font=get_font, color_base="black", hovering_color="Green")

			Guide_BACK.changeColor(PLAY_MOUSE_POS) #when hover change the color
			Guide_BACK.update(screen) #Update the button
			for event in pygame.event.get():#Check for any event 
				if event.type == pygame.QUIT:# Check if event is quit
					Play = False#Then quit pygame 
				if event.type == pygame.MOUSEBUTTONDOWN:
					if Guide_BACK.checkForInput (PLAY_MOUSE_POS): #if back button got pressed 
					
						Main.main_menu()  #Go to the main menu 


			pygame.display.update() #Update the pyagme window 
		pygame.quit()
	def options( ):
		
		pygame.init()# initialising the pygame 
		pygame.display.set_caption('Settings')#create caption 
		screen = pygame.display.set_mode((screen_width,screen_height))#create the screen 
		screen.fill("black")#Fill the screen black 
		get_font  =pygame.font.Font("FONTS/HACKED.ttf", 50)#Load the font
		Play =True#Variable to True
		while Play:
			
			OPTIONS_MOUSE_POS = pygame.mouse.get_pos()#get the mouse position
			
			get_font  =pygame.font.Font("FONTS/HACKED.ttf", 70)
			#Create the buttons 
			OPTIONS_TYPE = ActualButton(image=None, position=(640, 250),
								text_input="Choose Character", font=get_font, color_base="white", hovering_color="Green")
			OPTIONS_TYPE2 = ActualButton(image=None, position=(640, 400),
								text_input="FPS", font=get_font, color_base="white", hovering_color="Green")
			OPTIONS_TYPE3 = ActualButton(image=None, position=(640, 550),
								text_input="RESET", font=get_font, color_base="white", hovering_color="Green")
			OPTIONS_TYPE2.changeColor(OPTIONS_MOUSE_POS)#Change the color when hovering over the button 
			OPTIONS_TYPE2.update(screen)#update the button 
			OPTIONS_TYPE3.changeColor(OPTIONS_MOUSE_POS)#Change the color when hovering over the button 
			OPTIONS_TYPE3.update(screen)#update the button 
			OPTIONS_TYPE.changeColor(OPTIONS_MOUSE_POS)#Change the color when hovering over the button 
			OPTIONS_TYPE.update(screen)#update the button 
			get_font  =pygame.font.Font("FONTS/HACKED.ttf", 40)
			OPTIONS_TEXT2 = get_font.render("Please Restart after changing", True, "Red")#create the option text 

			OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 60))

			screen.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
			get_font  =pygame.font.Font("FONTS/HACKED.ttf", 40)
			OPTIONS_BACK = ActualButton(image=None, position=(640, 700),
								text_input="BACK", font=get_font, color_base="white", hovering_color="Green")

			OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)#Change the color when hovering over the button
			OPTIONS_BACK.update(screen)#update the button 

			for event in pygame.event.get():#Check for any event 
				if event.type == pygame.QUIT:# Check if event is quit
					Play=False#Then quit pygame 
				if event.type == pygame.MOUSEBUTTONDOWN:
					if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):#Check if the back button got pressed 
						Main.main_menu() #Go to main menu
					if OPTIONS_TYPE.checkForInput(OPTIONS_MOUSE_POS): #Check if the charactertype button got pressed 
    					 Main.character_type() #Go to the character type window 
					
					if OPTIONS_TYPE2.checkForInput(OPTIONS_MOUSE_POS): #Check if the FPS button got pressed 
    					 Main.FPS_win()#Go to the FPS  window
					if OPTIONS_TYPE3.checkForInput(OPTIONS_MOUSE_POS): #iF RESET BUTTON GOT PRESSED 
						#Set everything to default
						coin = open('Text_files/Coin.txt','w')
						coin.write('0') 
						score = open('Text_files/high.txt','w')
						score.write('0')
						
						
			pygame.display.update()#Update the pygame window 
		pygame.quit()
	def main_menu():
		mixer.init()#Initialise the mixer 
		buttonn = pygame.Rect(1200, 750, 50, 150)#Creates a rectangle

		randomnum  = random.randint(1, 3)#Creates a random number between 1 and 3 
		Background = pygame.image.load(f"assets/{randomnum}.jpg")#loads the background image
		Background = pygame.transform.scale(Background,(1280,800))#transform the image
		Play = True

		pygame.init() #Start the pygame 
		screen = pygame.display.set_mode((screen_width, screen_height))#create the screen 
		pygame.display.set_caption('NINJA')#Set the window title 
		
		pygame.mixer.music.load('assets/Ninja.mp3')#Load the music 
		pygame.mixer.music.set_volume(0.12)#Set the volume 
		pygame.mixer.music.play(-1) #Play it infinite 
		#Load the images and transform them to scale that would make them reusable 
		img  = pygame.image.load('assets/music1.png')
		img  = pygame.transform.scale(img,(int(img.get_width()*0.2),int(img.get_height() * 0.2)))
		while Play:
			global music_paused
			
			screen.blit(Background, (0, 0)) #Display the image at the background 
			pos = pygame.mouse.get_pos()#Get the mouse position 
			
			pp = pygame.draw.rect(screen, "white", buttonn) #Draw the rectangle 
			screen.blit(img,(1200,750)) #Show the image 
			get_font  =pygame.font.Font("FONTS/Sectar.ttf", 60)#Get the font 
			MENU_TEXT = get_font.render("NINJA", True, "#b68f40")#Get the text 
			MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))#Get the rect
			#Create the buttons 
			PLAY_BUTTON = ActualButton(image=pygame.image.load("assets/Play Rect.png"), position=(640, 250),
									text_input="PLAY", font=  get_font, color_base="#000000", hovering_color="White")
			OPTIONS_BUTTON = ActualButton(image=pygame.image.load("assets/Options Rect.png"), position=(640, 400),
									text_input="SETTINGS", font=  get_font, color_base="#000000", hovering_color="White")
			GUIDE_BUTTON = ActualButton(image=pygame.image.load("assets/Options Rect.png"), position=(640, 550),
									text_input="GUIDE", font=  get_font, color_base="#000000", hovering_color="White")
			QUIT_BUTTON = ActualButton(image=pygame.image.load("assets/Quit Rect.png"), position=(640, 700),
									text_input="QUIT", font=  get_font, color_base="#000000", hovering_color="White")
			get_fontt  =pygame.font.Font("FONTS/HACKED.ttf", 30)
			xx = open('Text_files/high.txt','r') #Get the highscore 

			high_text =   get_fontt.render(f'HIGHSCORE:{xx.read()}',True,"white") #Render the score 
			high_rect = high_text.get_rect(center=(1100,100)) #Create a rectangle
			#Display the text and the images 
			screen.blit(MENU_TEXT, MENU_RECT) 
			screen.blit(high_text,high_rect)
			for button in [PLAY_BUTTON, OPTIONS_BUTTON,GUIDE_BUTTON, QUIT_BUTTON]: #Loop through every button 
				button.changeColor(pos) # Change the color when hovered 
				button.update(screen) #Update the button 

			for event in pygame.event.get():#Check for any event 
				if event.type == pygame.QUIT:# Check if event is quit
					
					Play=False#Then quit pygame 
				if event.type == pygame.KEYDOWN:#If event is keydown 
					if event.key == pygame.K_ESCAPE:#if event is escape 
						Play=False#Then quit pygame 
					if event.key == pygame.K_m: #If key is M 
						pygame.mixer.music.fadeout(1000) #Pause the music for sometime 
				if event.type == pygame.MOUSEBUTTONDOWN: #Check if mouse key got pressed 
					
					if PLAY_BUTTON.checkForInput(pos):#if Play button pressed 
						play() #Then call the function Play
					if OPTIONS_BUTTON.checkForInput(pos):#if Options button pressed 
						Main.options() #Then call the function options
					if GUIDE_BUTTON.checkForInput(pos):#if Guide button pressed 
						Main.guide() #Then call the function guide
       
					if buttonn.collidepoint(event.pos): #If the mouse collides with the music button 
						if pygame.mouse.get_pressed()[0]==1: #if pressed 

							music_paused = not music_paused #Set the opposite to the music variable
							if music_paused: #If the music is paused is True
								pygame.mixer.music.pause() #Then pause the music 
								img = STOP_MUSIC #Change the image to stop 
								
							else: 
								pygame.mixer.music.unpause() #Unpause the music 
								img = Play_music #Set the image to play 

					if QUIT_BUTTON.checkForInput(pos):#If quit button got pressed 
						Play=False #Quit the pygame 
						
						

			pygame.display.update()
		pygame.quit()
def play():
	pygame.quit() #Quits any previous pygame
	pygame.init() #starts the pygame again
	screen = pygame.display.set_mode((screen_width, screen_height)) #Set the window mode
	pygame.display.set_caption('Ninja') #Set the window title 
	global current_level #Set the variable of level to global 
	current_level = 1 #The current level the player is on 
	FPS_CLOCK = pygame.time.Clock() #Start the clock
	F = open('Text_files/FPS.txt','r') #oPEN fps file
	kunai_img,potion_img,coin_img,Kunai_box_img = chest_images() #Get all the chest images 
	texture_img,trees_color_img,tree_img,tree_shadow_img = background_images() # Get all the background images
	font = 	pygame.font.Font("FONTS/Sectar.ttf", 20) #The font
	global scroll #Set the scroll to global variable
	scroll = int('0') #The scroll to 0 
	background_scroll = int('0') #Background scroll to 0 
	Moving_scroll = 200 #How fast the screen will be moving 
	block_type = len(os.listdir('assets/block/'))-1 #How many blocks there are 
	full_level = open('Text_files/level.txt','r').read() # Total number of levels
	Grav = float('0.55') #Set the gravity to 0.55
	m_left,m_right,throw_kunai,Attacking = boolean_variable() #Get all the boolean variables
	info = open('Text_files/blocksinfo.txt','r').read() #Read the ros and columns file
	info = info.split(',') #Split it 
	row = int(info[0]) #The first one is row 
	col = int(info[1])#second one is column 
	block_size = 50 #This is the size of each block 
	# if int(F) == ' ' or ''  : #Check if the FPS is None or empty 
    # 		FPS = 45 #Set the FPS to 45 
	# else:
	FPS = int(F.read()) #Set it to the deafult one
  
	Background = (0, 201, 120) #The background color 
	R = (255, 200, 0) #Yellow color

	
	

	def block_load(): #This loads the blocks in a list 
		block_list = []
		for x in range(block_type): #Loop through the range of blocks 
			block = pygame.image.load(f'assets/block/{x}.png') #Load the image
			block = pygame.transform.scale(block, (block_size, block_size))#Transform it 
			block_list.append(block) #Append it to the list 
		return block_list #Return the list 
	def set_update(): #Updates all the sets 
		KunaiSet.update()
		ChestSet.update()
		DecorationSet.update()
		waterSet.update()
		exitSet.update()
		KunaiSet.draw(screen)
		ChestSet.draw(screen)
		DecorationSet.draw(screen)
		waterSet.draw(screen)
		exitSet.draw(screen)
	def display_background(): #Shows the background in order with all the layers
		img_width = texture_img.get_width() #Get the image width 
		for x in range(40): #Loop for 40 iterations
			screen.blit(texture_img, ((x * img_width) - background_scroll * 0.4, 0))# Display the image and scroll it as the background scrolls
			screen.blit(trees_color_img, ((x * img_width) - background_scroll * 0.5, 0))# Display the image and scroll it as the background scrolls
			screen.blit(tree_img, ((x * img_width) - background_scroll * 0.6, 0))# Display the image and scroll it as the background scrolls
			screen.blit(tree_shadow_img, ((x * img_width) - background_scroll * 0.6, 0))# Display the image and scroll it as the background scrolls
	class Character(pygame.sprite.Sprite): #Creates the character 
		def __init__(self,  X_axis, Y_axis, run_sped, kunai,character): #Constructor for the classes 
			pygame.sprite.Sprite.__init__(self) #Inherit the functionality from pygame sprite class 
			self.coins = int(open('Text_files/Coin.txt','r').read()) # Gets the coins from the coin module
			self.time_sync = pygame.time.get_ticks() #Create a clock 
			self.Moveto = 0 #Create a moving counter 
			self.FindNinja = pygame.Rect(0, 0, 160, 30) #This willl allow to identify the enemy nearby
			self.is_in_idle = False #Bool for idle state
			self.is_idle_counter = 0 #For how long in idle
			self.breathing = True #Checks if the player is still alive 
			self.character = character# Character to character
			self.run_sped = run_sped #Gets the speed for running
			self.kunai = kunai #The number of kunai's
			self.time_kunai = 0 #Time the kunai in air 
			self.power = 0+100 #The initial power
			self.full_power = 100 #The max power the charcter can have 
			self.dir = 0 #The direction the player is in 
			self.velocity_Y = 0 #This will be used for jumping of the player 
			self.isJumping = False #checks if the player is jumping 
			self.isIn_Air = False #checks if he is in air 
			self.flip = False #Allows to flip the player around 
			self.Sprites = [] #Holds the sprite animations 
			self.current_frame = 0 #Tells which frame the character is on 
			self.Current_action = 0 #Checks the current action 
			
			sprites_num = ['Idle', 'Run', 'Jump', 'Dead','Throw','Jump_Throw'] #All of the sprite animations 
			if self.character =='Wizard': #If the sprite is wizard 
				sprites_num = ['Idle', 'Run', 'Attack','Dead'] #then the sprite animantioin is following 
			
			
			
			
			for sprite in sprites_num: #Loop through the sprite animantion
				sprite_list = [] #Empty list 
				numbers_of_sprites = len(os.listdir(f'{self.character}/{sprite}')) #Tells the niumber of sprites 
				for i in range(numbers_of_sprites-1): #Loops through the sprites 
					if self.character == 'Wizard': #if the type is wizard 
						img = pygame.image.load(f'{self.character}/{sprite}/{sprite}__00{i}.png').convert_alpha() #then load the image
						img = pygame.transform.scale(img, (int(img.get_width()*1.5 ), int(img.get_height()*1.5 )))# Transform the image
						sprite_list.append(img) #Append that image to the list 
						
					else:# If the character is not wizard 
						img = pygame.image.load(f'{self.character}/{sprite}/{sprite}__00{i}.png').convert_alpha()#then load the image
						img = pygame.transform.scale(img, (int(img.get_width() * 0.2), int(img.get_height() * 0.2)))# Transform the image
						sprite_list.append(img)#Append that image to the list 
				self.Sprites.append(sprite_list) #This appends the whole list into the sprite list making it 2d 

			self.sprite_img = self.Sprites[self.Current_action][self.current_frame] #Gets the image from the 2d array using current action
			self.rect = self.sprite_img.get_rect() #Create the Rectangle
			self.rect.inflate_ip(-20, 0)#Increase the size of the rect 
			self.rect.center = (X_axis, Y_axis) #Make the center of the image as X and y
			self.sprite_wid = self.sprite_img.get_width() #Get the width 
			self.sprite_hei = self.sprite_img.get_height() #Get the height
		def zero(self):
			if pygame.sprite.spritecollide(self, waterSet, False): #Check if the player has collided with the water 
				self.power = 0 #set the power to 0 
			if self.rect.bottom > screen_height: #Check if the player has gone out of screen 
					self.power = 0 #then power to 0 	
		def is_breathing(self): #Checks if the player is alive
				if self.power <= 0: # If the health is 0
					self.power = 0 #Then set the power to zero 
					self.run_sped = 0 #The player can't run 
					self.breathing = False #The character breathing to false
					self.nextAction(3) #Update the death action 
    
		def syncAnimation(self): #This makes the sprite animation set back 
			COOL = 100 #A clock type for telling how many sprites were executed 
			self.sprite_img = self.Sprites[self.Current_action][self.current_frame] #current sprite image 
			if pygame.time.get_ticks() - self.time_sync > COOL:# Checks if the time is greater than 100 
				self.time_sync = pygame.time.get_ticks() #Then reset 
				self.current_frame += 1 #Add one to the frame
			if self.current_frame >= len(self.Sprites[self.Current_action]): #If the current frame is greater than the length of the current action 
				if self.Current_action == 3: #If the action is 3 
					self.current_frame = len(self.Sprites[self.Current_action]) - 1 #Then the current frame is len of action 
				else:
					self.current_frame = 0 #Else the current frame is set to default
		def throw_kunai(self): #This allows the player to throw the kunai 
			if self.time_kunai == 0 and self.kunai > 0: #Checks if the kunai is grater than 0 
				self.time_kunai = 30 # Then increase the time for the kunai 
				kunai = Kunai(self.rect.centerx + (0.75 * self.rect.size[0] * self.dir), self.rect.centery, self.dir) #Create an object 
				KunaiSet.add(kunai) #Add object to the set 
				self.kunai -= 1 #Remove kunai from total kunai's
		def Run(self, m_left, m_right): #Run fuction
			scroll=int('0') #Set the scroll to 0 
			direction_x = 0 #Set the x direction to 0 
			direction_y = 0#Set the y direction to 0 

			if m_right: #Check if moving right is true
				self.dir = 1 #Then direction is 1 
				direction_x = self.run_sped #Add the speed to x axis
				self.flip = False #Flip is false
				 
			if m_left:#Check if moving left is true
				self.dir = -1 #Then direction is -1 
				direction_x = -self.run_sped#subtract the speed to x axis
				self.flip = True #Flip is True
				
			
			if self.isJumping == True and self.isIn_Air == False: #Checks if jumping is true
				self.velocity_Y = -12 # then the velocity y-12 which will make character go up 
				self.isJumping = False #Set the jumping to false
				self.isIn_Air = True #In air to true 
				isJumping = pygame.mixer.Sound('Music/jump.wav') #Load the soound 
				isJumping.set_volume(0.2) #Set the volume
				isJumping.play() #Play the sound 
				

			self.velocity_Y += Grav #Add the gravity after in air to make the player go down 
			if self.velocity_Y > 20: #Checks if the velocity is greater than 20 
				self.velocity_Y #set to default
			direction_y += self.velocity_Y #ADD it to the y direction to land the player on the ground 
			

			
			for block in game.hurdle_lis: #Loop through the hurdles 
				if block[1].colliderect(direction_x +self.rect.x , self.rect.y, self.sprite_wid, self.sprite_hei): #Check for collision with the block 
					direction_x = 0#If so then x direction is 0 
					if self.character == 'Wizard': #If the character is wizard 
						self.dir *= -1 #Move in the left direction 
						self.Moveto = 0# Go to startign position 
				if block[1].colliderect(self.rect.x, (direction_y+ self.rect.y ),self.sprite_wid, self.sprite_hei):#Check for collision with the block 
					if self.velocity_Y < 0: # If velocity is less than zero 
						self.velocity_Y = 0 #Set it to zero 
						direction_y = block[1].bottom - self.rect.top #Move in the direction by subtracting
					elif self.velocity_Y >= 0: #if greater than or equal to 0 
						self.velocity_Y = 0 #Set to defaut
						self.isIn_Air = False #And the player is not in Air 
						direction_y = block[1].top - self.rect.bottom #Move the player towartds the block 

			self.zero() #Check the colision with objects and set the health to zero 

			type_ = open('Text_files/info.txt','r').read() #Read the type of player in the text file 
			if self.character == type_: #If the character type if in the file 
				if self.rect.left + direction_x < 0 or self.rect.right + direction_x > screen_width:#Check if the user has gone out of boundary 
					direction_x = 0 #Sets the x axis back to 0 

			self.rect.x += direction_x #Add the direction x to rectangle x 
			self.rect.y += direction_y  #Add the direction y to rectangle y

			if self.character == type_:  # Checks if the type if character 
				if (self.rect.right > screen_width - Moving_scroll and background_scroll < (game.level_length * block_size) - screen_width)\
					or (self.rect.left < Moving_scroll and background_scroll > abs(direction_x)): # Makes the scroll based on the players position and 
					self.rect.x -= direction_x #Then move the rect by direction in opposite way
					scroll = -direction_x#Then subtract the direction x from scroll 

			return scroll  #Return the scroll 

		def handle_AI(self): #This makes the AI 
			if self.breathing and Ninja.breathing: #Checks if the chacters are breathing 
				if self.is_in_idle == False and random.randint(1, 155) == 1: # Then create a random num and check whether is == 1 
					self.nextAction(0) #If so then get to the next action 
					self.is_in_idle = True #And the movement of the AI is now idling 
					self.is_idle_counter = 40 #The idle for 40 
				if self.FindNinja.colliderect(Ninja.rect): #Checks if the rectangla has collides with player 
					self.nextAction(0) #Get to the next action 
					self.nextAction(2)#Get to the next action 
					self.throw_kunai() #Throw the kunai at the player 
				else: #Otherwise 
					if self.is_in_idle == False: #check if the enemy is not stationary
						if self.dir == 1: #set the direction to 1 
							aiM_right = True #the enemy is now moving right 
						else: #otherwise 
							aiM_right = False #The enemy is now not moving right 
						aiM_left = not aiM_right #Set the variable to opposite 
						self.Run(aiM_left, aiM_right) #Run the player base on that 
						self.nextAction(1) #Make the animatio to run 
						self.Moveto += 1 #Add 1 to the movement 
						
						self.FindNinja.center = (self.rect.centerx + 65 * self.dir, self.rect.centery) #Finds the rectangel center

						if self.Moveto > block_size:#Check if the enemy has gone out the block size 
							self.dir *= -1 #Move into other direction 
							self.Moveto *= -1 #Make the movement in negative direction 
					else:
						self.is_idle_counter -= 1 #Otherwise wait there 
						if self.is_idle_counter <= 0: # If the idle state is less than or 0 
							self.is_in_idle = False #Then the enemy is not idling 

			self.rect.x += scroll #Move the screen along with the player 

		def nextAction(self, next_action): #This function gets the next action 
			if next_action != self.Current_action: #Checks if teh current action is new 
				self.Current_action = next_action # Then replace the current action with the new action 
				self.current_frame = 0 #Set the frame to default
				self.time_sync = pygame.time.get_ticks() #Reset the time 

		def update(self): #updates the functions
			self.syncAnimation() #This updates sync funtion
			self.is_breathing() #This calls the is breathing funtion
			if self.time_kunai > 0: #Checks if the timekunai is greater than 0 
				self.time_kunai -= 1 #Then remove one kunai 
		def Sprite_Blit(self): #This displays the character 
			screen.blit(pygame.transform.flip(self.sprite_img, self.flip, False), self.rect) #This displays the charcter on the screen 
	class Game():
		def levelData(self, csv_data): #Create a function for getting the data on the screen 
			self.hurdle_lis = [] #Create an empty list for storing the blocks 
			self.level_length = len(csv_data[0]) #Get the length of the csv 
			block_list = block_load() #Loads the data as a list 
			for y, row in enumerate(csv_data): #Loop through the csv data
				for x, block in enumerate(row): #loops throught the every block 
					if block >= 0: #Checks if the block is greater than or 0 
						block_img = block_list[block] #Then get the image 
						block_img_rect = block_img.get_rect() #create a rectangle 
						block_img_rect.x = x * block_size #Transform the x axis 
						block_img_rect.y = y * block_size#tranform the y axis 
						block_data = (block_img, block_img_rect) #This is the tuple for the rectangle and the image 
						if block >= 0 and block <= 8: #Check is it is greater than 0 and less than 8 
							self.hurdle_lis.append(block_data) #Then it is a hurdle and append it to the hurdle list 
						elif block >= 9 and block <= 10:#Check is it is greater than or equal to 9 and less than or equal to 10 
							Water_Object = Poisonious_water(block_img, x * block_size, y * block_size) #Then create a water object 
							waterSet.add(Water_Object) #Append it to the water set 
						elif block >= 11 and block <= 13:#Check is it is greater than or equal to 11 and less than or equal to 13
							Decoration_Object = decorate_world(block_img, x * block_size, y * block_size)#Then create a decorating object 
							DecorationSet.add(Decoration_Object)#Append it to the decoration set 
						elif block == 14: #If block is 14 
							Chest_object = ChestBox('Coin', x * block_size, y * block_size) #Then create a Chest object coin 
							ChestSet.add(Chest_object) #Add it to the set 
						elif block == 15:#If block is 15
							type_ = open('Text_files/info.txt','r') #Read the characetr file 
							Ninja = Character( x * block_size, y * block_size,7, 20,f'{type_.read()}') #Then create a Ninja
							powerBar = Power(10, 10, Ninja.power, Ninja.power) #Create the power bar 
						elif block == 16:
							Wizard = Character( x * block_size, y * block_size, 2, 20,'Wizard')#Then create a Wizard
							WizardSet.add(Wizard) #Add it to the wizard set 
						elif block == 17:
							Chest_object = ChestBox('Kunai', x * block_size, y * block_size)#Then create a Chest object Kunai 
							ChestSet.add(Chest_object)#Add it to the set 
		
						elif block == 19:
							Chest_object = ChestBox('Potion', x * block_size, y * block_size)#Then create a Chest object Potion 
							ChestSet.add(Chest_object)#Add it to the set 
						elif block == 20: #Check if the block is 20
							Exit_object = Next_Level(block_img, x * block_size, y * block_size)#Then create a exit object  
							exitSet.add(Exit_object) #Add it to the set 

			return Ninja, powerBar #Return the Ninja and the power Bar for changing and updating 


		def Draw_blocks(self):#This will draw all of the blocks 
			for block in self.hurdle_lis: #Loop throught all of the hurdles
				block[1][0] += scroll #Add the scroll to each one of them 
				screen.blit(block[0], block[1])	#Display them onto the screen 
	class decorate_world(pygame.sprite.Sprite):
		def __init__(self, dec_img, X_axis, y_axis): #Create a constructor
			pygame.sprite.Sprite.__init__(self) #Inherit from the pygame sprite class
			self.image = dec_img 
			self.rect = self.image.get_rect()
			self.rect.midtop = (X_axis + block_size // 2, y_axis + (block_size - self.image.get_height())) #This Gets the middle 
			#top part for teh collision 

		def update(self): #update the decorating objects as the screen moves 
			self.rect.x += scroll #Adds the scroll to the rectangle x for the object 
	class Poisonious_water(pygame.sprite.Sprite):
		def __init__(self, poi_img, X_axis, y_axis): #Create a constructor
			pygame.sprite.Sprite.__init__(self)#Inherit from the pygame sprite class
			self.image = poi_img
			self.rect = self.image.get_rect()
			self.rect.midtop = (X_axis + block_size // 2, y_axis + (block_size - self.image.get_height()))#This Gets the middle 
			#top part for teh collision 

		def update(self):#update the decorating objects as the screen moves 
			self.rect.x += scroll#Adds the scroll to the rectangle x for the object 
	class Next_Level(pygame.sprite.Sprite):
		
		def __init__(self, exi_img, X_axis, y_axis):#Create a constructor
			pygame.sprite.Sprite.__init__(self)#Inherit from the pygame sprite class
			self.image = exi_img
			self.rect = self.image.get_rect()
			self.rect.midtop = (X_axis + block_size // 2, y_axis + (block_size - self.image.get_height()))#This Gets the middle 
			#top part for the collision 

		def update(self):#update the decorating objects as the screen moves 
			global current_level
			self.rect.x += scroll#Adds the scroll to the rectangle x for the object 
			current_level+=1 #Adds one to the current level 
	class ChestBox(pygame.sprite.Sprite):#Create a constructor
		def __init__(self, type_chest, X_axis, y_axis):#Inherit from the pygame sprite class
			pygame.sprite.Sprite.__init__(self)
			self.type_chest = type_chest
			if type_chest == 'Potion':#Checks if the chest is potion 
				self.image = potion_img #then image is potion 
			elif type_chest == 'Kunai':#Checks if the chest is Kunai 
    				self.image = Kunai_box_img#then image is Kunai 
			elif type_chest == 'Coin':#Checks if the chest is Coin 
    				self.image = coin_img#then image is Coin 
			self.rect = self.image.get_rect() #Sets the rectangle of the image to the rectangle of the image 
			self.rect.midtop = (X_axis + block_size // 2, y_axis + (block_size - self.image.get_height()))#This Gets the middle 
			#top part for the collision 


		def update(self):#update the decorating objects as the screen moves and ninja collides 
			
			self.rect.x += scroll# Adds the scroll to the rectangle x for the object 
			if pygame.sprite.collide_rect(self, Ninja): #Check for collision with the ninja 
				if self.type_chest == 'Potion':  #Checks if the chest is potion 
					Ninja.power += 50  #increase the health of the ninja 
					if Ninja.power > Ninja.full_power:  #If the health if greater than full power 
						Ninja.power = Ninja.full_power  #Set it to default 
				elif self.type_chest == 'Kunai':  #if the chest type is kunai
					Ninja.kunai += 8  #Add 8 kunai's
				elif self.type_chest == 'Coin':  #Check if the chest type if coin 
					x = open('Text_files/Coin.txt','r').read()  #Open the coin file as read 
					xx = open('Text_files/Coin.txt','w')  #Open the coin file as write 
					coin = int(x) +1   #Add one to the coin file
					xx.write(str(coin))  #Write it to the file 

					music = pygame.mixer.music.load('Music/coin.mp3')  #Load the music 
					pygame.mixer_music.set_volume(0.09)  #Set the volume 
					pygame.mixer.music.play()  #Play the music 
						
				self.kill() #Remove the object 
	class Power():
		def __init__(self, X_axis, y_axis, power, full_power):  #Create a constructor 
			#Define the variables
			self.x = X_axis 
			self.y = y_axis
			self.power = power
			self.full_power = full_power
		def draw(self, power): #Draws the power bar at the top of the screen
			powerRatio = (self.power / self.full_power) #Ratio for the health to damage 
			self.power = power
			power_green = pygame.image.load('Progress03.png') #Load the image 
			power_green = pygame.transform.scale(power_green,(abs(180*powerRatio),30)) #Transform it 
			power_red = pygame.image.load('Health.png') #Load the image 
			power_red = pygame.transform.scale(power_red,(180,30)) #Transform it 
			screen.blit(power_red,(105, 15))#Display it 
			screen.blit(power_green,(105,15))#Display it 
   
	class Kunai(pygame.sprite.Sprite):
		def __init__(self, X_axis, y_axis, dir):#Create a constructo
			pygame.sprite.Sprite.__init__(self)#Inherits the sprite class 
			#Define the variables 
			self.run_sped = 10
			self.image = kunai_img
			self.rect = self.image.get_rect()
			self.rect.center = (X_axis, y_axis)
			self.dir = dir

		def update(self):#This updates the kunai 
			self.rect.x += (self.dir * self.run_sped) + scroll #Allows the kunai's Movement 
			if self.rect.right < 0 or self.rect.left > screen_width: #Checks if the kunai has gone out of the screen 
				self.kill() #if so then kill the kunai
			for block in game.hurdle_lis: #For every hurdle in the hurdle list 
				if block[1].colliderect(self.rect): #if it collides with the kunai 
					self.kill() #then destroy the kunai 

			if pygame.sprite.spritecollide(Ninja, KunaiSet, False): #if the kunai hit the Ninja
				if Ninja.breathing: #Check if the ninja is still breathing 
						Ninja.power-=10 #Then reduce the power by 10 
						if Ninja.power>Ninja.full_power: #if the power of the ninja is greater than full power 
								Ninja.power=Ninja.full_power #Set the power to default 
		
						self.kill() #Destroy the kunai

			for Wizard in WizardSet: #Loop through every single wizard in the wizard set 
					if pygame.sprite.spritecollide(Wizard, KunaiSet, False): #If the kunai collided with the enemy 
						if Wizard.power ==0: #Check if the power of 0 
							Wizard.nextAction(2) #Then update the death action 
						if Wizard.breathing: #Check if the wizard is breathing 
							Wizard.power -= 20 #Reduce the power by 20 
							
							xx = problemMath(20,m_left,m_right,throw_kunai).problem_win() #Create a problem window 
							if xx: #Check if the answer is true
								Wizard.power -= 10 #Then reduce the power of the wizard 
							else: #otherwise
								Ninja.power -=10 # Reduce the health of the Ninja 
								
						
								
							self.kill() #Destroy the Kunai 
	def check():
		levcomplete = False
		if levcomplete:
			current_level += 1
			background_scroll = 0
			if current_level <= full_level:
				with open(f'current_level{current_level}_data.csv', newline='') as csvfile:
					csv_file = csv.reader(csvfile, delimiter=',')
					for x, row in enumerate(csv_file):
						for y, block in enumerate(row):
							csvData[x][y] = int(block)
				game = Game()
				Ninja, powerBar = game.levelData(csvData)	
			else:
				current_level =1
				with open(f'current_level{current_level}_data.csv', newline='') as csvfile:
					csv_file = csv.reader(csvfile, delimiter=',')
					for x, row in enumerate(csv_file):
						for y, block in enumerate(row):
							csvData[x][y] = int(block)
				game = Game()
				Ninja, powerBar = game.levelData(csvData)
			
      
	WizardSet,KunaiSet ,ChestSet ,DecorationSet ,waterSet ,exitSet =  create_sets() #Creates the sets for the different classes
	
	csvData = extract_data() # Gets the Csv data from the function 
	game = Game() #Creates a game object 
	Ninja, powerBar = game.levelData(csvData) #gets the ninja and the power bar from the level data 


	font = pygame.font.Font("FONTS/HACKED.TTF", 30) #Initisise the font 
	Play = True #Set the variabel play to true 
	while Play: #Run the while loop 
		screen.fill((0,0,0)) #Fill the screen black 
		FPS_CLOCK.tick(FPS) #Start the clock

		display_background() #display the background 
		game.Draw_blocks() # Draw the tiles
		powerBar.draw(Ninja.power) #draw the power bar for the player
		high = open('Text_files/high.txt','r') #Open the highscore file 
		coin = open('Text_files/Coin.txt','r') # open the coin file 
		
		
		text_img1 = font.render(f'SCORE: {high.read()}', True, R) #render the text for score 
		screen.blit(text_img1, (1000, 50)) #Display the text
		screen.blit(coin_img,(1000,100)) #Display the image
		text_img2 = font.render(f': {coin.read()}', True, (0,255,255))#render the text for coin 
		screen.blit(text_img2, (1050, 100))#Display the text
		text_img3 = font.render('KUNAI:  ', True, R)#render the text for kunai 
		screen.blit(text_img3, (10, 60))#Display the text
		text_img3 = font.render('HEALTH:  ', True, (0,255,0))#render the text for health 
		screen.blit(text_img3, ( 5, 10))#Display the text
		
		for x in range(Ninja.kunai):#Loop through the number of kunai images 
			screen.blit(kunai_img, (90 + (x * 10), 65)) #Display them side by side

		Ninja.update() #Update the Ninja contantly 
		Ninja.Sprite_Blit() #Display the Ninjaon the screen 

		for Wizard in WizardSet: #Loop through every single wizard 
			Wizard.handle_AI() #Make the enemy AI work 
			Wizard.update() # Update the wizard 
			Wizard.Sprite_Blit() #Display the wizard 

		
		set_update() #This updates all the sets 


		

		if Ninja.breathing: #Checks if the ninja is breathing 
			if throw_kunai: #If throw kunai is true 
				Ninja.nextAction(4) #Show the throw action 
				Ninja.throw_kunai() #Throw the kunai 
			if Attacking and Ninja.isIn_Air: # Check is the ninja is jumping and is in air
				Ninja.nextAction(5) #Update the 5 action 
			elif Ninja.isIn_Air: #Checks if the player is in air 
				Ninja.nextAction(2) #Then show the jump action 
			elif m_left or m_right: #If the player is moving right or left 
				Ninja.nextAction(1) #show first action 
			else:
				Ninja.nextAction(0)#Show the idle action 
			
			Ninja.Run(m_left, m_right) #Make the ninja run 
			scroll = Ninja.Run(m_left, m_right) #Returns the scroll 
			background_scroll -= scroll #Move the background by subtracting the scroll 
		
			check()
			
		else:
			Main.pause('Dead')#If player is not breathing then he is dead display the dead menu 


		for event in pygame.event.get(): #Loop through every event 
    			
			if event.type == pygame.QUIT: #Check if the event is quit 
				Play = False #set bool play to false 
			if event.type == pygame.KEYDOWN: #Check if key is pressed 
				if event.key == pygame.K_LEFT: #if the key is left 
					m_left = True #Set m_left to True
				if event.key == pygame.K_RIGHT:#if the key is right 
					m_right = True#Set m_right to True
				if event.key == pygame.K_SPACE:#if the key is space 
					throw_kunai = True#Set throw_kunai to True
					Attacking = True#Set Attacking to True
				if event.key == pygame.K_UP and Ninja.breathing:#if the key is up 
					Ninja.isJumping = True#Set isjumping to True
				if event.key == pygame.K_d:#if the key is d 
					m_right = True#Set m_right to True
				if event.key == pygame.K_a:#if the key is a 
					m_left = True#Set m_left to True
				if event.key == pygame.K_w and Ninja.breathing:#if the key is w 
					Ninja.isJumping = True#Set isjumping to True
				if event.key == pygame.K_ESCAPE:#if the key is escape 
					Main.pause('PAUSED') #Display the pause menu 
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:#if the key is left 
					m_left = False#Set m_left to False
				if event.key == pygame.K_RIGHT:#if the key is right 
					m_right = False#Set m_right to False
				if event.key == pygame.K_SPACE:#if the key is space 
					throw_kunai = False#Set throw_kunai to False
					Attacking = False#Set Attacking to False
				if event.key == pygame.K_UP and Ninja.breathing:#if the key is up 
					Ninja.isJumping = False#Set isjumping to False
				if event.key == pygame.K_d:#if the key is d 
					m_right = False#Set m_right to False
				if event.key == pygame.K_a:#if the key is a 
					m_left = False#Set m_left to False
				if event.key == pygame.K_w and Ninja.breathing:#if the key is w 
					Ninja.isJumping = False#Set isjumping to False


		pygame.display.update() #Update the display 
def create_sets(): #Creates and returns all the sets
	WizardSet = pygame.sprite.Group()
	KunaiSet = pygame.sprite.Group()
	ChestSet = pygame.sprite.Group()
	DecorationSet = pygame.sprite.Group()
	waterSet = pygame.sprite.Group()
	exitSet = pygame.sprite.Group()
	return WizardSet,KunaiSet ,ChestSet ,DecorationSet ,waterSet ,exitSet
def extract_data(): #Extracts the data from the csv file and appends it to the list and return it 
	csvData = []
	for row in range(16):
		r = [-1] * 170
		csvData.append(r)
	with open(f'Currentlevel{current_level}_data.csv', newline='') as csvfile:
		csv_file = csv.reader(csvfile, delimiter=',')
		for x, row in enumerate(csv_file):
			for y, block in enumerate(row):
				csvData[x][y] = int(block)
	return csvData
def chest_images(): #These contain all the chest images
	RANDOM_WORD = random.randint(1, 40)
	kunai_img = pygame.image.load('Men/Kunai/Kunai.png').convert_alpha()
	kunai_img  = pygame.transform.scale(kunai_img,(20,20))
	potion_img = pygame.image.load(f'Potions/Icon{RANDOM_WORD}.png').convert_alpha()
	potion_img = pygame.transform.scale(potion_img,(50,50))
	coin_img = pygame.image.load(f'assets/block/14.png').convert_alpha()
	coin_img = pygame.transform.scale(coin_img,(50,50))
	Kunai_box_img = pygame.image.load('Kunai_box.png').convert_alpha()
	Kunai_box_img = pygame.transform.scale(Kunai_box_img,(0,50))
	return kunai_img,potion_img,coin_img,Kunai_box_img
def background_images(): #This loads all the background files and returns them
	texture_img = pygame.image.load('img/Back_layers2/L1.png').convert_alpha()
	texture_img = pygame.transform.scale(texture_img, (1280,800))
	trees_color_img = pygame.image.load('img/Back_layers2/L2.png').convert_alpha()
	trees_color_img = pygame.transform.scale(trees_color_img, (1280,800))
	tree_img = pygame.image.load('img/Back_layers2/L3.png').convert_alpha()
	tree_img = pygame.transform.scale(tree_img, (1280,800))
	tree_shadow_img = pygame.image.load('img/Back_layers2/L4.png').convert_alpha()
	tree_shadow_img = pygame.transform.scale(tree_shadow_img, (1280,800))
	return texture_img,trees_color_img,tree_img,tree_shadow_img
def boolean_variable(): #This contains all the boolean variables
	m_left = False
	m_right = False
	throw_kunai = False
	Attacking = False
	return  m_left,m_right,throw_kunai,Attacking

# Main.main_menu()

