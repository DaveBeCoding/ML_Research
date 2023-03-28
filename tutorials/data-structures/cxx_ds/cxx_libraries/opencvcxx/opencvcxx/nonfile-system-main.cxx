#include <opencv2/opencv.hpp>

using namespace cv;

int main() {
    Mat img = imread("vskater.jpg", IMREAD_GRAYSCALE);

    if (img.empty()) {
        std::cerr << "Error: Could not read image file." << std::endl;
        return -1;
    }

    Mat enhanced_img;
    equalizeHist(img, enhanced_img);

    Mat diff;
    absdiff(img, enhanced_img, diff);

    Mat side_by_side(img.rows, img.cols * 2, img.type());
    img.copyTo(side_by_side(Rect(0, 0, img.cols, img.rows)));
    enhanced_img.copyTo(side_by_side(Rect(img.cols, 0, img.cols, img.rows)));
    imshow("Original vs Enhanced", side_by_side);

    imshow("Matrix Value Difference", diff);

    waitKey(0);

    return 0;
}

