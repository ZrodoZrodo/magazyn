import React from "react";
import DashboardNavbar from "../components/dashboardNavbar";
import Sidebar from "../components/sideBar";
import { DashboardInfo } from "../components/dashboardInfo";
import { TrainingInfo } from "../components/trainingInfo";
import { TrainingList } from "../components/trainingList";

import { AddExercise } from "../components/addExercise";

export const Dashboard = () => {
  return (
    <div className="flex flex-wrap max-h-screen w-full min-h-screen">
      <DashboardNavbar></DashboardNavbar>
      <div className="flex flex-nowrap min-h-screen w-full ">
        <Sidebar></Sidebar>
        <AddExercise />
        <DashboardInfo />
      </div>
    </div>
  );
};
