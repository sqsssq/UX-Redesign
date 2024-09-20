/*
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-11-20 18:21:36
 * @LastEditTime: 2022-11-21 00:21:58
 */
import { createRouter, createWebHashHistory, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LionView from '../views/LionView.vue';
import PicView from "../views/PicView.vue";

const router = createRouter({
  // history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/lion",
      name: 'lion',
      component: LionView
    },
    {
        path: "/pic",
        name: 'pic',
        component: PicView
    }
    // {
    //   path: "/baseline",
    //   name: "baseline",
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import("../views/BaselineView.vue"),
    // },
    // {
    //     path: "/UxEn",
    //     name: "UxEn",
    //     component: () => import("../views/HomeView_en.vue"),
    // },
    // {
    //     path: "/baselineEn",
    //     name: "baselineEn",
    //     component: () => import("../views/BaselineView_en.vue"),
    // },
  ],
});

export default router;
