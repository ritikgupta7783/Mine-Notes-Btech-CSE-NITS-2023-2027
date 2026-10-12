# Project 4 — Customer Segmentation

**Task:** clustering. **Skills:** scaling, K-means, PCA and silhouette interpretation.

## Problem statement
Create groups from two numeric customer-like measures—annual spending and visits per year—without providing a customer label. The data is synthetic and purposely generated from different centres for demonstration.

## Key design
- Features: annual_spend and visits.
- No y target exists; K-means clusters X.
- Scaling ensures one feature's numeric range does not dominate Euclidean distance solely because it is measured at a larger scale.
- K is a modelling choice. In this synthetic exercise we know how data were generated, but for real data the intended segments need validation.

## Run
Install: python -m pip install numpy pandas scikit-learn matplotlib  
Run: python customer_segmentation.py

The script prints cluster counts and silhouette score, and opens a scatter plot if a GUI is available. The score alone does not prove that the clusters are useful business segments.

## Questions
1. Why does K-means require a choice of K?
2. Why scale the features?
3. What does silhouette measure at a high level?
4. Why are cluster labels nominal identifiers rather than ordered values?
5. Why should segments be interpreted with business/domain knowledge?

## Extensions
- Try K=2,3,4,5 and compare the inertia/elbow plot and silhouette.
- Test different seeds/initialisations.
- Use PCA to visualise a dataset with more than two features.
- Check whether segmentation remains stable across samples.
