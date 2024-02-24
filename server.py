import threading
import pygame
import winsound
import time
import socket
# made by dokong2
# 이 파이썬 프로젝트는 비영리 목적이며 테스트로 만들어보는 사이드프로젝트입니다.
# 깃허브 : https://github.com/Dokong2/wandu_would


class log():
    def write(msg):
        now = time
        print(str(now.localtime().tm_hour) + "시" + str(now.localtime().tm_min) + "분" + str(now.localtime().tm_sec) + "초" + " : " + msg)

def startwindow():
    log.write("서버 생성을 시작합니다.")
    log.write("x좌표 생성..")
    host = socket.gethostname()
    x = socket.socket()
    x.bind((host, 1010))
    log.write("y좌표 생성..")
    y = socket.socket()
    y.bind((host, 2020))
    log.write("이모지 서버 생성..")
    emoge = socket.socket()
    emoge.bind((host, 8080))
    log.write("모든 서버가 생성됐습니다.")
    
    
if __name__ == "__main__":
    startwindow()