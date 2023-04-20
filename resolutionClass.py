import pyautogui as auto

class Resolution:
    def __init__(self, exitXCraft=0, exitYCraft=0, craftTableX=0,  
                 craftTableY=0, scrollX=0, startScrollY=0, endScrollY=0, 
                    warHammerX=0, warHammerY=0, craftButtonX=0, craftButtonY=0):
        self.__exitXCraft = exitXCraft
        self.__exitYCraft = exitYCraft
        self.__craftTableX = craftTableX
        self.__craftTableY = craftTableY
        self.__scrollX =  scrollX
        self.__startScrollY = startScrollY
        self.__endScrollY = endScrollY
        self.__warHammerX =  warHammerX
        self.__warHammerY = warHammerY
        self.__craftButtonX =  craftButtonX
        self.__craftButtonY =  craftButtonY

    def fullHD(self):
        self.__exitXCraft = 348
        self.__exitYCraft = 922
        self.__craftTableX = 352
        self.__craftTableY = 437
        self.__scrollX = 1620
        self.__startScrollY = 312
        self.__endScrollY = 900
        self.__warHammerX = 1326
        self.__warHammerY = 615
        self.__craftButtonX = 1326
        self.__craftButtonY = 942
        

# fullHD = {
#     "exitXCraft": 348,
#     "exitYCraft": 922,
#     "craftTableX": 352,
#     "craftTableY": 437,
#     "scrollX": 1620,
#     "startScrollY": 312,
#     "endScrollY": 900,
#     "warHammerX": 1326,
#     "warHammerY": 615,
#     "craftButtonX": 1326,
#     "craftButtonY": 942
# }