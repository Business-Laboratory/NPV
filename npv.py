import numpy as np

class NPV(object):
    """
    Creates a Net Present Value (NPV) object which keeps track of both a time and a value
    The rate is not assumned to be the same for every value
    The default tolerance TOL is set to a thousandth of a cent

    Setup
    -----
    The discount rate for an instance can be set using NPV.set_rate(instance, new_rate)
    The tolerance can be changed using NPV.TOL = <new_tol>.
    
    Constructor Parameters
    ----------------------
    time (int) : an integer giving the time the value is view from
    value (float) : a dollar value
    rate (float) : a discount rate
   
    Attributes
    ----------
    time (int) : an integer giving the time the value is view from
    value (float) : a dollar value
    rate (float) : a discount rate
    
    Overload Methods
    ----------------
    X + Y : Adds two NPVs by converting them to the earliest time and then adding thier values
    X - Y : Subtracts one NPV from annother by converting them to the earliest time and then adding thier values
    X + Y : Adds two NPVs with different rates by converting them to 0 time and adding their values
    X - Y : Subtracts one NPV from another with a different rate by convering them to 0 time and adding their values
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
    global TOL
    TOL = 10**-6
    
    __slots__ = ["time", "value", "rate"]
    def __init__(self, time, value, rate):
        
        # check types
        if not isinstance(time, (int, np.integer)):
            raise TypeError("The time argument must be an int.")
        if not isinstance(value, (int, np.integer, float, np.float)):
            raise TypeError("The value argument must be a number.")
        if not isinstance(rate, (int, np.integer, float, np.float)):
            raise TypeError("The rate argument must be a number.")

        # assign attributes
        self.time = time
        self.value = value
        self.rate = rate

        return
    
    def __str__(self):
        """ Creates a string representation of the NPV """
        return "NPV(time = {time}, value = {value}, rate = {rate})".format(time = str(self.time), value = str(self.value), rate = str(self.rate))
    
    def __repr__(self):
        return str(self)

    def set_rate(self, input_rate):
        """ Replaces the current rate with the new rate """

        if not isinstance(input_rate, (int, np.integer, float, np.float)):
            raise TypeError("The rate argument must be a number.")

        self.rate = input_rate
        return self
    
    def shift_to(self, target_time):
        """
        Converts a NPV to a target time and its correct value at that time
        
        Arguments:
        ----------
        target_time : the time from which the value is to be view from
        """
        
        # check type
        # check for complete class
        if not isinstance(target_time, int):
            raise TypeError("The target_time argument must be an int.")            
        
        new_value = self.value * (1 + self.rate) ** (target_time - self.time)
        new_time = target_time
        new_NPV = NPV(new_time, new_value, self.rate)
        return new_NPV

    def __add__(self, other):
        """
        Converts both NPV objects to the earliest time between them and adds their
        values together
        """
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be added to NPVs.")
        if (other.rate != self.rate):
            raise TypeError("Only NPVs with the same rate can be added.")
            
        new_time = min(self.time, other.time)
        new_value = self.shift_to(new_time).value + other.shift_to(new_time).value
        new_NPV = NPV(new_time, new_value, self.rate)
        return new_NPV
        
    def __sub__(self, other):
        """
        Converts both NPV objects to the earliest time between them and subtracts the inputed 
        NPV object from the current one
        """

        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be subtracted from to NPVs")
        if (other.rate != self.rate):
            raise TypeError("Only NPVs with the same rate can be subtracted.")

        new_time = min(self.time, other.time)
        new_value = self.shift_to(new_time).value - other.shift_to(new_time).value
        new_NPV = NPV(new_time, new_value, self.rate)
        return new_NPV

    def force_add(self, other):
        """ Adds two NPV values together if their rates are different from one another """

        if (other.rate != self.rate):
            new_value = self.shift_to(0).value + other.shift_to(0).value
            new_NPV = NPV(0, new_value, 0)
            return new_NPV
        else:
            raise TypeError("Force_add is only to be used for NPVs with different rates. Please use __add__")

    def force_sub(self, other):
        """ Subtracts the inputed NPV from the current NPV if their rates are different from one another """

        if (other.rate != self.rate):
            new_value = self.shift_to(0).value - other.shift_to(0).value
            new_NPV = NPV(0, new_value, 0)
            return new_NPV
        else:
            raise TypeError("Force_sub is only to be used for NPVs with different rates. Please use __sub__")

    
    def __rmul__(self, other):
        """ Multiplies an NPV value by a constant """

        # check type
        if not isinstance(other, (int, float)):
            raise TypeError("NPV can only be multiplied by numbers.")
        return NPV(self.time, self.value * other, self.rate)
    
    __mul__ = __rmul__
    
    def __truediv__(self, other):
        """ Divides an NPV value by a constant """

        # check type
        if not isinstance(other, (int, float)):
            raise TypeError("NPV can only be divided by numbers.")
            
        return NPV(self.time, self.value / other, self.rate)
    
    def __neg__(self):
        """ Makes an NPV's value negative """
        
        return NPV(self.time, -self.value, self.rate)
    
    def __eq__(self, other):
        """ Returns true if two NPV's values are equal """

        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.") 
            
        new_time = min(self.time, other.time)
        return abs(self.shift_to(new_time).value - other.shift_to(new_time).value) < TOL
    
    def __lt__(self, other):
        """ Returns true if the current NPV's value is less than the inputted NPV """
        
        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return self.shift_to(new_time).value < other.shift_to(new_time).value and self != other
    
    def __gt__(self, other):
        """ Returns true if the current NPV's value is greater than the inputted NPV """

        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return self.shift_to(new_time).value > other.shift_to(new_time).value and self != other
    
    def __le__(self, other): 
        """ Returns true if the current NPV's value is less than or equal to the inputted NPV """

        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return self.shift_to(new_time).value < other.shift_to(new_time).value
    
    def __ge__(self, other): 
        """ Returns true if the current NPV's value is greater than or equal to the inputted NPV """

        # check type
        if not isinstance(other, NPV):
            raise TypeError("Only NPVs can be compared.")
            
        new_time = min(self.time, other.time)
        return self.shift_to(new_time).value > other.shift_to(new_time).value or self == other

def generate_annuity(periods, cash_flow, rate):
    """
    Creates an NPV object from an annuity payment. Requires

    Arguments:
    ----------
    periods : How many times the payment will be collected/made
    cash_flow : How much money is payed per period
    rate : rate of growth per period
    """
    new_NPV = NPV(0, 0, rate)
    for x in range(1, periods + 1):
        temp_NPV = NPV(x, cash_flow, rate).shift_to(0)
        new_NPV.value += temp_NPV.value
    return new_NPV