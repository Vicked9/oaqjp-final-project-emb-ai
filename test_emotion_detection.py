import unittest
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectionTest(unittest.TestCase):
    def test_joy(self):
        response = emotion_detector('I am glad this happened')
        dominant_emotion = response['dominant_emotion']
        self.assertEqual('joy',dominant_emotion)
    
    def test_anger(self):
        response = emotion_detector('I am really mad about this')
        dominant_emotion = response['dominant_emotion']
        self.assertEqual('anger',dominant_emotion)
    
    def test_disgust(self):
        response = emotion_detector('I feel disgusted just hearing about this')
        dominant_emotion = response['dominant_emotion']
        self.assertEqual('disgust',dominant_emotion)
    
    def test_sadness(self):
        response = emotion_detector('I am so sad about this')
        dominant_emotion = response['dominant_emotion']
        self.assertEqual('sadness',dominant_emotion)
    
    def test_fear(self):
        response = emotion_detector('I am really afraid that this will happen')
        dominant_emotion = response['dominant_emotion']
        self.assertEqual('fear',dominant_emotion)

unittest.main()