from utils import *
import utils
from Login import Login

if __name__ == '__main__':
    root = Tk()
    root.geometry('310x330')
    root.iconphoto(False, PhotoImage(file = "pucpr.png"))
    root.configure(background=co1)
    root.resizable(width=FALSE, height=FALSE)
    application = Login(root)
    utils.center(root)
    root.mainloop()
