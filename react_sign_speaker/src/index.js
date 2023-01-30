import React from "react";
import { createRoot } from "react-dom/client";
import Translate from "./components/routes/Translate";
import Welcome from "./components/routes/Welcome";
import Learn from "./components/routes/Learn";
import Sidebar from "./components/sidebar";
import "./App.css";
import {
  createBrowserRouter,
  RouterProvider,
  Route,
  Link,
  Outlet,
} from "react-router-dom";

const AppLayout = () => (
  <>
    <Sidebar />
    <Outlet />
  </>
);

const router = createBrowserRouter([
  {
    element: <AppLayout />,
    children: [
      {
      path: "/",
      element: <Welcome />,
      },
      {
        path: "translate",
        element: <Translate />,
      },
      {
        path: "learn",
        element: <Learn />,
      },
    ],
  },

]);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);