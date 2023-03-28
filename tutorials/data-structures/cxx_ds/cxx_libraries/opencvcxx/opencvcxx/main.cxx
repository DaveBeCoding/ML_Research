#include <opencv2/opencv.hpp>

using namespace cv;

int main()
{
    Mat img = imread("v-skater.jpeg"); // load input image
    Mat sharpeningKernel = (Mat_<float>(3,3) << 0, -1, 0, -1, 5, -1, 0, -1, 0); // sharpening kernel
    Mat sharpenedImg;

    filter2D(img, sharpenedImg, -1, sharpeningKernel); // apply filter to image

    namedWindow("Input Image", WINDOW_NORMAL);
    namedWindow("Sharpened Image", WINDOW_NORMAL);

    imshow("Input Image", img);
    imshow("Sharpened Image", sharpenedImg);
    waitKey(0);

    return 0;
}
