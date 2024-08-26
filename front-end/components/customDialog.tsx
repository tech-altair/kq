import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
// import { Input } from "@/components/ui/input";
// import { Label } from "@/components/ui/label";

export function CustomDialog({ description }: any) {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline">View</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[825px] m-5">
        <DialogHeader>
          <DialogTitle>Read Review</DialogTitle>
          {/* <DialogDescription>
            View the full review of the selected item.
          </DialogDescription> */}
        </DialogHeader>
        <div className="grid gap-4 py-4 lowercase">{description}</div>
        {/* <DialogFooter>
          <Button type="submit">Save changes</Button>
        </DialogFooter> */}
      </DialogContent>
    </Dialog>
  );
}
