import unittest

class Point:

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
        
    def __str__(self):    # All we have done is renamed the method
            return "({0}, {1})".format(self.x, self.y)
            
    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
    def reflect_x(self):
        """Turn y to negative"""
        return Point(self.x, self.y * (-1))
        
    def slope_from_origin(self):
        """Return slope"""
        return float(self.y)/float(self.x)
        
    def get_line_to(self, target):
        """y = ax + b The coefficients a and b completely describe the line. Write a method in the Point class so 
        that if a point instance is given another point, it will compute the equation of the straight line joining the two points."""
        slope = (target.y - self.y) / (target.x - self.x)
        c = self.y - (self.x * slope)
        return (slope, c)

class SMS_store:
    def __init__(self, has_been_viewed = False, from_number = 0, time_arrived = 0, text_of_SMS = None):
        """ Create a SMS Message """
        self.has_been_viewed = has_been_viewed
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS
        
    def add_new_arrival(self):
        return SMS_store

a = Point()
my_inbox = SMS_store()
print my_inbox.has_been_viewed
