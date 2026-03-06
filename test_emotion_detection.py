import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response['dominant_emotion'], 'joy')

    def test_anger(self):
        response = emotion_detector("I am mad about this")
        self.assertEqual(response['dominant_emotion'], 'anger')

    def test_sadness(self):
        response = emotion_detector("I am sad about this")
        self.assertEqual(response['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()
