#include <iostream>

//#include "../Shark/include/shark/Data/Dataset.h"
//#include "../Shark/include/shark/Core/Exception.h/"

#include <shark/Data/Dataset.h>
#include <shark/Core/Exception.h>
#include "../Shark/build/include/shark/Core/Shark.h"

#include <shark/ObjectiveFunctions/Loss/SquaredLoss.h>
#include <shark/Models/LinearModel.h>
#include <shark/Algorithms/Trainers/LinearRegression.h>

using namespace shark;

int main() {
  // Create a toy dataset with 2 input features and 1 output
  Data<RealVector> dataset;
  dataset.inputs = {{0.1, 0.2}, {0.3, 0.4}, {0.5, 0.6}, {0.7, 0.8}};
  dataset.labels = {{0.3}, {0.6}, {0.9}, {1.2}};

  // Split the dataset into training and testing sets
  auto const [train, test] = splitAtElement(dataset, 2);

  // Define the linear regression model
  LinearModel<RealVector, RealVector> model(2);

  // Define the squared loss function
  SquaredLoss<RealVector, RealVector> loss;

  // Define the linear regression trainer
  LinearRegression trainer(loss);

  // Train the model on the training set
  trainer.train(model, train.inputs, train.labels);

  // Make predictions on the testing set
  auto predictions = model(test.inputs);

  // Print the predicted and actual values
  std::cout << "Predictions:\n" << predictions << "\n";
  std::cout << "Actual:\n" << test.labels << "\n";

  return 0;
}

