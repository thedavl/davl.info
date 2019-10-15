<template>
  <div class="single-post mt-2">
    <div v-if="post" class="container">
      <br />
      <router-link :to="{ name: 'blog' }" class="btn btn-sm btn-danger">Back</router-link>
      <br />
      <br />
      <h1>{{ post.content }}</h1>
      <PostActions v-if="isPostAuthor" :slug="post.slug" />
      <p clas="mb-0">
        Posted by:
        <span class="author-name">{{ post.author }}</span>
      </p>
      <p>{{ post.created_at }}</p>
      <hr />
      <div v-if="userHasCommented">
        <p class="comment-added">You have commented!</p>
      </div>
      <div v-else-if="showForm">
        <form class="card" @submit.prevent="onSubmit">
          <div class="card-header px-3">Comment</div>
          <div class="card-block">
            <textarea
              v-model="newCommentBody"
              class="form-control"
              placeholder="Write your comment here!"
              rows="5"
            ></textarea>
          </div>
          <div class="card-footer px-3">
            <button type="submit" class="btn btn-sm btn-success">Submit your comment</button>
          </div>
        </form>
        <p v-if="error" class="error mt-2">{{ error }}</p>
      </div>
      <div v-else>
        <button v-if="isLoggedIn" class="btn btn-sm btn-success" @click="showForm = true">Comment</button>
        <button v-else class="btn btn-sm btn-success">Login to Comment</button>
      </div>
      <hr />
    </div>
    <div v-else>
      <h1 class="error text-center">404 - Post Not Found</h1>
    </div>
    <div v-if="post" class="container">
      <CommentComponent
        v-for="comment in comments"
        :comment="comment"
        :requestUser="requestUser"
        :key="comment.id"
        @delete-comment="deleteComment"
      />

      <div class="my-4">
        <p v-show="loadingAnswers">...loading...</p>
        <button
          v-show="next"
          @click="getPostComments"
          class="btn btn-sm btn-outline-success"
        >Load More</button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import CommentComponent from "@/components/Comment.vue";
import PostActions from "@/components/PostActions.vue";
export default {
  name: "Post",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    CommentComponent,
    PostActions
  },
  data() {
    return {
      post: {},
      comments: [],
      newCommentBody: null,
      error: null,
      userHasCommented: false,
      showForm: false,
      next: null,
      loadingComments: false,
      requestUser: null,
    };
  },
  computed: {
    isPostAuthor() {
      return this.post.author === this.requestUser;
    },
    isLoggedIn() {
        return this.requestUser !== "";
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    getPostData() {
      let endpoint = `/api/posts/${this.slug}/`;
      apiService(endpoint).then(data => {
        if (data) {
          this.post = data;
          this.userHasCommented = data.user_has_commented;
          this.setPageTitle(data.content);
        } else {
          this.post = null;
          this.setPageTitle("404 - Page Not Found");
        }
      });
    },
    getPostComments() {
      let endpoint = `/api/posts/${this.slug}/comments/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingComments = true;
      apiService(endpoint).then(data => {
        this.comments.push(...data.results);
        this.loadingComments = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
    onSubmit() {
      if (this.newCommentBody) {
        let endpoint = `/api/posts/${this.slug}/comment/`;
        apiService(endpoint, "POST", { body: this.newCommentBody }).then(
          data => {
            this.comments.unshift(data);
          }
        );
        this.newCommentBody = null;
        this.showForm = false;
        this.userHasCommented = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty comment!";
      }
    },
    async deleteComment(comment) {
      let endpoint = `/api/comments/${comment.id}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$delete(this.comments, this.comments.indexOf(comment));
        this.userHasCommented = false;
      } catch (err) {
        // console.log(err);
      }
    }
  },
  created() {
    this.getPostData();
    this.getPostComments();
    this.setRequestUser();
  }
};
</script>

<style scoped>
.author-name {
  font-weight: bold;
  color: #dc3545;
}
.comment-added {
  font-weight: bold;
  color: green;
}
.error {
  font-weight: bold;
  color: red;
}
</style>