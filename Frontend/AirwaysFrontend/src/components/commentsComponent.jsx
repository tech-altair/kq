import React, { useEffect, useState } from "react";
import {Stack, SimpleGrid, Card, CardBody} from "@chakra-ui/react"

const CommentsComponent = () => {
  const [comment, setComment] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchComments = async () => {
      try {
        const API_URL='http://localhost:3000/api'
        const responce = await axios.get(`${API_URL}/ /`,{ withCredentials: true });

        if (Array.isArray(responce)) {
          setComment(responce);
        } else {
          setComment([]);
          setError("Fetched data is not an array");
        }
      } catch (error) {
        setError("Error fetching comments");
      }
    };
    fetchComments();
  }, []);
  console.log(comment);
  if (error) {
    return <p>{error}</p>;
  }
  return (
    <Stack marginTop="30px">
      <div className="d-flex justify-content-center">
        <h2>Comments</h2>
      </div>
      <div className="d-flex justify-content-between">
        {comment.length > 0 ? (
          <div>
            <SimpleGrid
              columns={{ sm: 1, md: 2, lg: 3, xl: 4 }}
              spacing={6}
              padding="20px"
            >
              {comment.map((course) => (
                <Card className="card " key={comment.id}>
                  <CardBody>
                   {/* comments will loaded here */}
                  </CardBody>
                </Card>
              ))}
            </SimpleGrid>
          </div>
        ) : (
          <p>No comments available</p>
        )}
      </div>

    </Stack>
  );
};

export default CommentsComponent;
