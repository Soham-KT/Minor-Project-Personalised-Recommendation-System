import polars as pl
from data_loader import DataLoader
from sklearn.preprocessing import MultiLabelBinarizer

class MovieRecommendationEngine:
    def __init__(self) -> None:
        df = DataLoader.getInstance()
        self.data = df.getData()
        
        
    def getMovieRecommendation(self, preferred_genres: list, top_n: int = 20):
        recommendation = self.data.filter(
            pl.all_horizontal(
                pl.col(preferred_genres) == 1
            )
        )
        
        best_recommendation = recommendation.filter(
            pl.all_horizontal(
                pl.col('rating') == 5
            )
        )
        
        top_recommendation = best_recommendation['title'].head(top_n).to_numpy()
        
        return top_recommendation
    
if __name__ == '__main__':
    rec = MovieRecommendationEngine()
    genres = ['Action', 'Adventure']
    movies = rec.getMovieRecommendation(genres)
    
    print(f'Genres: {genres}')
    for i, movie in enumerate(movies):
        print(i + 1, movie)