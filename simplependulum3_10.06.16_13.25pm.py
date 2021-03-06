# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:05:28 2016

@author: janannibalaskandan

Simple Pendulum Project
"""

"""Want to set all the variables and calculate the matix T"""
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import pylab

class Matrix:
    
    def __init__(self, dt=0.0001, gravity = 9.81, Damping=1000, alpha=1, mass=1000, length=1):
        """Sets all the constants"""
        self.a = alpha
        self.g = gravity
        self.m = mass
        self.l = length
        self.dt = dt
        self.Dhat = Damping/(self.m*self.l*self.a) #scaled damping constant
    def matrixT(self):
        """returns matrix T"""
        self.oneone = -self.dt*self.Dhat+1
        self.onetwo = -self.dt*self.g/(self.l*(self.a)**2)
        self.twoone = self.dt
        self.twotwo = 1
        self.T = [self.oneone, self.onetwo, 
                  self.twoone, self.twotwo]
        return self.T

"""Want to generate intial conditions to feed into another class (which will
calculate the first set of variables). 
Either set the initial conditions or calculate phi(t=0) from theta(t=0)"""
class GenerateInitialConditions:
    def initialconditions(self,theta_nought=np.pi/2,phi_nought=1):
        """returns first input vector"""
        self.theta = theta_nought
        self.phi = phi_nought
        return [self.phi, self.theta]

"""Want to: 1) take matrix from Matrix class and take the initial conditions 
from GenerateInitialConditions class 2) calculate the first  input vector 3) apply the 
matrix T to get the output vector 4) store the output 5) set the output to the 
new input 6) repeat"""
class CalculateVariables(Matrix):#(Matrix, GenerateInitialConditions):  
    thetaAxis = []
    def CalculateFirstInputVector(self): 
        """creates the first vector [phi, theta] from the intial conditions"""
        initial = GenerateInitialConditions()
        initial = GenerateInitialConditions.initialconditions(initial)
        self.thetaOld = initial[1]
        self.thetaAxis.append(self.thetaOld)
        self.phiOld = initial[0]
        self.inputVector = [self.phiOld, self.thetaOld]
        return self.inputVector
    def GetMatrixT(self):
        matrix = Matrix()
        self.T = Matrix.matrixT(matrix)
        return self.T 
    def Store(self,addThisThetaValue):
        """Stores values in array"""
        self.addThisThetaValue = addThisThetaValue
        self.thetaAxis.append(self.addThisThetaValue)
    def Output(self,howmanytimes = 100000):
        """Does matrix calculations and gets output"""
        #self.T = self.GetMatrixT()
        #self.inputVector = self.CalculateFirstInputVector()
        self.howmanytimes = howmanytimes
        for i in range(self.howmanytimes):
            self.phiNew = self.T[0]*self.inputVector[0] + self.T[1]*self.inputVector[1]
            self.thetaNew = self.T[2]*self.inputVector[0] + self.T[3]*self.inputVector[1]
            self.Store(self.thetaNew)
            self.outputVector = [self.phiNew, self.thetaNew]
            self.inputVector = self.outputVector
        self.timeAxis = [self.dt*i for i in range(self.howmanytimes +1)]
        return self.thetaAxis, self.timeAxis
        
class Run(CalculateVariables):
    def run(self):        
        """Run program: plot graph of trajectory of simple pendulm"""
        self.b = CalculateVariables()
        self.inputVector = CalculateVariables.CalculateFirstInputVector(self.b)
        self.getMatrixT = CalculateVariables.GetMatrixT(self.b)
        self.outputVector = CalculateVariables.Output(self.b)
        #return self.b.thetaAxis, self.b.timeAxis
        """"Plots graphs"""
        plt.plot(self.b.timeAxis,self.b.thetaAxis)
        plt.xlabel('time/s')
        plt.ylabel('Theta/radians')
        
a = Run()
a = Run.run(a)

#Use the following code to check how many data points there are on the x axis and
#how many there are on the y axis. There should be 100001 in each
"""
c = Run()
b = Run.CalculateFirstInputVector(c)
b = Run.GetMatrixT(c)
b = Run.Output(c)
print "theta:", len(b[0])," time:", len(b[1])
"""
plt.show()

