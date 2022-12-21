import  time
class Clock:

    def d1(self):
        try:
            print("Start Clock")
            while True:
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S:%p", localtime)
                print(result)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stop Clock")

c = Clock()
c.d1()
