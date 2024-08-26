# YouTube Comments Sentiment Analysis

## Description

The project is a web scraping tool developed to analyze sentiments from YouTube video comments. Using the YouTube Data API, the tool extracts comments from specified YouTube videos and performs sentiment analysis to classify comments as positive, negative, or neutral. I used React, Vite, and Material UI to create a visualized represenation of the results.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Environment Setup](#environment-setup)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

```bash

   git clone https://github.com/hanningto/kq.git
   cd kq

   ```
2. **Navigate to the backend directory**:

```bash

cd backend/src
Install backend dependencies:
```

```bash
npm install
```
3. **Navigate to the frontend directory**:

```bash
cd ../frontend/sentimentalAnalysisDashboard
Install frontend dependencies:
```

```bash
npm install
```
4. **Set up the .env file for the backend**:

Create a .env file in the backend directory and add your YouTube Data API key:

```makefile
YOUTUBE_API_KEY=your_youtube_api_key_here
```

# Usage
## Running the Backend
1. **run the scraping code**:

```bash
cd backend/src/scraping
node youtubeComments.mjs
```
This will run the code requiered to fetch and analyse and save the comments from youtube.

```bash
cd ..
npm run dev
```
This will run the server

# Running the Frontend
Start the frontend development server:

```bash
cd frontend/sentimentalAnalysisDashboard
npm run dev
```
This will start the frontend development server, and you can access the dashboard at http://localhost:3000.



# Features
1. YouTube Data Extraction: Extract comments from YouTube videos using the YouTube Data API.
2. Sentiment Analysis: Analyze the sentiment of comments using a sentiment analysis library.
3. Visualization: Visualize the sentiment analysis results on a web dashboard with charts.
4. Redux State Management: Manage the state of the sentiment data using Redux Toolkit for a seamless user experience.

# Environment Setup
## Prerequisites
Node.js: Make sure you have Node.js installed (v12 or later).
YouTube Data API Key: You will need a YouTube Data API key to fetch comments from YouTube videos.

## Backend
Express: The backend server is built with Express.js to handle API requests.
Prisma: Prisma ORM is used for managing the database and interacting with it efficiently.
MSSQL: Sql server is used for saving the analyzed user comments

## Frontend
React: The frontend is built using React with functional components.
Vite: Vite is used as the development server for fast development and hot module replacement.
Material UI: Material UI is used for UI components and styling, making the dashboard look clean and modern.
Chart.js: Chart.js is used for visualizing the sentiment data in bar charts.
Contributing
Contributions are welcome! To contribute to this project:

# Additional Inforamtion

## Procedure to Obtain a YouTube Video ID
1. **Open YouTube**:

Go to the YouTube website or open the YouTube app on your device.
2. **Find the Video:**

Search for the video you are interested(One concerning Kenya Airways) in by typing keywords related to the video in the search bar and hitting the "Enter" key.
3. **Open the Video:**

Click on the video from the search results to open it.
4. **Get the Video URL:**

Once the video is open, look at the URL in your browser's address bar. It will look something like this:
https://www.youtube.com/watch?v=Yv0tzAJ46uU
5. **Identify the Video ID:**

The YouTube video ID is the string of characters that comes after the v= in the URL.
In the example URL above, the video ID is Yv0tzAJ46uU.
6. **Copy the Video ID:**

Highlight the video ID in the URL, right-click and select "Copy" or press Ctrl+C (Windows) or Cmd+C (Mac) to copy the video ID.


# Limitations
1. You have to get the video id manualy from youtube
2. You have to edit add the video url directly into the code
3. You have to run the scraping code manually in order to get the comments from youtube