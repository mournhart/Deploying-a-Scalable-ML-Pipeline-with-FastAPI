# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model used is RandomForestClassifier with hyperparameters tuned by GridSearchCV.

## Intended Use
The model is part of the course project for Udacity's Machine Learning DevOps on census data. Results not intended for real decision making.

## Training Data
The training data came from the 1994 Census database. Features in the dataset are used to predict a person's salary. The data was split into a 80/20 train/test split.

## Evaluation Data
The model was evaluated on 20% of the dataset.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model was evaluated using precision, recall, and F1 score on the test set split from the dataset.

Feature slices were also evaluated. Of these, "education = Prof-school" had an F1 score of 0.8820, "education = Doctorate" had an F1 score of 0.8544, while, "occupation = Exec-managerial" had an F1 score of 0.8071.

There is also a different in scores between the "sex" category.
"sex = Female" has an F1 of 0.6021.
"sex = Male" has and F1 of 0.6959.

## Ethical Considerations
Given historical and cultural differences, some of the observations from the income differences may reflect biases prevalent in 1994.

## Caveats and Recommendations
A model trained on more recent data may show the changing landscape of these inequalities or biases.
