# -*- coding: dongwook kim
import pygame, time

from pygame.locals import *
pygame.init().

display_screen = pygame.display.set_mode((815, 85)) 

pygame.display.set_caption('MINI PYTHON PIANO')	

pygame.mouse.set_visible(1)	

white = (255, 255, 255)	

black = (0, 0, 0)

display_font = pygame.font.Font('/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf', 32)

text = (u"키보드 1~8까지 꾸욱 눌러 보세요. \n Esc키를 누르면 종료 됩니다.")	

display_text = display_font.render(text, True, black, white)	.

display_text_vis = display_text.get_rect()	

display_text_vis.center = (340, 34)	

def mp(file):	
	pygame.mixer.music.load(file)
	
while True:

	display_screen.fill(white)	
	
	display_screen.blit(display_text, display_text_vis)	
	
	pygame.display.update()	

	for event in pygame.event.get():	
      
      
		if (event.type == KEYDOWN):	
			if (event.key == pygame.K_1):

				mp("1.mp3")
				pygame.mixer.music.play()
 
      
		if (event.type == KEYDOWN):
     			if (event.key == pygame.K_2):

				mp("2.mp3")
				pygame.mixer.music.play()
     
		if (event.type == KEYDOWN):
     			if (event.key == pygame.K_3):

				mp("3.mp3")
				pygame.mixer.music.play()
			
		if (event.type == KEYDOWN):
     			if (event.key == pygame.K_4):

				mp("4.mp3")
				pygame.mixer.music.play()
			
		if (event.type == KEYDOWN):
     			if (event.key == pygame.K_5):

				mp("5.mp3")
				pygame.mixer.music.play()
			
		if (event.type == KEYDOWN):
     			if (event.key == pygame.K_6):

				mp("6.mp3")
				pygame.mixer.music.play()
		if (event.type == KEYDOWN):
     			if (event.key == pygame.K_7):

				mp("7.mp3")
				pygame.mixer.music.play()
		if (event.type == KEYDOWN):
     			if (event.key == pygame.K_8):

				mp("8.mp3")
				pygame.mixer.music.play()
				
		if (event.type == KEYUP):	


     			pygame.mixer.music.stop()
      
      
		if (event.type == KEYUP):
      			if (event.key == pygame.K_ESCAPE):

      				pygame.quit()
	
		if event.type == QUIT:	
			pygame.quit()


