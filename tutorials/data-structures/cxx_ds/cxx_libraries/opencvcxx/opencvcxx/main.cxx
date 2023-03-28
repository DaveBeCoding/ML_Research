/*
     
                                           histogram equation

**Compute the image histogram: Calculate the histogram of the image, which is a plot of the frequency of occurrence of each pixel intensity value in the image.

**Compute the cumulative distribution function (CDF): Calculate the cumulative distribution function of the histogram, which is a function that maps each pixel intensity value to a new intensity value.

**Compute the new intensity values: Using the CDF, calculate the new intensity value for each pixel in the image.
Update the image: Replace each pixel in the image with its corresponding new intensity value.
 
*/


#include <opencv2/opencv.hpp>
#include <filesystem>

using namespace cv;

namespace fs = std::__fs::filesystem;

int main() {
    // Load the image
    Mat img = imread("vskater.jpg", IMREAD_GRAYSCALE);

    if (img.empty()) {
        std::cerr << "Error: Could not read image file." << std::endl;
        return -1;
    }

    // Enhance the image using histogram equalization
    Mat enhanced_img;
    equalizeHist(img, enhanced_img);

    // Compute the matrix value difference between the two images
    Mat diff;
    absdiff(img, enhanced_img, diff);

    // Display the original and enhanced images side by side
    Mat side_by_side(img.rows, img.cols * 2, img.type());
    img.copyTo(side_by_side(Rect(0, 0, img.cols, img.rows)));
    enhanced_img.copyTo(side_by_side(Rect(img.cols, 0, img.cols, img.rows)));
    imshow("Original vs Enhanced", side_by_side);

    // Save a copy of the "Original vs Enhanced" image in a directory named "output-image"
    fs::path output_dir("../output-image");
    if (!fs::exists(output_dir)) {
        fs::create_directory(output_dir);
    }
    fs::path output_path = output_dir / "original_vs_enhanced.jpg";
    imwrite(output_path.string(), side_by_side);

    // Display the matrix value difference between the two images
    imshow("Matrix Value Difference", diff);

    // Wait for a key press
    waitKey(0);

    return 0;
}

