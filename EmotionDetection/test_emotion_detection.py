from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        case1 = emotion_detector("I am glad this happened")
        self.assertEqual(case1['dominant_emotion'], case1['joy'])
        case2 = emotion_detector("I am really mad about this")
        self.assertEqual(case2['dominant_emotion'], case2['anger'])
        case3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(case3['dominant_emotion'], case3['disgust'])
        case4 = emotion_detector("I am so sad about this")
        self.assertEqual(case4['dominant_emotion'], case4['sadness'])
        case5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(case5['dominant_emotion'], case5['fear'])
        

if __name__ == '__main__':
    unittest.main() 