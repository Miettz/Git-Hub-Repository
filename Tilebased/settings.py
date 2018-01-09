##colors
lightgrey = (100,100,100)
darkgrey = (40,40,40)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)


title = 'My Game'
width = 1024
height = 768
fps = 60
bgcolor = darkgrey

tilesize = 32
gridwidth = width/tilesize
gridheight = height/tilesize

#player
player_speed = 300

##platform coordinates (x,y,w,h)
##platform_list = [(0,height-40,width,40),
##                 (width/2 -50,height*3/4,100,20),
##                 (300,200,100,20),
##                 (175,100,50,20)]


##
##
##        This is how you add platforms without the platform list
##
##        p1 = Platform(0,height-40,width,40)
##        self.all_sprites.add(p1)
##        self.platforms.add(p1)
##        p2 = Platform(width/2 -50,height*3/4,100,20)
##        self.all_sprites.add(p2)
##        self.platforms.add(p2)


