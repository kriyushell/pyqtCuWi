
#           Custom Widgets For PyQt5 Module           #
#                 GPL 3.0 - myygunduz                 #
#      https://github.com/myygunduz/custom-widgets    #

class NoIcon(Exception):
    def __init__(self,operation): 
        super().__init__(f"\n\nError Message:\n'''\n{operation}\n'''")