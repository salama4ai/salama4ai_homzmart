# salama4ai_homzmart
![Screenshot](homzmart.png)
The assessment task solution of the machine-learning vacation at homzmart company in march-2022 by Ahmed Salama
"Al _ ML Engineer - Assignment.pdf"

# installation of elasticsearch&kibana
this link https://dev.to/elastic/downloading-elasticsearch-and-kibana-macos-linux-and-windows-1mmo
contains more details

run ```curl https://localhost:9200``` to ensure that setup is done correctly

run ```bin\elasticsearch-create-enrollment-token.bat --scope kibana``` from the elastic directory to creates enrollment tokens for Elasticsearch nodes and Kibana instances, or you can find it in the CMD of the setup

i used the bulk API Helper to index all the data, and flask API 

note: regarding ibm-watson tone analyzer it's unavailable for new users -like my case- as of 24-feb-2023



Elasticsearch is a distributed, free and open search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. Elasticsearch is built on Apache Lucene. Known for its simple REST APIs, distributed nature, speed, and scalability, Elasticsearch is the central component of the Elastic Stack, a set of free and open tools for data ingestion, enrichment, storage, analysis, and visualization. Once indexed in Elasticsearch, users can run complex queries against their data and use aggregations to retrieve complex summaries of their data

The speed and scalability of Elasticsearch and its ability to index many types of content mean that it can be used for a number of use cases:

    Application search
    Website search
    Enterprise search
    Logging and log analytics
    Infrastructure metrics and container monitoring
    Application performance monitoring
    Geospatial data analysis and visualization
    Security analytics
    Business analytics






