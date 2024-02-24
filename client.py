import threading
import pygame
import winsound
import time
import socket
# made by dokong2
# 이 파이썬 프로젝트는 비영리 목적이며 테스트로 만들어보는 사이드프로젝트입니다.
# 깃허브 : https://github.com/Dokong2/wandu_would

def startwindow():
    screen = pygame.display.set_mode((500, 500)) # 가로, 세로
    pygame.display.set_caption("wandu_would")
    running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
    programIcon = pygame.image.load('./gamepile/imege/zzzzzzz.png')
    pygame.display.set_icon(programIcon)
    while running:
        for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
            if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
                running = False
    pygame.quit()

if __name__ == "__main__":
    startwindow()