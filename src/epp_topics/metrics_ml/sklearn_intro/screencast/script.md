# Script: Intro to scikit-learn

### Loading datasets from scikit-learn

- This dataset was derived from the 1990 U.S. census; one row per census block group

- A block group is the smallest geographical unit for which the U.S. Census Bureau
  publishes sample data (a block group typically has a population of 600 to 3,000
  people).

- More
  [info](https://scikit-learn.org/1.5/datasets/real_world.html#california-housing-dataset)

- target variable is the median house value for California districts, expressed in
  hundreds of thousands of dollars (\$100,000).

______________________________________________________________________

# Train-test splits

- The function train_test_split lets you:

  - select the test set size

  - set random_state for reproducibility

______________________________________________________________________

# Basic scikit-learn steps

- Arrange data into a features matrix and target vector, split the data into training
  and test sets

- Choose a class of models by importing the appropriate estimator

- Set hyperparameters by instantiating this class

- Fit the model to your data by calling the `fit()` method on the model instance

- Apply the model to new data using the `predict()` method

- Evaluate the quality of predictions
