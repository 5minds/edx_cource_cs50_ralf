import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = []
        self.negatives = []
        with open(positives) as lines:
            for line in lines:
                if line[0].isalpha():
                    line = line.rstrip()
                    self.positives.append(line)
        with open(negatives) as lines:
            for line in lines:
                if line[0].isalpha():
                    line = line.rstrip()
                    self.negatives.append(line)

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score = 0
        tknzr = nltk.TweetTokenizer(strip_handles=True, reduce_len=True)
        text = tknzr.tokenize(text.lower())
        
        for word in text:
            for compareWord in self.positives:
                if word == compareWord:
                    score += 1
        for word in text:
            for compareWord in self.negatives:
                if word == compareWord:
                    score -= 1
        return score
