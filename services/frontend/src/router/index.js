import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SingleFileView from "../views/SingleFileView.vue";
import MultipleFilesView from "../views/MultipleFilesView.vue";
import DetailView from "@/views/DetailView.vue";

const routes = [
  {
    path: "/",
    name: "HomeView",

    component: HomeView,
  },
  {
    path: "/single_file",
    name: "SingleFileView",
    component: SingleFileView,
    props: { default: true }
  },
  {
    path: "/multiple_files",
    name: "MultipleFilesView",
    component: MultipleFilesView
  },
  {
    path: "/detail",
    name: "DetailView",
    component: DetailView,
    props: true
  }

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
