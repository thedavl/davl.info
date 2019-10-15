<template>
    <div class="container mt-2">
        <h1 class="mb-3">Edit Your Comment</h1>
        <form @submit.prevent="onSubmit">
            <textarea 
                v-model="commentBody"
                class="form-control"
                rows="3"
            ></textarea>
            <br>
            <button
                type="submit"
                class="btn btn-success"
                >Publish your comment
            </button>
        </form>
        <p v-if="error " class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
    name: "CommentEditor",
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            postSlug: null,
            commentBody: null,
            error: null
        }
    },
    methods: {
        onSubmit() {
            if (this.commentBody) {
                let endpoint = `/api/comments/${this.id}/`;
                apiService(endpoint, "PUT", { body: this.commentBody })
                    .then(() => {
                       this.$router.push({
                           name: "post",
                           params: { slug: this.postSlug }
                       }) 
                    })
            } else {
                this.error = "You can't submit an empty comment";
            }
        }
    },
    async beforeRouteEnter(to, from, next) {
        let endpoint = `/api/comments/${to.params.id}/`;
        let data = await apiService(endpoint);
        // to.params.previousComment = data.body;
        // to.params.postSlug = data.post_slug;
        return next(vm => (
            vm.commentBody = data.body,
            vm.postSlug = data.post_slug
        ));
    }
};
</script>