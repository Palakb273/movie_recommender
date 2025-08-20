import pandas as pd
import numpy as np
class Movie_recommender:
    def __init__(self,feature_csv,metadata_csv):
        self.features=pd.read_csv(feature_csv)
        self.movies=pd.read_csv(metadata_csv)
        self.id_to_title=dict(zip(self.features["id"],self.features["title_x"]))
        self.title_to_id=dict(zip(self.features["title_x"],self.features["id"]))
        self.feature_matrix=self.features.drop(columns=["id","title_x"]).values
        self.feature_matrix=self.feature_matrix/np.linalg.norm(self.feature_matrix,axis=1,keepdims=True)#normalize feature vectors for cosine similariity
    def cosine_similarity(self,vec1,vec2):
        return np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))
    def recommend(self,movie_title,top_n):
        if movie_title not in self.title_to_id:
            print(f"{movie_title} not found in dataset!")
            return[]
        movie_id=self.title_to_id[movie_title]
        idx=self.features.index[self.features["id"]==movie_id][0]
        target_vec=self.feature_matrix[idx]
        scores=[]
        for i,vec in enumerate(self.feature_matrix):
            if i==idx:
                continue
            sim=self.cosine_similarity(target_vec,vec)
            scores.append((i,sim))
        scores=sorted(scores,key=lambda x:x[1],reverse=True)
        top_indices=[i for i,_ in scores[:top_n]]
        recommendations=[(self.features.iloc[i]["title_x"],round(sim,3))
                         for i,sim in scores[:top_n]]
        return recommendations
if __name__=="__main__":
    recommender=Movie_recommender(
        feature_csv="C:/Users/palak/OneDrive/Desktop/movie_analysis/feature_movie.csv",
        metadata_csv="C:/Users/palak/OneDrive/Desktop/movie_analysis/clean_movies.csv",)
    while True:
        movie=input("enter a movie(quit to exit)")
        if movie.lower()=="quit":
            print("exiting....")
            break
        n=int(input("number of recommendations"))
        recs=recommender.recommend(movie,top_n=n)
        if recs:
            print(f"because you liked {movie},you may also enjoy:")
            for i,(title,score)in enumerate(recs,1):
                print(f"{i}. {title} (similarity:{score})")
                
    
        
