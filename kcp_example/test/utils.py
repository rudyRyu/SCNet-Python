import time
import random

g_ScriptStartTime = time.time()

g_RndSeed = int(time.time())

def msleep(ms):
    time.sleep(ms * 0.001)

def initrndseed():
    global g_RndSeed
    random.seed(g_RndSeed)

def rndvalue(_min, _max):
    return _min + random.randint(0, _max - _min)
    # return random.randint(0, _max - _min)

def getms():
    global g_ScriptStartTime
    return int((time.time()-g_ScriptStartTime)*1000)

def uint322netbytes(i):
    # a, b, c, d = chr(i>>24&255) ,chr(i>>16&255),chr(i>>8&255),chr(i&255)
    # print(a.encode('utf-8'))
    # print(b.encode('utf-8'))
    # print(c.encode('utf-8'))
    # print(d.encode('utf-8'))

    # return chr(i>>24&255) + chr(i>>16&255) + chr(i>>8&255) + chr(i&255)
    return i.to_bytes(4, byteorder="big", signed=False)

def netbytes2uint32(s):
    # return s[0]<<24 | s[1]<<16 | s[2]<<8 | s[3]
    return int.from_bytes(s, byteorder="big", signed=False)
