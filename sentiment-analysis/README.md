# Twitter Scraping and React Integration

## Overview

This project demonstrates how to set up an Express.js backend to scrape Twitter for specific keywords and a React frontend to display the results. The project utilizes the Twitter API for data scraping and Prisma ORM for storing data in an SQL database.

## Prerequisites

Ensure you have the following installed:

- Node.js (v14 or higher)
- npm (v6 or higher)
- pnpm
- Twitter Developer Account (for API keys)
- mySQL or any other SQL database
- Create a Twitter Developer account and obtain the following credentials:
  - `API Key`
  - `API Key Secret`
  - `Access Token`
  - `Access Token Secret`

## Backend Setup (Express.js)

- commands
 - pnpm i express nodemon axios cheerio @prisma/client
 - Update the package.json to work with nodemon (since nodemon doesn't restarts itself when changes are made making it a better option)

 
 - prisma inititalization
  - npx prisma init
  - npx prisma generate
  - npx prisma migrate dev --name init (the name you will use)
  - npx prisma pull db (to chech whether the database is functioning well)

- Run the Backend 
 - pnpm start 



