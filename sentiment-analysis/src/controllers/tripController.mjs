import { fetchTripAdvisorReviews, saveReview } from "../services/tripServices.mjs";

//the function below will be used to pass a url to tripservices for data fetching
export const getTripReview = async (req,res) => {
    try {
        const reviews=await fetchTripAdvisorReviews("https://www.tripadvisor.com/Hotel_Review-g1-d1-KenyaAirways.html",{
            headers: {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'DNT': '1', 
                'Upgrade-Insecure-Requests': '1'
              },
              timeout: 5000,
        })
        
        for (review of reviews){
            saveReview(review)
        }
        
    } catch (error) {
        console.error("Error fetching reviews", error)
    }
}