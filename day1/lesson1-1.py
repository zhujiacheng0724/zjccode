import random
import cv2
import re

from numpy import append, true_divide
import math
from functools import reduce
import time,sys
import heapq
from collections import deque
from datetime import datetime
import mysql.connector
from sqlalchemy import Column,create_engine,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def worktime(function):
    def timetotime(a,b):
        time1=time.time()
        x = function(a,b)
        time2=time.time()
        print("计算时间为=",time2 - time1)
        return x 
    return timetotime
@worktime
def myAdd(a,b):
    return(a+b)
@worktime
def myCut(a,b):
    return(a-b)
@worktime
def myPlus(a,b):
    return(a*b*a*a*b-a-b/a+b**99)
@worktime
def myChu(a,b):
    return(a/b)


print(myChu(4,5))
