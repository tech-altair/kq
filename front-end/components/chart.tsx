"use cleint";
import React from "react";
import { CircularChart } from "./circular";
import { BarChartComponent } from "./barChart";
export default function Chart({ data }: any) {
  return (
    <div className="rounded-md m-5 flex justify-center items-center">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
        <CircularChart data={data} />
        <BarChartComponent data={data} />
      </div>
    </div>
  );
}
