# Twitter analysis
An analysis of twitter data using 538's troll tweet database and twitter's streaming API.
(https://github.com/fivethirtyeight/russian-troll-tweets/)

The end goal is to create a classification model that can identify twitter tolls. Current POA:

- Clean and subset troll dataset to left and right political trolls
- Curate a list of twitter handles from legitimate political activists on twitter. Ideally a mix of politicians and pundits
- Use twitters streaming API to collect tweets from the legitimate activists
- Clean both datasets with basic NLP procedures
- Train a classification model on these datasets
- Deploy the model with some sort of user interface via flask