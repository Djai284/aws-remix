import unittest
from aws_remix import summary

class TestAWSRemixSummary(unittest.TestCase):
    def test_generate_full_summary(self):
        regions = ["us-east-1"]
        report = summary.generate_full_summary(regions)
        # Check that some major sections exist
        self.assertIn("EC2", report)
        self.assertIn("IAM", report)
        self.assertIn("S3", report)

if __name__ == '__main__':
    unittest.main()
