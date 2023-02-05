# citation-screening
Using NLP Deep Learning Algorithms for systematic reviews. 

The aim of this project is to be able to reduce the workload of human reviewers drastically by having an algorithm that works for a small labelled sample set and still produce the best result. We also would like to create an algorithm that can be suited to multiple domains with the Inclusion Protocol serving as a seed.

## DataSet
The Data Set we will be using is the https://github.com/CLEF-TAR/tar dataset and the Pubmed doccumenr download will be from https://www.ncbi.nlm.nih.gov/books/NBK25497/#chapter2.Usage_Guidelines_and_Requiremen in the XML format and following strictly the Frequency, Timing and Regisgration of E-utility URL requests.

## Constraints
1. 3 requests per second
2. Large jobs are limited to 9PM to 5AM weekdays or Weekends.

Considering the constraints stated above we have made sure to follow the policy to the letter to avoid our IP address from being blocked. Hence, the custom settings for our SCRAPY spyder for both test and train document extraction has been properly handled to cater to the requirements.

At the time of writing this, 125,000 pubmed train document XML files have been downloaded in 13 hours and the pubmed test document xml is scheduled to be downloaded from 1 p.m, Sunday, 05 Feb 2023.
