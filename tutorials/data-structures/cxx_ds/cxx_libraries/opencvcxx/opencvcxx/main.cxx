#include <opencv2/opencv.hpp>
#include <filesystem>

using namespace cv;

//namespace fs = std::filesystem;
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

