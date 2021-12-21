import math

class snailfish:
    def __init__(self, p, l, r):
        self.parent = p
        self.left   = l
        self.right  = r

    def __str__(self):
        return "[" + str(self.left) + "," + str(self.right) + "]"

    def __add__(self, other):
        new_snailfish = snailfish(None, self, other)
        self.parent  = new_snailfish
        other.parent = new_snailfish
        print("after addition: " + str(new_snailfish))
      
        # explode until there are no longer pairs which are 5 deep
        dp = new_snailfish.maxdepth() # get deepest pair
        while dp[0] > 4:
            dp[1].add("l", "u", dp[1].left)
            dp[1].add("r", "u", dp[1].right)
            
            # now set the correct value to 0
            if dp[1].parent.left == dp[1]:
                dp[1].parent.left = 0
            else:
                dp[1].parent.right = 0
            
            print("After explosion: " + str(new_snailfish))

            dp = new_snailfish.maxdepth() # get new deepest pair
        return new_snailfish

    def add(self, lr, ud, val):
        print("    Adding " + str(val) + " going" + (" up" if ud == "u" else " down") + (" left" if lr == "l" else " right"))
        print("    Self: " + str(self))
        print("    Parent: " + str(self.parent))

        if self.parent == None and ud == "u": # at the top
            #print("At the top - nothing to do")
            pass # we're at the top, so done
        else:
            # determine target
            if ud == "u":
                if lr == "l":
                    target = self.parent.left
                else:
                    target = self.parent.right
            else: # when going down, check the opposite side than where you're moving
                if lr == "l":
                    target = self.right 
                else:
                    target = self.left

            if ud == "u":
                if target != self:
                    if isinstance(target, int):
                        if lr == "l":
                            self.parent.left += val
                            if self.parent.left > 9:
                                child = snailfish(self.parent, math.floor(self.parent.left / 2),  math.ceil(self.parent.left / 2))
                                self.parent.left = child
                        else:
                            self.parent.right += val
                            if self.parent.right > 9:
                                child = snailfish(self.parent, math.floor(self.parent.right / 2),  math.ceil(self.parent.right / 2))
                                self.parent.right = child
                    else:
                        target.add("r" if lr == "l"else "l", "d", val)                
                else:
                    self.parent.add(lr, ud, val)
            else:
                if isinstance(target, int):
                    if lr == "r":
                        self.right += val
                        if self.right > 9:
                            child = snailfish(self.parent, math.floor(self.right / 2),  math.ceil(self.right / 2))
                            self.right = child
                    else:
                        self.left += val
                        if self.left > 9:
                            child = snailfish(self.parent, math.floor(self.left / 2),  math.ceil(self.left / 2))
                            self.left = child
                else:
                    self.right.add(lr, "d", val)
        print("    Parent after: " + str(self.parent))

    def depth(self):
        return 1 if self.parent == None else self.parent.depth() + 1

    def maxdepth(self):
        lm = [self.depth(), self] if isinstance(self.left, int) else self.left.maxdepth()
        rm = [self.depth(), self] if isinstance(self.right, int) else self.right.maxdepth()
        if rm[0] > lm[0]:
            return rm[0], rm[1] # only return the right side if it is highest

        else:
            return lm[0], lm[1] # else return left, so we start as far left as possible
    
def create_snailfish(i):
    ssn = snailfish(None, 0, 0) # start snailfish
    csn = ssn                   # current snailfish

    currentside = "l"
    for c in list(i)[1:]:
        # options: "[", "number", "]", ","
        if c == "[":
            cn = snailfish(csn, 0, 0) # create child, with current snailfish as parent
            if currentside == "l":    # update the child of the parent
                csn.left = cn      
            else:
                csn.right = cn
            csn = cn                  # set a new current snailfish
            currentside = "l"
        elif c.isdigit():
            if currentside == "l":
                csn.left = int(c)
            else:
                csn.right = int(c)
        elif c == ",":
            currentside = "r" # switch to processing the other side
        elif c == "]":
            csn = csn.parent
        else:
            print("PANIC! Found character " + c)
            quit()
    return(ssn)
        
input = open("input.1").read().splitlines()
input = open("input.2").read().splitlines()
print(input)

sns = [create_snailfish(i) for i in input]
result = sns.pop(0) 
for sn in sns:
    result += sn
print(result)


