import { fetchTweets, saveTweet } from "../services/twitterServices.mjs";

export const getTweets = async (req, res) => {
  try {
    const query = "Kenya Airways"; //passing query parameters to the fetch tweets function
    const tweets = await fetchTweets(query);
    tweets.forEach((tweet) => {
      saveTweet(tweet.text); //passes the fetched tweets to the saveTweet function for saving purposes.
    });

    res.status(200).json({
        message: "Tweets fetched and saved successfully",
        data: tweets
    })
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while fetching tweets.' });
  }
};
