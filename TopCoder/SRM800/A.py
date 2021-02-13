class TIEFighterAssembly:
    def assemble(self, salvagedParts):
        a=salvagedParts.count('|')
        b=salvagedParts.count('-')
        c=salvagedParts.count('O')
        ans=min(a//2,b//2,c)
        return ans