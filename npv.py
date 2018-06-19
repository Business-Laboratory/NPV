import numpy as np

class NPV(object):
    """
    Creates a Net Present Value (NPV) object which keeps track of both a time and a value
    The rate RATE is assumed to be on the appropiate scale for the time
    The rate is assumned to be the same for every value
    The default discount rate is set to .1
    The default tolerance TOL is set to a thousandth of a cent

    Setup
    -----
    The discount rate for all instances can be set using NPV.RATE = <new_rate>
    The tolerance can be changed using NPV.TOL = <new_tol>.
    
    Constructor Parameters
    ----------------------
    time (int) : an integer giving the time the value is view from
    value (float) : a dollar value
    
    Attributes
    ----------
    time (int) : an integer giving the time the value is view from
    value (float) : a dollar value
    
    Overload Methods
    ----------------
    X + Y : Adds two NPVs by converting them to the earliest time and then adding thier values
    X - Y : Subtracts one NPV from annother by converting them to the earliest time and then adding thier values
    a * X or X * a : multiplies an NPV X and a number a by multiplying X's value by a
    X / a : divides an NPV X by a number a by dividing X's value by a
    -X : set NPV X's value to its negative
    == : converts two NPVs them to a common time and checks if their converted values are within the tolerance
    != : converts two NPVs them to a common time and checks if their converted values are not within the tolerance
    >= : converts two NPVs them to a common time and checks if the left NPV's value is greater than the right NPV's value or within tolerance
    >= : converts two NPVs them to a common time and checks if the left NPV's value is less than the right NPV's value or within tolerance
    > : converts two NPVs them to a common time and checks if the left NPV's value is greater than the right NPV's value and not within tolerance
    < : converts two NPVs them to a common time and checks if the left NPV's value is greater than the right NPV's value and not within tolerance
    """
    
    # define global variables
    global RATE
    global TOL
    RATE = 0.1
    TOL = 10**-6
    
    __slots__ = ["time", "value"]
    def __init__(self, time, value):
        
        # check types
        if not isinstance(time, (int, np.integer)):
            raise TypeError("The time argument must be an int.")
        if not isinstance(value, (int, np.integer, float, np.float)):
            raise TypeError("The value argument must be a number.")
        
        # assign attributes
        self.time = time
        self.value = value
        return
    
    def __str__(self):
        return "NPV(time = {time}, value = {value})".format(time = str(self.time), value = str(self.value))
    
    def __repr__(self):
        return str(self)
    
    def shift_to(self, target_time):
        """
        Converts a NPV to a taget time and its correct value at that time
        
        Arguments:
        ----------
        target_time : the time from which the value is to be view from
        """
        
        # check type
        if not isinstance(target_time, int):
            raise TypeError("The traget_time argument must be an int.")
        
        new_value = self.value * (1 + RATE) ** (target_time - self.time)
        new_time = target_time
        new_NPV = NPV(new_time, new_value)
        return new_NPV
        
    def __add__(self, other):
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be added to NPVs.")
            
        new_time = min(self.time, other.time)
        new_value = self.shift_to(new_time).value + other.shift_to(new_time).value
        new_NPV = NPV(new_time, new_value)
        return new_NPV
        
    def __sub__(self, other):
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be subtracted from to NPVs")
            
        new_time = min(self.time, other.time)
        new_value = self.shift_to(new_time).value - other.shift_to(new_time).value
        new_NPV = NPV(new_time, new_value)
        return new_NPV
    
    def __rmul__(self, other):
        
        # check type
        if not isinstance(other, (int, float)):
            raise TypeError("NPV can only be multiplied by numbers.")
        return NPV(self.time, self.value * other)
    
    __mul__ = __rmul__
    
    def __truediv__(self, other):
        
        # check type
        if not isinstance(other, (int, float)):
            raise TypeError("NPV can only be divided by numbers.")
            
        return NPV(self.time, self.value / other)
    
    def __neg__(self):
        return NPV(self.time, -self.value)
    
    def __eq__(self, other):
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return abs(self.shift_to(new_time).value - other.shift_to(new_time).value) < TOL
    
    def __lt__(self, other):
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return self.shift_to(new_time).value < other.shift_to(new_time).value and self != other
    
    def __gt__(self, other):
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return self.shift_to(new_time).value > other.shift_to(new_time).value and self != other
    
    def __le__(self, other):
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return self.shift_to(new_time).value < other.shift_to(new_time).value
    
    def __ge__(self, other):
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return self.shift_to(new_time).value > other.shift_to(new_time).value or self == other
        