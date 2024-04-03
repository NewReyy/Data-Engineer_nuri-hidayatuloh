import csv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Sentiment(Base):
    __tablename__ = 'sentiments'

    sentiment_id = Column(Integer, primary_key=True)
    sentiment_label = Column(String(20), unique=True)

class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    text = Column(String(280))
    sentiment_id = Column(Integer, ForeignKey('sentiments.sentiment_id'))

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def insert_from_csv(self, csv_file):
        Session = self.Session()
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                text = row['tweets']
                label = row['labels']
                
                # Assign sentiment_id based on label
                if label == 'good':
                    sentiment_id = 2
                elif label == 'bad':
                    sentiment_id = 3
                else:
                    sentiment_id = 1  # Default to neutral
                
                # Insert sentiment if not exists
                sentiment = Session.query(Sentiment).filter_by(sentiment_id=sentiment_id).first()
                if not sentiment:
                    sentiment = Sentiment(sentiment_id=sentiment_id, sentiment_label=label)
                    Session.add(sentiment)
                    Session.commit()

                # Insert tweet
                tweet = Tweet(text=text, sentiment_id=sentiment_id)
                Session.add(tweet)
                Session.commit()

        Session.close()


if __name__ == "__main__":
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    DB_NAME = 'db_sentiment_gpt'
    db_url = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    
    db_manager = DatabaseManager(db_url)
    db_manager.create_tables()
    db_manager.insert_from_csv('data_source/file.csv') 