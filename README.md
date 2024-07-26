# Data-Survivors-Capstone-Project
Capstone Project - Data Science

<h3>Present Working Model - Functioning_Model_3.0</h3>

<h3>Problem statement:</h3>

We aim to create a comprehensive pipeline of methodologies including database queries, key information extraction, similarity index comparison of human-written and AI-generated legal documents using an LLM to predict the likelihood of a legal text being AI generated.

<h3>Datasets:</h3>

Authentic Legal Documents: Authentic Washington case documents collected from Court Listener.

AI Generated Synthetic Data: Synthetic documents were generated using a different prompts and and temperatures Chat-GPT.

Risks and Challenges:

NER:
Although we expect NER to work as it normally does, that might not be the case in the legal domain, considering the different structurization of a few entities.
Mislabeling critical details like the case number, names of the judge, defendant, prosecutor etc., can prove to be a realistic problem.

MNB:
The assumption of independence between features (the Naïve assumption) may not hold in all cases, especially in the context of natural language, where word dependencies exist. However, the algorithm can still perform well in practice despite this simplification.
If the model encounters words in the test set that were not present in the training set (especially considering the wide range of vocabulary in the legal domain and the restricted resources we have, to implement this project), it assigns zero probability to these words, which can lead to issues.

SGD:
The model is very sensitive to learning rate, having a too high rate can cause the optimization to diverge, while a too low rate may lead to a slow convergence, or even get stuck in a local minima.

LightGBM:
It is prone to overfitting if it’s not properly tuned.
Performance heavily depends on tuning hyperparameters. Choosing the wrong parameters may lead to suboptimal results.
The model's performance is directly influenced by the quality of the input data. Noisy or biased data can negatively impact the model's predictions.

CatBoost:
While CatBoost has mechanisms to handle imbalanced data, achieving optimal performance in highly skewed datasets might still require careful tuning and potentially additional data preprocessing or sampling strategies.
