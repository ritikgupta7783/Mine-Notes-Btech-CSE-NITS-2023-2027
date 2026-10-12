# Interview Set 17.5 — Project Discussion Template

Use this structure for every ML project on your résumé. Be honest about what you implemented, measured, and personally contributed.

## 1. Problem and value
- What decision or prediction is being supported?
- Who will use the result?
- What is the target, sample and prediction horizon?
- Why is ML appropriate rather than a simple rule?

## 2. Data understanding
- Where did data come from and is the use/license appropriate?
- What do each row, feature and target represent?
- How many samples/features, missing values and duplicates?
- What leakage or sampling-bias risks existed?
- What information was available at prediction time?

## 3. Preprocessing and design
- Which columns were numeric, categorical, text or dates?
- How were missing values and categories handled?
- Were split and preprocessing leakage-safe?
- Why choose the algorithm and metric?
- What baseline was compared?

## 4. Evaluation and results
- Which data was used for fit, validation and final test?
- Which metrics were calculated and what do they mean?
- How did the selected model compare with baseline?
- Which errors were common?
- Were results measured by running code? If not, don't quote them as measured.
- What are the limitations or possible distribution shifts?

## 5. Improvements
Describe each improvement as hypothesis → change → fair evaluation → actual result → trade-off. Do not imply that tuning improved performance unless the experiment demonstrated it.

## 6. Engineering
- How are training and inference separated?
- Is preprocessing saved with the estimator?
- How is the model versioned and how are dependencies documented?
- What happens when an input is missing or has an unseen category?
- How would you monitor and roll back a failure?

## 7. One-minute project explanation
“I addressed [task] using [data]. The target was [y], and features were [X]. I first established [baseline], then used [preprocessing/model] because [reason]. I split data using [strategy] and evaluated with [metric] because [cost/reason]. The measured result was [actual result only], and the main limitation is [limitation]. My next improvement would be [specific experiment].”

Practise follow-up questions about leakage, model choice, metric choice, failed attempts and your own contribution.
