
import math
import matplotlib.pyplot as plt
class C_polar:
    """
    总结一下我想要的效果：
    输入Re() 和 Im(), 得到attribute r 和 theta
    input 是 complex number 或者是re/im
    一个类可以是一个combinations of tasks 
    return 的dataype是
    """
    def __init__(self,arg=None,mod=None,re=None,im=None):
        if mod!=None and arg!=None:
            self.Arg= arg
            self.Mod = mod
        if re!=None and im!=None:
            AM = self.R2polar(re,im)
            self.Arg = AM[0]
            self.Mod = AM[1]
        

    def R2polar(self,re,im):
        mod=math.sqrt(re**2 + im**2)
        try:
            if re*im >=0:
                if re>=0:
                    arg=math.atan(im/re)
                    return arg,mod
                else:
                    arg=-(math.pi-math.atan(im/re))
                    return arg,mod
            else:
                if re>=0:
                    arg=-math.atan(im/re)
                    return arg,mod
                else:
                    arg=math.pi-math.atan(im/re)
                    return arg,mod
        except:
            raise ValueError("value input is problematic")
   
    def Polar_plot_rec(self,re,im):
        ctpl_size = max(abs(re),abs(im))*1.5
        X_axis_x = [-ctpl_size, ctpl_size]
        X_axis_y = [0, 0]
        Y_axis_x = [0, 0]
        Y_axis_y = [-ctpl_size, ctpl_size]
        p_x = [0,re]
        p_y = [0,im]
        plt.plot(X_axis_x, X_axis_y, color = "gray")
        plt.plot(Y_axis_x, Y_axis_y, color = "gray")
        plt.plot(0, 0, marker="o", color = "gray")
        plt.plot(0, 0, marker="o", color = "gray")
        plt.plot(p_x, p_y, marker="o", color = "red")
        plt.show()

    def Polar_plot_polar(self):
        re = self.Mod*math.cos(self.Arg)
        im = self.Mod*math.sin(self.Arg)
        self.Polar_plot_rec(re,im)

if __name__ == '__main__':
    #class demo
    z1 = C_polar(arg=math.pi*10, mod=1)
    C_polar.Polar_plot_polar(z1)

    z2 = C_polar(re=1, im=1)
    C_polar.Polar_plot_polar(z2)