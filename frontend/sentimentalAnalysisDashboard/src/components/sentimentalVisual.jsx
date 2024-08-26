import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Box, Typography, Paper } from '@mui/material';
//imports for chart generation
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import {useSelector} from "react-redux"

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const SentimentChart = () => {

const {data} = useSelector(state => state.sentiment)
const {positive, negative, neutral} = data //destructuring for the values
//chart generation  
const chartData = {
    labels: ['Positive', 'Negative', 'Neutral'],
    datasets: [
      {
        label: 'Sentiments',
        data: [positive, negative, neutral],
        backgroundColor: ['#4caf50', '#f44336', '#ffeb3b'],
      },
    ],
  };

  return (
    <Paper elevation={3} sx={{ p: 3, mt: 4 }}>
     
      <Box>
        <Typography variant="h6" component="h2" gutterBottom>
          Sentiment Analysis Results
        </Typography>
        <Box sx={{ position: 'relative', height: '400px', width: '100%' }}>
          <Bar data={chartData} options={{ maintainAspectRatio: false }} />
        </Box>
      </Box>
    </Paper>
  );
};

export default SentimentChart;
