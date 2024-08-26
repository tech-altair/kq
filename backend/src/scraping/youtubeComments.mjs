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
  auth: 'AIzaSyCmdesGSYTjzGV7-0XTtHAo4sKY4ABEEDQ', // API key (should be replaced with your actual API key)
});

// Function to fetch comments from a YouTube video
async function fetchYouTubeComments(videoId) {
  try {
    // Make a request to the YouTube API to get comment threads
    const response = await youtube.commentThreads.list({
      part: 'snippet', // Specifies the resource parts that the API response should include
      videoId: videoId, // The ID of the video for which comments are being fetched
      maxResults: 100, // Maximum number of comments to retrieve
    });

    // Transform the response to extract necessary data
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
  // Map over each comment and perform sentiment analysis
  return comments.map(({ author, comment }) => {
    const analysis = sentiment.analyze(comment); // Analyze the sentiment of the comment text
    return { author, comment, score: analysis.score }; // Return the author, comment, and sentiment score
  });
}

// Function to save sentiment scores to the database using Prisma
async function saveSentimentScores(comments) {
  try {
    // Loop over each comment and save it to the database
    for (const { author, comment, score } of comments) {
      await prisma.comment.create({
        data: { author, comment, score }, // Create a new record in the 'comment' table with author, comment, and score
      });
    }
    // Log success message after all comments are saved
    console.log('Sentiment scores saved successfully.');
  } catch (error) {
    // Log any errors that occur while saving to the database
    console.error('Error saving sentiment scores:', error);
  }
}

// Function to fetch comments, analyze them, and save the scores
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
