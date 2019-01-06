import pyxel
alphaChanel = 11
charset = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'.':26,':':27,'!':28,'?':39,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
s = 0
class App:
    def __init__(self):
        pyxel.init(160, 120,caption='レトロゲー',scale=4,fps=60)
        pyxel.image(0).load(0,0, 'res/font.png')
        pyxel.image(1).load(0,0, 'res/sf00.png')
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
#        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(1)
#        pyxel.rect(self.x, 0, self.x + 7, 7, 9)
#        pyxel.text(55, 41, "Hello world!", 16)
#        pyxel.blt(0,0,0,0,0,8,8,alphaChanel)
#        pyxel.blt(80,60,1,0,0,16,16,alphaChanel)
        self.char()
        self.score(self.char(),50,2)
        self.text("SCORE:",2,2)

    def char(self):
        x = pyxel.mouse_x
        y = pyxel.mouse_y

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            pyxel.blt(x,y,1,0,0,16,-16,alphaChanel)
            global s
            s += 1
        else:
            pyxel.blt(x,y,1,0,0,16,16,alphaChanel)
        
        return str(s)
        
    def text(self,text,x,y):
        for i in range(len(text)):
            pyxel.blt(x+i*8,y,0,charset[text[i]]*8,0,8,8,alphaChanel)

    def score(self,s,x,y):
        for i in range(len(s)):
            pyxel.blt(x+i*8,y,0,charset[s[i]]*8,8,8,8,alphaChanel)


App()