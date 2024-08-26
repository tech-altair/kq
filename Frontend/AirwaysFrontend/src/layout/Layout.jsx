import { Grid, GridItem } from "@chakra-ui/react";
import NavBar from "./NavBar";
import Sidebar from "./Sidebar";
import Footer from "./footer";
import Dashboard from "../pages/Dashboard";

const Layout = () => {
  return (
    <Grid
      templateAreas={{
        base: `"navbar" "main" "footer"`,
        md: `"navbar navbar" "sidebar main" "footer footer"`,
      }}
      templateColumns={{
        base: "1fr",
        md: "250px 1fr",
      }}
    >
      <GridItem area="navbar" bg="lightblue">
        <NavBar />
      </GridItem>
      <GridItem area="sidebar" bg="darkgrey">
        <Sidebar />
      </GridItem>
      <GridItem area="main" bg="whitesmoke">
        {/* <Dashboard /> */}
      </GridItem>
      <GridItem area="footer" bg="goldenrod">
        {/* <Footer /> */}
      </GridItem>
    </Grid>
  );
};

export default Layout;
