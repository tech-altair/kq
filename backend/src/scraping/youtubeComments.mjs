import { google } from 'googleapis';

const youtube = google.youtube({
  version: 'v3',
  auth: 'AIzaSyCmdesGSYTjzGV7-0XTtHAo4sKY4ABEEDQ' // Replace with your API key
});

export const fetchYouTubeComments = async (req, res) => {
    const videoId = 'TIn11pAyjP0'
  try {
    const response = await youtube.commentThreads.list({
      part: 'snippet',
      videoId: videoId,
      maxResults: 100 // Fetch up to 100 comments per request
    });

    const comments = response.data.items.map(item => {
      const comment = item.snippet.topLevelComment.snippet.textDisplay;
      const author = item.snippet.topLevelComment.snippet.authorDisplayName;
      return { author, comment };
    });
    res.send(comments)
    console.log(comments);
  } catch (error) {
    console.error('Error fetching YouTube comments:', error);
  }
}

// Example usage: Fetch comments for a specific YouTube video
// fetchYouTubeComments('TIn11pAyjP0'); // Replace 'VIDEO_ID_HERE' with the actual YouTube video ID
