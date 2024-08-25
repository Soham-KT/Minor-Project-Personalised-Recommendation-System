import polars as pl

class DataLoader:
    _instance = None
    
    @staticmethod
    def getInstance():
        if DataLoader._instance is None:
            DataLoader._instance = DataLoader()
        return DataLoader._instance

    def __init__(self):
        if DataLoader._instance is not None:
            raise Exception('This is a singleton')
        self.data = pl.read_csv('Recommendation Engine/Data/final_movie_dataset.csv')
        
    def getData(self):
        return self.data
    
    
if __name__ == '__main__':
    df = DataLoader.getInstance()
    data = df.getData()
    print(data)