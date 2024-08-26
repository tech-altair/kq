"use client";
import React from "react";
import { CustomDialog } from "./customDialog";

interface Review {
  id: string;
  description: string;
  sentiment: string;
  created_at: string;
  source: string;
  source_link: string;
}

interface ReviewsProps {
  data: Review[];
}

export default function Reviews({ data }: ReviewsProps) {
  const [description, setDescription] = React.useState("");
  const [loading, setLoading] = React.useState(false);

  function filterData(id: string) {
    setLoading(true);
    const filteredData = data.filter((review) => review.id === id);
    if (filteredData.length > 0) {
      setDescription(filteredData[0].description);
    } else {
      setDescription("No description available.");
    }
    setLoading(false);
  }

  return (
    <div className="w-full p-4">
      {/* <div className="mb-4 text-lg font-semibold text-center">
        {loading ? "Loading..." : description}
      </div> */}
      <table className="table-auto w-full border-collapse">
        <thead>
          <tr className="bg-primary text-white px-2">
            <th className=" lg:py-1 w-10">#</th>
            <th className=" text-start">Category</th>
            <th className=" text-start">Review</th>
            <th className=" text-start">Category</th>
            <th className=" text-start px-2">Link</th>
            <th className=" text-start">Date</th>
            <th className=" text-start">View</th>
          </tr>
        </thead>
        <tbody>
          {data.map((review, index) => (
            <tr key={index} className="border text-sm py-2 hover:bg-gray-200">
              <td className="text-center w-10">{index + 1}</td>
              <td className="text-center w-10">{review.source}</td>
              <td className="lowercase ">
                {review.description.slice(0, 50)}...
              </td>
              <td className="px-2">
                {review.sentiment === "positive" ? (
                  <span className="text-green-500">Positive</span>
                ) : review.sentiment === "negative" ? (
                  <span className="text-red-500">Negative</span>
                ) : (
                  <span className="text-gray-500">Neutral</span>
                )}
              </td>
              <td>
                <a
                  href={review.source_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-500 underline px-2"
                  aria-label={`View review ${index + 1}`}
                >
                  link
                </a>
              </td>
              <td className="px-2">
                {new Date(review.created_at).toDateString()}
              </td>
              <td>
                {/* <button
                  className="text-blue-500 underline px-2"
                  onClick={() => filterData(review.id)}
                  aria-label={`View review ${index + 1}`}
                >
                  View
                </button> */}
                <CustomDialog description={review.description} />
                {/* <div className="p-4">{description}</div> */}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
