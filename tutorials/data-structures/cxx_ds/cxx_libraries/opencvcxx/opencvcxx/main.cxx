#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main() {
    // Load the image
    Mat img = imread("vskater.jpg", IMREAD_GRAYSCALE);
    
    if (img.empty()) {
        cerr << "Error: Could not read image file." << endl;
        return -1;
    }

    // Enhance the image using histogram equalization
    Mat enhanced_img;
    equalizeHist(img, enhanced_img);

    // Display the original and enhanced images
    namedWindow("Original Image", WINDOW_AUTOSIZE);
    imshow("Original Image", img);
    namedWindow("Enhanced Image", WINDOW_AUTOSIZE);
    imshow("Enhanced Image", enhanced_img);

    // Wait for a key press
    waitKey(0);

    return 0;
}

