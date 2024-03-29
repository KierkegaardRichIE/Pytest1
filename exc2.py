# plot a sine wave from 0 to 4pi  
from pylab import *  
x_values = arange(0.0, math.pi * 4, 0.01)  
y_values = sin(x_values)  
plot(x_values, y_values, linewidth=1.0)  
xlabel('x')  
ylabel('tan(x)')  
title('Simple plot')  
grid(True)  
savefig("sin.png")  
show()  