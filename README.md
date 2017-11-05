# movie-clustering
In this project, I use unsupervised learning models (k-means and lda) to cluster Top 250 movies crawled from IMDB into different groups, visualize the results and identify their latent topics/structures. The first part is to scrape data of movie synopses from IMDB; and then train unsupervised machine learning models to do clustering.
## Requirements
This project requier several python packages including: 
* BeautifulSoup 
* sklearn 
* lda
* nltk
## Usage
* Run `python crawler.py` to scrape movie synopses from IMDB top 250 movies. This will create a new folder data under current directory. Two files synopses.txt and titles.txt will be create inside data.
* Run movie-clustering to read the scraped data and cluster movies. Two plots will be generated to visulize the clustering results.
## Extending this
If you want to extend this, here are a fews places to start:
* Scrape more movie synopses or from other website such as wiki.
* Generate different features when doing tf-idf by setting different parameters.
