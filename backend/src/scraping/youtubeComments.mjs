// Importing necessary modules
import Sentiment from 'sentiment'; // Sentiment analysis library
import { google } from 'googleapis'; // Google APIs library
import { PrismaClient } from '@prisma/client'; // Prisma Client for database operations

// Initializing sentiment analysis and Prisma Client
const sentiment = new Sentiment();
const prisma = new PrismaClient();

// Connecting to YouTube API with specific version and API key
const youtube = google.youtube({
  version: 'v3', // Specifies the version of the YouTube API to use
  auth: process.env.youtubeApiKey, // API key 
});

// Function to fetch comments from a YouTube video
async function fetchYouTubeComments(videoId) {
  try {
    // Make a request to the YouTube API to get comment threads
    const response = await youtube.commentThreads.list({
      part: 'snippet', 
      videoId: videoId, 
      maxResults: 100, 
    });

    //  extract necessary data
    return response.data.items.map(item => ({
      author: item.snippet.topLevelComment.snippet.authorDisplayName, // The name of the comment author
      comment: item.snippet.topLevelComment.snippet.textDisplay, // The text of the comment
    }));
  } catch (error) {
    // Log any errors that occur during the API request
    console.error('Error fetching YouTube comments:', error);
  }
}

// Function to analyze sentiments of comments
function analyzeSentiments(comments) {
  // perform sentiment analysis to every comment
  return comments.map(({ author, comment }) => {
    const analysis = sentiment.analyze(comment); // Analyze the sentiment of the comment text
    return { author, comment, score: analysis.score }; // Return the author, comment, and sentiment score
  });
}

//save sentiment scores to the database
async function saveSentimentScores(comments) {
  try {
    for (const { author, comment, score } of comments) {
      await prisma.comment.create({
        data: { author, comment, score }, // Create a new record in the 'comment' table with author, comment, and score
      });
    }
    // feedback for successfull
    console.log('Sentiment scores saved successfully.');
  } catch (error) {
    // error handling
    console.error('Error saving sentiment scores:', error);
  }
}

// fetching comments, analyze them, and save the scores
async function fetchAndAnalyzeComments(videoId) {
  const comments = await fetchYouTubeComments(videoId); // Fetch comments from YouTube
  const analyzedComments = analyzeSentiments(comments); // Analyze the sentiment of the fetched comments
  await saveSentimentScores(analyzedComments); // Save the analyzed comments to the database
}

// Main function to run the program
async function main() {
  const prevVidoesIds = ['_ZygCEeb5iU',"nle6K7GvT0U"]
  await fetchAndAnalyzeComments('_ZygCEeb5iU'); // passing the video id

  // Disconnect Prisma Client to close the database connection
  await prisma.$disconnect();
}

// Execute the main function and handle any errors
main().catch((e) => {
  console.error(e); 
  prisma.$disconnect(); // Prisma disconnects 
});
