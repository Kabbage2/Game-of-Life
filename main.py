import sys, pygame
pygame.init()

size = width, height = 500, 500
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
background = pygame.Surface(size)

class rect:
    def __init__(self, color, pos, surface, invcol):
        self.color = color
        self.pos = pos
        self.surface = surface
        self.invcol = invcol


    def draw(self):
        pygame.draw.rect(self.surface, self.invcol, ((self.pos), (100,100)))
        pygame.draw.rect(self.surface, self.color, ((self.pos), (100,100)), 1)
        
rep_rects = {}
my_rects = {}
num = 0

for y in range(0, height, 100):
    for x in range(0, width, 100):
        my_rects[f"rect_{num}"] = rect(white, (x,y), screen, black)
        my_rects[f"rect_{num}"].draw()
        rep_rects[x // 100, y // 100] = 0
        num += 1
pygame.display.flip() 

def changesqrcolr(n):
    if my_rects[f"rect_{n}"].color == white:
        my_rects[f"rect_{n}"].color = black
        my_rects[f"rect_{n}"].invcol = white
        my_rects[f"rect_{n}"].draw()
    else:
       my_rects[f"rect_{n}"].color = white
       my_rects[f"rect_{n}"].invcol = black
       my_rects[f"rect_{n}"].draw()
    pygame.display.flip()  

def get_neighbors(coords: tuple):
    print(coords)

while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rect_num = (mouse_y // 100) * 5 + (mouse_x // 100)
            changesqrcolr(rect_num) 