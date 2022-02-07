import pygame

#게임 기본 옵션
pygame.init()
size = [400,900]
screen = pygame.display.set_mode(size)
title = 'my game'
pygame.display.set_caption(title)
clock = pygame.time.Clock()

#클래스 선언
class obj:
    #글로벌한 변수 선언
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    #이미지 불러오기
    def put_img(self, address):
        if address[-3] == 'png':
            self.img = pygame.image.load(address).conver_alpha()
        else:
            self.img = pygame.image.load(address)
            self_sx, self_sy = self.img.get_size()
    #불러온 이미지의 크기 조정
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx,sy))
        self.sx, self.sy = self.img.get_size()
    #해당좌표에 이미지 출력    
    def show(self):
        screen.blit(self.img, (self.x, self.y))

#클래스를 이용해 객체 선언
#ss는비행선
ss = obj()
ss.put_img("C:/Users/jp_desk/make_game/king.png")
ss.change_size(50,80)
ss.x = round(size[0]/2 - ss.sx/2)
ss.y = size[1] -ss.sy - 300
ss.move = 5
left_go = False
right_go = False
space_go = False
m_list = []        
black = (0,0,0)
white = (255,255,255)
k = 0

sb = 0
while sb == 0:
    #초당 프레임
    clock.tick(60)
    
    #입력
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sb = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False

    if left_go == True:
        ss.x -= ss.move
        if ss.x <= 0:
            ss.x = 0
    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx
    if space_go == True:
        mm = obj()
        mm.put_img("C:/Users/jp_desk/make_game/bullet.png")

        mm.change_size(5,15)
        mm.x = round(ss.x + ss.sx/2 - mm.sx/2)
        mm.y = ss.y - mm.sy - 10
        mm.move = 15
        m_list.append(mm)
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        m.y -= m.move
        if m.y <= - m.sy:
            d_list.append(i)
    for d in d_list:
        del m_list[d]

#출력    
    screen.fill(black)
    ss.show()
    pygame.display.flip()
pygame.quit()
