import csv
import os

class SentimentClassifier:
    def __init__(self):
        self.tweets = []
        self.labels = []

    def load_data(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.tweets.append(row['tweets'])
                self.labels.append(row['labels'])

    def classify_sentiment(self):
        self.sentiments = []
        for label in self.labels:
            if label == "good":
                self.sentiments.append("good")
            elif label == "bad":
                self.sentiments.append("bad")
            else:
                self.sentiments.append("neutral")

    def save_to_csv(self):
        for sentiment in set(self.sentiments):
            tweets_sentiment = [tweet for tweet, sent in zip(self.tweets, self.sentiments) if sent == sentiment]
            labels_sentiment = [label for label, sent in zip(self.labels, self.sentiments) if sent == sentiment]

            with open(os.path.join("Code-Competance-1", f'sentiment_{sentiment}.csv'), 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["tweets", "labels"])
                for tweet, label in zip(tweets_sentiment, labels_sentiment):
                    writer.writerow([tweet, label])

    def summarize_counts(self):
        good_count = self.sentiments.count("good")
        bad_count = self.sentiments.count("bad")
        neutral_count = self.sentiments.count("neutral")

        with open(os.path.join("Code-Competance-1", 'sentiment_counts.csv'), 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Sentiment", "Count"])
            writer.writerow(["Good", good_count])
            writer.writerow(["Bad", bad_count])
            writer.writerow(["Neutral", neutral_count])


if __name__ == "__main__":
    classifier = SentimentClassifier()
    classifier.load_data('Code-Competance-1/data_source/file.csv')
    classifier.classify_sentiment()
    classifier.save_to_csv()
    classifier.summarize_counts()