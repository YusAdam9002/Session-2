import sys,pygame

## Setup code
pygame.init()
screen = pygame.display.set_mode((500,500))

## Initialize all variables
x = 100
y = 100
dx = 0
dy = 0
Movement = True

# Game loop
while True:
    # Event detection
    pos = pygame.mouse.get_pos() 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and Movement == True:
            x1 = pos[0]
            y1 = pos[1]
            dx = x1 - x
            dy = y1 - y
            Movement  = False 
        if event.type == pygame.QUIT: 
            sys.exit()
    
    # Update game model
    x = x + dx
    y = y + dy
    screen.fill((0,0,0))
      # Draw background
    for i in range(210):
        for t in range(200):
            pygame.draw.circle(screen,(11, 3, 252),(i * 4, t*4), 2)

    # Check for wall collisions and change direction if necessary
    if x > 500 or x < 1:
        dx = -dx
    if y > 500 or y < 1:
        dy = -dy
    if x >= 392.5 and x <= 407.5 and y >= 392.5 and y <= 407.5:
          quit()

    if dx <= 0.1 and dy <= 0.1:
        Movement = True

    dx = dx * 0.69
    dy = dy * 0.69
    # Draw target
    pygame.draw.circle(screen,(0, 0, 0), (400, 100), 15)
    
    # Draw ball
    pygame.draw.circle(screen,(255,255,255),(x,y),10) 

    pygame.display.update()
