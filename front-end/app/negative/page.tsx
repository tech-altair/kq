import Image from "next/image";
import Navbar from "@/components/navbar";
import Chart from "@/components/chart";
import Reviews from "@/components/reviews";
async function getData() {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_BACKEND_URL}/reviews/negative`,
    // { next: { revalidate: 3600 } }
    { next: { revalidate: 0 } }
  );
  try {
    if (!res.ok) {
      throw new Error("Request failed");
    }
  } catch (err) {
    if (err instanceof Error) {
      throw new Error(err.message);
    } else {
      throw err;
    }
  }
  return res.json();
}

export default async function Home() {
  const data: any = await getData();
  // console.log(data);
  // };
  return (
    <main>
      <Navbar />
      <Chart data={data} />
      <Reviews data={data} />
    </main>
  );
}
