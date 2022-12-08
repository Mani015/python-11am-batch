class Pen:
    def p1(self):
        name='cello-faster'
        print(name)
    def p2(self):
        print(name)


object=Pen()
object.p1()
# cello-faster

object.p2()
# NameError: name 'name' is not defined