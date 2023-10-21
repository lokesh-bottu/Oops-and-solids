import sys
class DataAnalyzer:
    def analyze(self,data,ans,index1,index2,size):
        soln = sys.maxsize
        for lines in data:
            if(len(lines)>=size):
                dif = abs(int(lines[index1][:2]) - int(lines[index2][:2]))
                if(dif <soln):
                    soln = dif
                    day = lines[ans]
        return day
