## DATA

- Where are you getting the data from?
- Do you have enough?
- What format should it be stored in?
   - Database, filesystem, archive?
   - Is it dirty, clean?
- What reconciliation/ preprocessing needs to be applied?
- How will you get more or augment the data you have?
- Where do you store the preprocessed data?

## PIPELINE

- How does the training pipeline look?
- How much data do you need to train on?
- How are you going to feed the data to your model?
  - If you need to train in on 10x more data, how might you train the model in a distributed way?
- How do you judge if you have trained a successful model?
- How will you do hyperparameter optimization?

## MODEL

- What is the simplest possible way/heuristic of solving this?
- What's the minimal model you'd want to construct to solve this task?
- Do you need a more complicated approach? What are the tradeoffs?
- If using Deep Learning, what kind of approach? What rea the tradeoffs?
- Do you need to worry about regularization?

## SERVING

- How is your model served?
- If your model results in a product, how is it accessed by the main application?
- How is the model kept up to date?
- How do you store model backups?
- Would it scale to hundreds of thousands of customers?
- What is a reasonable time for your model to answer your hypothesis?
- Does that include pre-processing the data?
- How long does inference last? How can you make it shorter?
- How do you test and validate the answers your model produces? 
