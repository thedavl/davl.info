<template>
    <div class="post-actions">
        <router-link 
            :to="{name: 'post-editor', params: { slug: slug }}"
            class="btn btn-sm btn-outline-secondary mr-1"
            >Edit
        </router-link>
        <button
            class="btn btn-sm btn-outline-danger"
            @click="deletePost"
            >Delete
        </button>
    </div>
</template>
<script>
import { apiService } from "@/common/api.service.js";
export default {
    name: "PostActions",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    methods: {
        async deletePost() {
            let endpoint = `/api/posts/${this.slug}/`;
            try {
                await apiService(endpoint, "DELETE");
                this.$router.push("/")
            } catch (err) {
                console.log(err)
            }
        }
    }
}
</script>