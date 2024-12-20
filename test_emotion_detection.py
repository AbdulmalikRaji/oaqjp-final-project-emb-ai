from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        #joy test
        test1 = emotion_detector("I am glad this happened")
        self.assertEqual(test1['dominant_emotion'], 'joy')

        #anger test
        test2 = emotion_detector("I am really mad about this")
        self.assertEqual(test2['dominant_emotion'], 'anger')

        #disgust test
        test3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test3['dominant_emotion'], 'disgust')

        #sadness test
        test4 = emotion_detector("I am so sad about this")
        self.assertEqual(test4['dominant_emotion'], 'sadness')

        #fear test
        test5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test5['dominant_emotion'], 'fear')


unittest.main()