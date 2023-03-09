# Identify Bugs *Early* in your Software Projects
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c5/The_Early_Bird..._%28165702619%29.jpg" width="250">


## 1. Setup

Clone this repository to your local environment
`pip install requirements.txt` (requires python 3+)

## 2. Usage
The main function just takes one input: repository_url (string) 

Run: `main.py <paste your git based repository url for which you wish to classify the commits>`

Output: Writes `predictions.csv` in the current working directory. 

## References

This repository is developed based on the research (and code) by:

* [Shrikanth, N. C.](https://snaraya7.github.io/), Suvodeep Majumder, and Tim Menzies. "Early life cycle software defect prediction. why? how?." 2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE). IEEE, 2021.

* [Shrikanth, N. C.](https://snaraya7.github.io/), and Tim Menzies. "Assessing the Early Bird Heuristic (for Predicting Project Quality)." ACM Transactions on Software Engineering and Methodology (2023).

* Rosen, Christoffer, Ben Grawi, and Emad Shihab. "Commit guru: analytics and risk prediction of software commits." Proceedings of the 2015 10th joint meeting on foundations of software engineering. 2015.
