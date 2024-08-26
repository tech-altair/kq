import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  data: [],
  loading: false,
  error: null,
  videosCount: 0,
  commentsCount: 0,
};

const sentimentSlice = createSlice({
  name: 'sentiment',
  initialState,
  reducers: {
    // Action to start fetching sentiments
    fetchSentimentsStart(state) {
      state.loading = true;
      state.error = null;
    },
    // Action when sentiments are successfully fetched
    fetchSentimentsSuccess(state, action) {
      state.data = action.payload.sentiments;
      state.videosCount = action.payload.videosCount;
      state.commentsCount = action.payload.commentsCount;
      state.loading = false;
    },
    // Action when there is an error fetching sentiments
    fetchSentimentsFailure(state, action) {
      state.error = action.payload;
      state.loading = false;
    },
    // Action to reset sentiments data
    resetSentiments(state) {
      state.data = [];
      state.videosCount = 0;
      state.commentsCount = 0;
      state.error = null;
      state.loading = false;
    },
  },
});

export const {
  fetchSentimentsStart,
  fetchSentimentsSuccess,
  fetchSentimentsFailure,
  resetSentiments,
} = sentimentSlice.actions;

export default sentimentSlice.reducer;
