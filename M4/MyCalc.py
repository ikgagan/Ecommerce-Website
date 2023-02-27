class MyCalc:
# Created a class MyCalc
    ans = 0
    # Initially storing the variable ans as 0 becasue when the program 
    # starts for the first time ans wont have value and it will throw an error

    def _is_float(self, val):
    # Gagan Indukala Krishna Murthy - gi36 - 22nd feb 2023
    # Summary: _is_float is a function which checks if the given input is a float
    # we are using try except method in this function
    # _is_float is used in _as_number function
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
    # Gagan Indukala Krishna Murthy - gi36 - 22nd feb 2023
    # Summary: _is_int is a function which checks if the given input is a int 
    # we are using try except method in this function
    # _is_int is used in _as_number function
    # Gagan Indukala Krishna Murthy - gi36 - 22nd feb 2023
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
    # Gagan Indukala Krishna Murthy - gi36 - 22nd feb 2023
    # Sumamry: _as_number is a function which converts input of string of numbers into its respective datatype(ie. float or int)
    # line 38 is written to slove the bug which was existing in this code. 
    # It basically written to convert our final ans back to a string because if our ans is a float value python will convert the 
    # float value into int in the "if" condition(line 39 and 40) 
    # Main part of the function: In this function we are checking the if input val of string is a int, float or not a number.
    # According to which condition passes we will return the data type converted val to where ever the _as_number function is called.
        val = str(val)
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def add(self, num1, num2):
    # Gagan Indukala Krishna Murthy - gi36 - 23nd feb 2023
    # Summary: add is basically used for adding 2 numbers.
    # we are calling _as_number to convert the input val of string into its particular datatype.
    # if we are adding a number to the previous ans then the statement in "if" condition will run in a "while" 
    # loop below where there add function is called and the add function is executed again and the normal 
    # calculation(addition) in the "else" condition will returned as the final answer. 
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1+num2
        return self.ans

    def sub(self, num1, num2):
    # Gagan Indukala Krishna Murthy - gi36 - 23nd feb 2023
    # Summary: sub is basically used for subtracting 2 numbers.
    # we are calling _as_number to convert the input val of string into its particular datatype.
    # if we are subtracting a number to the previous ans then the statement in "if" condition will run in a "while" 
    # loop below where there sub function is called, then the main sub function is executed again and the normal 
    # calculation(subtraction) in the "else" condition will returned as the final answer.
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1-num2
        return self.ans

    def mult(self, num1, num2):
    # Gagan Indukala Krishna Murthy - gi36 - 23nd feb 2023
    # Summary: mult is basically used for Multiplying 2 numbers.
    # we are calling _as_number to convert the input val of string into its particular datatype.
    # if we are multiplying a number to the previous ans then the statement in "if" condition will run in a "while" 
    # loop below where there mult function is called and the mult function is executed again and the normal 
    # calculation(Multiplication) in the "else" condition will returned as the final answer.
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1*num2
        return self.ans

    def div(self, num1, num2):
    # Gagan Indukala Krishna Murthy - gi36 - 23nd feb 2023
    # Summary: div is basically used for dividing 2 numbers.
    # we are calling _as_number to convert the input val of string into its particular datatype.
    # if we are dividing a number to the previous ans then the statement in "if" condition will run in a "while" 
    # loop below where there div function is called and the div function is executed again and the normal 
    # calculation(division) in the "else" condition will returned as the final answer.
    # In div function we have another condition in which we are checking if the divisor is equal to 0
    # in that case we are printing "Can't divide by zero, sorry".
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1/num2
        return self.ans

# Gagan Indukala Krishna Murthy - gi36 - 23nd feb 2023
if __name__ == '__main__':
    is_running = True # used to keep the program running in while loop
    calc = MyCalc() 
    while is_running: # running the code in while loop so it doesnt exist after a single equation
        iSTR = input("What is your eq (To quit:q): ") # taking input from the user for the equation
        if iSTR == "quit" or iSTR == "q": # if the user enters quit or q the program will get terminated 
            print("Good Bye") # termination print statement
            is_running = False # triggers terminaion 
        else:
            print("Your eq was " + str(iSTR)) # this print statment prints the same equation which was given by the user
            if "+" in iSTR: # this condition runs if there is a '+' symbol in the input equation
                nums = iSTR.split("+") # the equation is split using .split() method into 2 parts keeping '+' as the reference and stored in array called nums
                # line - 129 and 130
                # r is the output if the equation
                # nums has the 2 numbers using which the addition has to be performed. 
                # we are calling it individually from the array as num[0] and and num[1] and striping to remove the all the spaces in that string
                # the striped values in sent to the add function
                r = calc.add(nums[0].strip(), nums[1].strip()) 
                print("Result is " + str(r)) # printing the final result to the user
            # must be done before - check to hanlde negative values
            elif "/" in iSTR: # this condition runs if there is a '/' symbol in the input equation
                nums = iSTR.split("/") # the equation is split using .split() method into 2 parts keeping '/' as the reference and stored in array called nums
                # line - 139 and 140
                # r is the output if the equation
                # nums has the 2 numbers using which the division has to be performed. 
                # we are calling it individually from the array as num[0] and and num[1] and striping to remove the all the spaces in that string
                # the striped values in sent to the div function
                r = calc.div(nums[0].strip(), nums[1].strip()) 
                print("Result is " + str(r)) # printing the final result to the user
            elif "*" in iSTR or "x" in iSTR: # this condition runs if there is a 'x' or '*' symbol in the input equation
                nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x") # the equation is split using .split() method into 2 parts keeping 'x' or '*' as the reference and stored in array called nums
                # line - 148 and 149
                # r is the output if the equation
                # nums has the 2 numbers using which the multiplication has to be performed. 
                # we are calling it individually from the array as num[0] and and num[1] and striping to remove the all the spaces in that string
                # the striped values in sent to the mult function
                r = calc.mult(nums[0].strip(), nums[1].strip())
                print("Result is " + str(r)) # printing the final result to the user
            # must be done last so negative numbers work
            elif "-" in iSTR: # this condition runs if there is a '-' symbol in the input equation
                iSTR = iSTR.replace(" ", "") # Removing all the white spaces from the string to remove complications while subtracting negative numbers. 
                if "--" in iSTR : # Here we are checking for if subtrahend is a negative number by checking if there is "--" in the string
                    nums = iSTR.split("--") # if the above condition passes then we are spliting the string using "--" as the refrence
                    nums[-1] = f"-{nums[-1]}" # since in the above line we removed the negative sign for the subtrahend, now we are adding it back again manually
                else:
                    nums = iSTR.rsplit("-",1) # the equation is split using .rsplit() method into 2 parts keeping '-' and length 1 as the reference and stored in array called nums
                # line - 158 and 159
                # r is the output if the equation
                # nums has the 2 numbers using which the subtraction has to be performed. 
                # we are calling it individually from the array as num[0] and and num[1] and striping to remove the all the spaces in that string
                # the striped values in sent to the sub function
                r = calc.sub(nums[0].strip(), nums[1].strip()) 
                print("Result is " + str(r)) # printing the final result to the user