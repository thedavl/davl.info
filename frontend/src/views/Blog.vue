<template>
  <div class="home">
    <br />
    <div class="container mt-2">
      <router-link
        v-if="isLoggedIn"
        :to="{ name: 'post-editor' }"
        class="btn btn-sm btn-danger"
        style="margin-left: 10px"
      >Post</router-link>
      <button v-else class="btn btn-sm btn-danger" style="margin-left: 10px">Login to Post</button>
      <br />
      <br />
      <div v-for="post in posts" :key="post.pk" class="card">
        <p>
          Posted by:
          <span class="post-author">{{ post.author }}</span>
        </p>
        <h2>
          <router-link
            :to="{ name: 'post', params: { slug: post.slug } }"
            class="post-link"
          >{{ post.content }}</router-link>
        </h2>
        <p>Comments: {{ post.comments_count }}</p>
      </div>
      <div class="my-4">
        <p v-show="loadingPosts">...loading...</p>
        <button 
          v-show="next" 
          @click="getPosts" 
          class="btn btn-sm btn-outline-success" 
          style="margin-left: 10px">
          Load More</button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "blog",
  data() {
    return {
      posts: [],
      next: null,
      loadingPosts: false,
      isLoggedIn: null
    };
  },   
  methods: {
    getPosts() {
      let endpoint = "/api/posts/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingPosts = true;
      apiService(endpoint).then(data => {
        this.posts.push(...data.results);
        this.loadingPosts = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
    getUsername() {
      let endpoint = `api/user/`;
      apiService(endpoint).then(data => {
        if (data) {
          if (data.username != "") {
            this.isLoggedIn = true;
          } else {
            this.isLoggedIn = false;
          }
        } else {
          this.setPageTitle("username error");
        }
      });
    }
  },
  created() {
    this.getPosts();
    this.getUsername();
    document.title = "Blog";
  }
};
</script>

<style scoped>
.post-author {
  font-weight: bold;
  color: #dc3545;
}

.post-link {
  font-weight: bold;
  color: black;
}

.post-link:hover {
  color: #343a40;
  text-decoration: none;
}

.card {
  width: 80%;
  padding-left: 10px;
  padding-top: 12px;
  margin: 10px;
  box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.2), 0 0px 20px 0 rgba(0, 0, 0, 0.19);
  background-color: #E8E8E8
}
</style>
