class SlotMachineHacking:
    def win(self, reels, steps):
        reels=list(reels)
        steps=list(steps)
        for i in range(len(steps)):
            steps[i]%=len(reels[i])
        ans=[]
        for i in range(len(steps)):
            ans.append(1)
            step = steps[i]
            while reels[i][steps[i]]!='c':
                if ans[-1]>=11:
                    ans[-1]=-1
                    break
                else:
                    ans[-1]+=1
                    steps[i]+=step
                    steps[i]%=len(reels[i])
        if -1 in ans:
            return -1
        while min(ans)!=max(ans):
            i=ans.index(min(ans))
            ans[i]+=len(reels[i])
        return ans[0]-1