class Pen:
    def p1(self):
        # Instance variable
        self.name='cello-faster'
        print(self.name)
    def p2(self):
        print(self.name)


object=Pen()
object.p1()
# cello-faster

object.p2()
# cello-faster

# another Syntax to calling the method
Pen.p2(object)
# cello-faster
