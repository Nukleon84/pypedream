import math

class ScalarMethods(object):

    @staticmethod
    def solveNewtonRaphson(f, x, maxIter=50, tolerance=1e-6, silent=True):
        for i in range(maxIter):
            f.reset()
            fx= f.eval()
            dfdx=f.diff(x)
            delta = -fx/dfdx
            x.addDelta(delta)
            if(not silent):
                print(f"Iter: {i} x: {x.value} dfdx: {dfdx} delta: {delta}")

            if(math.fabs(delta)<tolerance):
                if(not silent):
                    print(f"Newton-Raphson solver converged in {i} iterations.")
                return True
        if(not silent):
            print(f"Newton-Raphson solver did not converge in {i} iterations.")                
        return False                
        
    @staticmethod
    def solveBisection(f, x, a,b, maxIter=50, tolerance=1e-6):
        x1 =a
        x2 =b
        mid = 0.5*(x1+x2)
        x0 = x.eval()

        x.value= x1
        f.reset()
        fa= f.eval()

        x.value= x2
        f.reset()
        fb= f.eval()

        if(math.copysign(1,fa) == math.copysign(1,fb) ):
            x.value=x0
            print("Root is not bracketed!")
            return False

        for i in range(maxIter):
            mid = 0.5*(x1+x2)
            x.value=mid

            f.reset()

            if(fb*f.eval()>0):
                x2=mid
            else:
                x1=mid
            
            delta=x2-x1
            
            print(f"Iter: {i} x: {x.value} x1: {x1} x2: {x2} delta: {delta}")

            if(math.fabs(delta)<tolerance):
                x.value= x1
                f.reset()
                fx1= f.eval()

                x.value=x2
                f.reset()
                fx2=f.eval()

                if(math.fabs(fx2-fx1)>0):
                    x.value= x2-(x2-x1)*fx2/(fx2-fx1)

                print(f"Bisection solver converged in {i} iterations.")
                return True

        print(f"Bisection solver did not converge in {i} iterations.")                
        return False      

