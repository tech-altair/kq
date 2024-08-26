import React, { useEffect} from "react";
//material UI styling imports
import {
  Container,
  Typography,
  Box,
  CircularProgress,
  Paper,
  Grid,
} from "@mui/material";

import SentimentChart from "./components/sentimentalVisual"; //Import the chart component
//importing the requierd actions from the redux slice 
import {
  fetchSentimentsFailure,
  fetchSentimentsStart,
  fetchSentimentsSuccess,
} from "./features/sentiments/sentimentsSlice.mjs";
//importing hooks required for interacting with state
import { useDispatch, useSelector } from "react-redux";

function App() {
  const { data, loading, videosCount, commentsCount } = useSelector(
    (state) => state.sentiment
  );
  const dispatch = useDispatch();

  //Fetching data from backend
  useEffect(() => {
    const fetchData = async () => {
      dispatch(fetchSentimentsStart());

      try {
        const response = await fetch("http://127.0.0.1:3000/api/");
        const data = await response.json();
        //setting the states
        dispatch(
          fetchSentimentsSuccess({
            sentiments: data.sentiments,
            videosCount: data.videosCount,
            commentsCount: data.commentsCount,
          })
        );
      } catch (error) { //error handling
        dispatch(fetchSentimentsFailure(error));
        console.log(error)
      }
    };

    fetchData();
  }, [dispatch]);

  return (
    <Container  sx={{ mt: 4, pb: 4 }}>
      <Typography
        variant="h3"
        component="h1"
        gutterBottom
        sx={{ fontWeight: "bold", color: "#333" }}
      >
        Sentiment Analysis Dashboard
      </Typography>

      <Typography
        variant="body1"
        gutterBottom
        sx={{ mb: 3, fontSize: "1.3rem", color: "#555" }}
      >Welcome to the Sentiments analysis dashboard.
        This dashboard presents a sentiment analysis of YouTube comments related
        to{" "}
        <span style={{ fontWeight: "bold", color: "#D32F2F" }}>
          Kenya Airways
        </span>
        . The sentiments have been categorized into positive, negative, and
        neutral, based on the feedback from various YouTube videos featuring
        Kenya Airways. Explore the insights below to understand public opinion
        and sentiments about the airline.
      </Typography>
      <Grid container spacing={2} mb={4}>
            <Grid item xs={6}>
              <Box textAlign="center" p={2} bgcolor="#f0f0f0" borderRadius={1}>
                <Typography variant="h6">Total Videos Analyzed</Typography>
                <Typography variant="h4">{videosCount}</Typography>
              </Box>
            </Grid>
            <Grid item xs={6}>
              <Box textAlign="center" p={2} bgcolor="#f0f0f0" borderRadius={1}>
                <Typography variant="h6">Total Comments Analyzed</Typography>
                <Typography variant="h4">{commentsCount}</Typography>
              </Box>
            </Grid>
          </Grid>
      
      
      {loading ? (
        <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          height="50vh"
        >
          <CircularProgress />
        </Box>
      ) : (
        <Paper elevation={4} sx={{ p: 3, backgroundColor: "#f5f5f5" }}>
          <Grid container spacing={2} mb={4}>
            <Grid item xs={4}>
              <Box textAlign="center" p={2} bgcolor="#2e7d32" borderRadius={1}>
                <Typography variant="h6">Positive</Typography>
                <Typography variant="h4">{data.positive}</Typography>
              </Box>
            </Grid>
            <Grid item xs={4}>
              <Box textAlign="center" p={2} bgcolor="#c62828" borderRadius={1}>
                <Typography variant="h6">Negative</Typography>
                <Typography variant="h4">{data.negative}</Typography>
              </Box>
            </Grid>
            <Grid item xs={4}>
              <Box textAlign="center" p={2} bgcolor="#0277bd" borderRadius={1}>
                <Typography variant="h6">Neutral</Typography>
                <Typography variant="h4">{data.neutral}</Typography>
              </Box>
            </Grid>
           
          </Grid>
          <SentimentChart />
        </Paper>
      )}
    </Container>
  );
}

export default App;
