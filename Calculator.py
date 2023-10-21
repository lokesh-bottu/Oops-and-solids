from DataExtractor import DataExtractor
from DataAnalyzer import DataAnalyzer
class Calculator:
    def __init__(self,ans,index1,index2,size,path):
            self.ans = ans
            self.index1 = index1
            self.index2 = index2
            self.size = size
            self.path = path
    def calculate(self):
            obj_Extractor = DataExtractor()
            data = obj_Extractor.extract(self.path)
            
            obj_analyzer = DataAnalyzer()
            lokesh = obj_analyzer.analyze(data,self.ans,self.index1,self.index2,self.size)
            return lokesh
