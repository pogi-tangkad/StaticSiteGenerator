import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("----------------------------------------------")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        print(self.assertEqual(node, node2))

        print("----------------------------------------------")
        node3 = TextNode("This is a text node", TextType.BOLD, "http://www.test.net")
        print(self.assertNotEqual(node, node3))

        print("----------------------------------------------")
        print(self.assertUrlIsNone(node))



    def assertEqual(self, node, node2):
        print(f"Assert Equal Test: \n{node}\n{node2}")
        return node == node2

    def assertNotEqual(self, node, node2):
        print(f"Assert Not Equal Test:\n{node}\n{node2}")
        return not node == node2

    def assertUrlIsNone(self, node):
        print(f"Assert Url is None:\nNode Url = {node.url}")
        return node.url == None


if __name__ == "__main__":
    unittest.main()
