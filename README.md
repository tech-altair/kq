# Solution 1.
Scraping KQ customer reviews from TrustPilot website.

  ### Scrapper file:
   - `scrapper.py` - This is for scrapping data from the source website (Trustpilot website)
        - Libraries used: ``Requests`` , ``BeautifulSoup`` , ``Pandas``
         
  ### Sentiment analysis file:
   - `sentiment-analysis.py` - This is for cartegorizing customer reviews.
        - Libraries used: ``Requests`` , ``BeautifulSoup`` , ``Pandas`` and ``transformers`` About pipeline here:<https://huggingface.co/transformers/v3.0.2/main_classes/pipelines.html>

  ### Data pipeline file:
    - `pipeline.py` - For automation of scraping, sentiment-analysis and storing the data.
        - Libraries used: ``Requests`` , ``BeautifulSoup`` , ``Pandas`` and ``vaderSentiment`` <https://vadersentiment.readthedocs.io/en/latest/>


## Frontend:
 - A simple UI developed using `HTML/CSS/JS`

## Backend:
 - API developed using Django Rest Framework (DRF)
    - Has the following endpoints: 
       ``{{BASE_URL}}/api/reviews/`` - for listing reviews
       ``{{BASE_URL}}/api/scrape/`` - for scraping reviews 


# How to set up the project libraries
 - Create virtual env: `python -m venv .yourEnv` and activate it `source .yourEnv/bin/activate`
 - Install project requirements: `pip install -r requirements.txt`
 - Runserver: `python manage.py runserver`
 - To see the dashboard, visit: `http://127.0.0.1:8000/dashboard`


 - PR Link: <https://github.com/mutemip/kq/tree/feature/sentiment-analysis>

 - Project Documentation: <https://docs.google.com/document/d/1Hf39yE6rT_aOvxawuOb_U3QViuEnE5xLpMTDMi-wC1E/edit?usp=sharing>

========================================================================================



# Problem Description: Sentiment Analysis Solution for Kenya Airways
# Background: 
Kenya Airways is looking to improve its overall travel experience by analyzing customer feedback from social media and travel review sites. Your task is to develop a sentiment analysis solution that scrapes relevant data, processes it, and provides insights into customer sentiments regarding the airline's services.

# Objective: 
You are required to develop a system that scrapes social media platforms and travel review sites for mentions of Kenya Airways, performs sentiment analysis on the collected data, and presents the findings in a user-friendly manner.

# Instructions:
    1. Repository Setup:
        ◦ Fork the provided GitHub repository containing the problem description.
        ◦ Clone the forked repository to your local machine.
    2. Branching:
        ◦ Create a new branch from the main branch named feature/sentiment-analysis.
    3. Implementation:
        ◦ Data Scraping: Implement a solution that scrapes data from at least two social media platforms and one travel review site for mentions of Kenya Airways.
        ◦ Sentiment Analysis: Use natural language processing (NLP) techniques to analyze the sentiments expressed in the scraped data. The analysis should categorize sentiments into positive, negative, or neutral.
        ◦ Data Pipeline: Design a data pipeline that automates the scraping, analysis, and storage of results.
        ◦ System Design: Consider how your system handles scalability, error handling, and system security (e.g., API key management, rate limiting).
        ◦ Frontend Development: Build a simple dashboard that displays the sentiment analysis results. It should include visualizations like charts or graphs that provide insights into customer sentiments over time.
        ◦ Backend Development: Develop the backend API that handles the data scraping, processing, and serves the analyzed data to the frontend.
        ◦ User Experience: Ensure that the dashboard is user-friendly, with a focus on clarity and ease of navigation.
    4. Documentation:
        ◦ Clearly document your code and provide a README.md file that explains how to set up and run your solution.
        ◦ Include instructions for how to use the data scraping and sentiment analysis features, and describe any assumptions or limitations of your solution.
    5. Submission:
        ◦ Push your branch feature/sentiment-analysis to the forked GitHub repository.
        ◦ Create a pull request (PR) from your branch to the main branch in the forked repository.
        ◦ Attach any relevant documentation, links, or notes to the PR.
        ◦ Send a short video clip (maximum 5 minutes) via WhatsApp, explaining your work and demonstrating how to use your solution. The video should be submitted by 11:00 AM on the submission day.
    6. Evaluation Criteria:
        ◦ Version Control: Proper use of Git branching, commits, and pull requests.
        ◦ Data Pipeline: Robustness and efficiency of the data scraping and sentiment analysis pipeline.
        ◦ System Design: Scalability, security, and overall architecture of the solution.
        ◦ Frontend/Backend Development: Quality, functionality, and user experience of the dashboard and backend API.
        ◦ Documentation: Clarity, thoroughness, and organization of the documentation.
        ◦ Presentation: Clarity and conciseness of the video explanation.

# Deadline:
    • Code Submission: Monday at 10:00 AM.
    • Video Submission: Monday at 11:30 AM via WhatsApp.

# Note: 
You are encouraged to tackle as many aspects of the problem as possible, but you may choose to focus on specific areas according to your strengths and interests. However, ensure that any implemented section is well-documented and complete.
