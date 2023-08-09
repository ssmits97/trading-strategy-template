These are my informal notes to write down my assumption, line of thinking, and improvements.

We are interested in creating a simple trading strategy on the S&P500 as a showcase.
Let's start with some simple S&P500 data from https://datahub.io/core/s-and-p-500

The raw dataset looks quite good, I don't think there is much cleaning required.
There are some missing NaN values, you can remove those observations, forward fill, fill with a fixed value.

Let's do some basic features from the dataset, do a simple log, and start predicting returns.
Down te line, we might add technical features like MA, RSI, and maybe some alternative data.

We need to split the data into pieces, let's go for a 60/40 train prediction split.
Normally, I would recommend an 80/20 train/test split, with the training set having a 60/40 train/validation split.
We split in time, however, since these are timeseries, we now created a time bias.

Our OLS really does not work, we might consider using a binary classifier and predict the sign of the return.

However, let's do a simple trading strategy on our trained model
We assume no transaction cost, no delay, etc, etc, etc. <- this leaves a lot of room for improvement.
This strategy does not work, as expected, the OLS holds 0 predictive power.

Now that our 0 to 1 is set up, let's go over all assumptions/ideas we got along the way and try again.