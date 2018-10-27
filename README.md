# Bus Lines Categorization

This is the second assignment of "Data Mining" course (spring 2018).

**Requirements:**
  * [Jupyter Notebook](http://jupyter.org/install)
  * [scikit learn](http://scikit-learn.org/stable/install.html)
  * [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)
  * [numpy](https://docs.scipy.org/doc/numpy/user/install.html)
  * [gmplot](https://pypi.org/project/gmplot/)
  * [fastdtw](https://pypi.org/project/fastdtw/)
  * [haversine](https://pypi.org/project/haversine/)
  
**Dataset format:**

![img not found](https://github.com/giorgospan/BusLinesCategorization/blob/master/figure.png "Dataset Format")

  * **Part 1:** The purpose of this part is to familiarize us with the use of gmplot python library by visualizing 5 different bus lines (i.e: journeyPatternIDs). 
  
  * **Part 2:** For every bus line(i.e: trajectory) in test_set_a1.csv we need to find its 5 neighbors* from the train_set.csv file. We utilize Dynamic Time Warping ([DTW](https://en.wikipedia.org/wiki/Dynamic_time_warping)) as similarity measure between two trajectories.
  
  * **Part 3:** In this part we do the same as the in the previous part with the exception of utilizing Longest Common Subsequence ([LCS](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)) as similarity measure this time.
  
  * **Part 4:** The main task of this part is to predict the bus line that each trajectory in test_set_a2.csv is part of. For this purpose we create a typical KNN-Classifier. 
  
Multiprocessing is achieved using Python's multiprocessing module.  
train_set.csv file will be uploaded soon.



\* By "neighbors" we mean the 5 most similar trajectories to the one currently being tested.
