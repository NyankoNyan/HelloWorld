class Cow:

    def __init__(self, name):
        self.name = name

    def get_art(self):
        return self.name + """
\|/          (__)    
     `\------(oo)
       ||    (__)
       ||w--||     \|/
   \|/        
        """


cow1 = Cow( "Бурёнка" )

print(cow1.get_art())