import threading
import pygame
import winsound
import time
# made by dokong2
# 이 파이썬 프로젝트는 비영리 목적이며 테스트로 만들어보는 사이드프로젝트입니다.
# 깃허브 : https://github.com/Dokong2/wandu_would


def log(msg):
    now = time
    print(now.localtime().tm_hour + " : " + now.localtime().tm_min + " : " + now.localtime().tm_sec + " " + msg)


def startwindow():
    print("이 콘솔에 출력되는 메시지는 테스트 용이며 실제 exe 확장자에선 콘솔이 실행되지 않을 것입니다.")
    