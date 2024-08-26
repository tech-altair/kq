# Sentiment Analysis Solution for Kenya Airways
# Overview of System: 
The sentiment analysis solution is designed to gather, analyze, and present customer feedback from various online platforms. The primary goal is to extract insights from social media and travel review sites to understand customer sentiments toward the airline’s services. 

# System Architecture: 
The solution is gotten from first understanding the system design. The system comprises of several components; the data ingestion layer which is responsible for the data collection processes made possible via APIs or webscraping, the data storage layer which is responsible for storing structured (processed) and unstructured (pre-processed) data, the data processing layer is responsible for performing the sentiment analysis on the data, the data pipeline which orachestrates the ETL data flow for a smooth experience and the presentation layer responsible for the visual aspects of the sentiments. Security is integrated to all the layers to provide protection. 

# UX/UI design:
This step ensured that the data is presented to the users in a user-friendly manner. It's simple yet professional giving the users a comfortable and easy experience in accessing the system. Find link [here](https://www.figma.com/design/aW4y44FrMp1kq3GVuohP6t/KQ?node-id=0-1&t=1ZIjp5sfj0isziAV-1)

# Running the system:
1. Activate venv

`source venv/bin/activate 
`

2. In the backend directory run the Flask app

```
cd/backend/api
python3 app.py
```

3. In the frontend directory run the React app

```
cd frontend/sentiment-dashboard
npm start
```

4. Trigger the data pipeline to start the ETL process

```
cd backend/data_pipeline
python pipeline.py
```

5. Install the extension vscode-pdf (optional) where needed to access the report
  
# Note
There's room for adjustments and improvements in the overal solution 
