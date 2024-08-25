import Sentiment from 'sentiment';
import { google } from 'googleapis';
import { PrismaClient } from '@prisma/client';

const sentiment = new Sentiment();
const prisma = new PrismaClient();

const youtube = google.youtube({
  version: 'v3',
  auth: 'AIzaSyCmdesGSYTjzGV7-0XTtHAo4sKY4ABEEDQ', // Replace with your API key
});

async function fetchYouTubeComments(videoId) {
  try {
    const response = await youtube.commentThreads.list({
      part: 'snippet',
      videoId: videoId,
      maxResults: 100,
    });

    return response.data.items.map(item => ({
      author: item.snippet.topLevelComment.snippet.authorDisplayName,
      comment: item.snippet.topLevelComment.snippet.textDisplay,
    }));
  } catch (error) {
    console.error('Error fetching YouTube comments:', error);
  }
}

function analyzeSentiments(comments) {
  return comments.map(({ author, comment }) => {
    const analysis = sentiment.analyze(comment);
    return { author, comment, score: analysis.score };
  });
}

async function saveSentimentScores(comments) {
  try {
    for (const { author, comment, score } of comments) {
      await prisma.comment.create({
        data: { author, comment, score },
      });
    }
    console.log('Sentiment scores saved successfully.');
  } catch (error) {
    console.error('Error saving sentiment scores:', error);
  }
}

async function fetchAndAnalyzeComments(videoId) {
  const comments = await fetchYouTubeComments(videoId);
  const analyzedComments = analyzeSentiments(comments);
  await saveSentimentScores(analyzedComments);
}
  

async function main() {
  await fetchAndAnalyzeComments('Yv0tzAJ46uU'); // Replace with actual video ID

  // Disconnect Prisma Client
  await prisma.$disconnect();
}

main().catch((e) => {
  console.error(e);
  prisma.$disconnect();
});
