<template>
  <div class="container mt-2">
    <br />
    <button class="btn btn-lg btn-danger">Post</button>
    <br />
    <br />
    <br />
    <form @submit.prevent="onSubmit">
      <textarea
        v-model="post_body"
        class="form-control"
        placeholder="What do you want to post?"
        rows="3"
      ></textarea>
      <br />
      <button type="submit" class="btn btn-success">Publish</button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "PostEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      post_body: null,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (!this.post_body) {
        this.error = "Post can't be empty!";
      } else if (this.post_body.length > 240) {
        this.error = "Post must be less than 240 characters!";
      } else {
        let endpoint = "/api/posts/";
        let method = "POST";
        if (this.slug !== undefined) {
          endpoint += `${this.slug}/`;
          method = "PUT";
        }
        apiService(endpoint, method, { content: this.post_body }).then(
          post_data => {
            this.$router.push({
              name: "post",
              params: { slug: post_data.slug }
            });
          }
        );
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    if (to.params.slug !== undefined) {
      let endpoint = `/api/posts/${to.params.slug}/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.post_body = data.content));
    } else {
      return next();
    }
  },
  created() {
    document.title = "Editor - Portfolio";
  }
};
</script>

<style scoped>
.btn-lg {
  pointer-events: none;
}
</style>
