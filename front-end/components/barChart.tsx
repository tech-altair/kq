"use client";

import { TrendingUp } from "lucide-react";
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart";

const chartConfig = {
  positive: {
    label: "Positive",
    color: "hsl(var(--chart-1))",
  },
  negative: {
    label: "Negative",
    color: "hsl(var(--chart-2))",
  },
  neutral: {
    label: "Neutral",
    color: "hsl(var(--chart-3))",
  },
} satisfies ChartConfig;

export function BarChartComponent({
  data,
}: {
  data: { created_at: string; sentiment: string }[];
}) {
  const currentYear = new Date().getFullYear();
  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  // Initialize chartData with the last 6 months
  const chartData = months.slice(-6).map((month) => ({
    month,
    positive: 0,
    neutral: 0,
    negative: 0,
  }));

  // Classify data into months
  data.forEach((item) => {
    const date = new Date(item.created_at);
    if (date.getFullYear() === currentYear) {
      const monthIndex = date.getMonth();
      if (monthIndex >= 6) {
        chartData[monthIndex - 6].positive +=
          item.sentiment === "positive" ? 1 : 0;
        chartData[monthIndex - 6].neutral +=
          item.sentiment === "neutral" ? 1 : 0;
        chartData[monthIndex - 6].negative +=
          item.sentiment === "negative" ? 1 : 0;
      }
    }
  });

  return (
    <Card>
      <CardHeader>
        <CardTitle>Comparison of Sentiments by Months</CardTitle>
        <CardDescription className="text-center">
          Monthly analysis of {currentYear}
        </CardDescription>
      </CardHeader>
      <CardContent>
        <ChartContainer config={chartConfig}>
          <BarChart accessibilityLayer data={chartData}>
            <CartesianGrid vertical={false} />
            <XAxis
              dataKey="month"
              tickLine={false}
              tickMargin={10}
              axisLine={false}
              tickFormatter={(value) => value.slice(0, 3)}
            />
            <ChartTooltip
              cursor={false}
              content={<ChartTooltipContent indicator="dashed" />}
            />
            <Bar dataKey="positive" fill="var(--color-positive)" radius={4} />
            <Bar dataKey="neutral" fill="var(--color-neutral)" radius={4} />
            <Bar dataKey="negative" fill="var(--color-negative)" radius={4} />
          </BarChart>
        </ChartContainer>
      </CardContent>
      <CardFooter className="flex-col items-center gap-2 text-sm">
        <div className="flex gap-2 font-medium leading-none">
          <span className="text-positive">Positive</span>
          <span className="text-neutral">Neutral</span>
          <span className="text-negative">Negative</span>

          <TrendingUp className="h-4 w-4" />
        </div>
        <div className="leading-none text-muted-foreground">
          Showing total reviews for the last growth over time
        </div>
      </CardFooter>
    </Card>
  );
}
