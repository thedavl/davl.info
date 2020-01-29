import Vue from "vue";
import Router from "vue-router";
import CommentEditor from "./views/CommentEditor.vue";
import Home from "./views/Home.vue";
import NotFound from "./views/NotFound.vue";
import Post from "./views/Post.vue";
import PostEditor from "./views/PostEditor.vue";
import Blog from "./views/Blog.vue";
import Projects from "./views/Projects.vue";
import AboutMe from "./views/AboutMe.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  //base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/blog/",
      name: "blog",
      component: Blog
    },
    {
      path: "/projects/",
      name: "projects",
      component: Projects
    },
    {
      path: "/about-me/",
      name: "about-me",
      component: AboutMe
    },
    {
      path: "/post/:slug",
      name: "post",
      component: Post,
      props: true
    },
    {
      path: "/post-editor/:slug?",
      name: "post-editor",
      component: PostEditor,
      props: true
    },
    {
      path: "/comment/:id",
      name: "comment-editor",
      component: CommentEditor,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound
    }
  ]
});
