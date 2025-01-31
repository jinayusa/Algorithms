# Huffman Coding Implementation in Python

import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    """Node class for the Huffman Tree"""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for priority queue (Min-Heap)
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    """
    Function to build Huffman Tree from input text.
    :param text: Input string
    :return: Root node of Huffman tree
    """
    if not text:
        return None

    # Step 1: Calculate frequency of characters
    frequency = Counter(text)

    # Step 2: Create Min-Heap Priority Queue
    min_heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(min_heap)

    # Step 3: Build Huffman Tree
    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)  # Remove least frequent
        right = heapq.heappop(min_heap)  # Remove second least frequent
        merged = HuffmanNode(None, left.freq + right.freq)  # Merge two nodes
        merged.left, merged.right = left, right
        heapq.heappush(min_heap, merged)  # Insert merged node back into heap

    return min_heap[0]  # Root node of Huffman Tree

def generate_huffman_codes(root, current_code="", huffman_codes={}):
    """
    Function to generate Huffman codes from Huffman Tree.
    :param root: Root node of Huffman Tree
    :param current_code: Current Huffman code (prefix)
    :param huffman_codes: Dictionary storing character codes
    """
    if root is None:
        return

    if root.char is not None:  # Leaf node
        huffman_codes[root.char] = current_code
        return

    generate_huffman_codes(root.left, current_code + "0", huffman_codes)
    generate_huffman_codes(root.right, current_code + "1", huffman_codes)

def huffman_encoding(text):
    """
    Function to encode input text using Huffman Coding.
    :param text: Input string
    :return: Encoded string, Huffman tree
    """
    root = build_huffman_tree(text)
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)
    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    """
    Function to decode Huffman encoded text.
    :param encoded_text: Encoded binary string
    :param root: Root node of Huffman Tree
    :return: Decoded original text
    """
    decoded_text = []
    node = root

    for bit in encoded_text:
        node = node.left if bit == "0" else node.right

        if node.char is not None:  # Leaf node reached
            decoded_text.append(node.char)
            node = root  # Reset to root

    return "".join(decoded_text)


# Example Usage:
text = "AAABBC"
encoded_text, tree = huffman_encoding(text)
decoded_text = huffman_decoding(encoded_text, tree)

print(f"Original Text: {text}")
print(f"Encoded Text: {encoded_text}")
print(f"Decoded Text: {decoded_text}")
