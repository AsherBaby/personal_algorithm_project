// Prototype of Huffman codes algorithm
#ifndef __StanfordAlgo2__huffman__
#define __StanfordAlgo2__huffman__

#include <vector>
#include <string>

using std::vector;
using std::string;

class BinaryTree
{
    // Need to be defined
};
struct HuffmanCodes
{
    BinaryTree huffmanTree;
    vector<bool> binaryCode; // bit-friendly data structure
};

bool huffmanEncode(string asciiFile, string huffmanFile);
// asciiFile is the raw file
// huffmanFile is the encoded file

bool huffmanDecode(string huffmanFile, string asciiFile);
// huffmanFile is the encoded file
// asciiFile is the decoded file

#endif /* defined(__StanfordAlgo2__huffman__) */
