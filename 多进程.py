import multiprocessing,os

def dance():
    for i in range(100):
        print('dancing')

def sing():
    for i in range(100):
        print('singing ')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=dance)
    p2 = multiprocessing.Process(target=sing)

    p1.start()
    p2.start()
