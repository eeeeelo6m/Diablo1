import effect

class Effect_slow(effect.Effect):
    def __init__(self,igroc,strong,long=2):
        effect.Effect.__init__(self, self.deystvie, 'picture/эфект_slow.png',long)

        self.igroc=igroc
        self.strong=strong
        self.deystvie()


    def deystvie(self):
        self.igroc.stamina-=self.strong