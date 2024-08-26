"use client";

import * as React from "react";
import { TrendingUp } from "lucide-react";
import { Label, Pie, PieChart } from "recharts";

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

export function CircularChart({ data }: { data: any[] }) {
  const positive = data.filter(
    (review: any) => review.sentiment === "positive"
  ).length;
  const negative = data.filter(
    (review: any) => review.sentiment === "negative"
  ).length;
  const neutral = data.filter(
    (review: any) => review.sentiment === "neutral"
  ).length;

  const chartData = [
    { sentiment: "positive", count: positive, fill: "var(--color-positive)" },
    { sentiment: "negative", count: negative, fill: "var(--color-negative)" },
    { sentiment: "neutral", count: neutral, fill: "var(--color-neutral)" },
  ];

  const totalReviews = positive + negative + neutral;

  // Check the data and set the earliest date and the latest date
  let start_date = new Date(data[0].created_at);
  let end_date = new Date(data[0].created_at);

  data.forEach((item) => {
    const currentDate = new Date(item.created_at);
    if (currentDate < start_date) {
      start_date = currentDate;
    }
    if (currentDate > end_date) {
      end_date = currentDate;
    }
  });

  return (
    <Card className="flex flex-col">
      <CardHeader className="items-center pb-0">
        <CardTitle>Distribution of User Reviews</CardTitle>
        <CardDescription>Sentiment Analysis</CardDescription>
      </CardHeader>
      <CardContent className="flex-1 pb-0">
        <ChartContainer
          config={chartConfig}
          className="mx-auto aspect-square max-h-[250px]"
        >
          <PieChart>
            <ChartTooltip
              cursor={false}
              content={<ChartTooltipContent hideLabel />}
            />
            <Pie
              data={chartData}
              dataKey="count"
              nameKey="sentiment"
              innerRadius={60}
              strokeWidth={5}
            >
              <Label
                content={({ viewBox }) => {
                  if (viewBox && "cx" in viewBox && "cy" in viewBox) {
                    return (
                      <text
                        x={viewBox.cx}
                        y={viewBox.cy}
                        textAnchor="middle"
                        dominantBaseline="middle"
                      >
                        <tspan
                          x={viewBox.cx}
                          y={viewBox.cy}
                          className="fill-foreground text-3xl font-bold"
                        >
                          {totalReviews.toLocaleString()}
                        </tspan>
                        <tspan
                          x={viewBox.cx}
                          y={(viewBox.cy || 0) + 24}
                          className="fill-muted-foreground"
                        >
                          Reviews
                        </tspan>
                      </text>
                    );
                  }
                }}
              />
            </Pie>
          </PieChart>
        </ChartContainer>
      </CardContent>
      <CardFooter className="flex-col gap-2 text-sm">
        <div className="flex items-center gap-2 font-medium leading-none">
          <span className="text-positive">+{positive}</span>
          <span className="text-negative">-{negative}</span>
          <span className="text-neutral">{neutral}</span>

          <TrendingUp className="h-4 w-4" />
        </div>
        <div className="leading-none text-muted-foreground">
          Showing sentiment analysis for the reviews
        </div>
      </CardFooter>
    </Card>
  );
}
