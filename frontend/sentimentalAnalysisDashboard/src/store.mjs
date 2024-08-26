// store/store.js
import { configureStore } from '@reduxjs/toolkit';
import sentimentsSlice from './features/sentiments/sentimentsSlice.mjs';

const store = configureStore({
  reducer: {
    sentiment: sentimentsSlice,
  },
});

export default store;
