from EmotionDetection.emotion_detection import emotion_detector
import unittest 

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        return self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"], 
            "joy")
    
    def test_anger(self):
        return self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"], 
            "anger")
    
    def test_disgust(self):
        return self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], 
            "disgust")

    def test_sadness(self):
        return self.assertEqual(
            emotion_detector("I am so sad about this")["dominant_emotion"], 
            "sadness")
    
    def test_fear(self):
        return self.assertEqual(
            emotion_detector("I am really afraid that this will happen")["dominant_emotion"], 
            "fear")
    

if __name__ == '__main__':
    unittest.main()
