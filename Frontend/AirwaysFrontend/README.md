# Twitter Sentiment Analysis Frontend

## Overview

This React application serves as the frontend for displaying Twitter sentiment analysis data fetched from an Express.js backend. The application pulls data from the backend and presents it in a user-friendly interface with visualizations.

## Prerequisites

Ensure you have the following installed:

- Node.js (v14 or higher)
- npm (v6 or higher)

## Setup Instructions

- Run
 - npm create vite@latest 
  - follow the instructions to setup your name and what other applications to use.
 - cd <name-of-the-app>
  -Run the following command to install the dependencies
   -npm install
   -npm run dev (to check if the application is well setup)

- Install dependencies
 - npm i axios @chakra-ui/react bootstrap (They will be used for styling)


### OverView of the code structure

components/: Contains React components used to display data.
- Component for displaying Twitter posts.
services/: Contains service files for making API requests.
- Service file for fetching data from the backend.
App.jsx: The main application component where the layout and routing are managed.
index.jsx: Entry point of the React application.