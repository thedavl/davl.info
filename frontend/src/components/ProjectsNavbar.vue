<template>
  <div>
    <div class="projecto">
      <button
        type="button"
        v-on:click="toggleThisWebsite"
        class="btn btn-sm btn-outline-info ml-1"
      >
        This Website
      </button>
      <button
        type="button"
        v-on:click="toggleProjectTwo"
        class="btn btn-sm btn-outline-info ml-1"
      >
        Auto-Sort Drawer
      </button>
    </div>
    <div align="center" style="margin-top:10px">
      <ThisWebsiteComponent v-if="displayThisSite" />
      <ProjectTwoComponent v-else-if="display2" />
      <DefaultProjectComponent v-else />
    </div>
  </div>
</template>

<script>
import ThisWebsiteComponent from "@/components/ThisWebsite.vue";
import ProjectTwoComponent from "@/components/ProjectTwo.vue";
import DefaultProjectComponent from "@/components/DefaultProject.vue";

export default {
  name: "ProjectsNavbarComponent",
  components: {
    ThisWebsiteComponent,
    ProjectTwoComponent,
    DefaultProjectComponent
  },
  data() {
    return {
      // research using "isActive" vue functionality
      displayThisSite: false,
      display2: false
    };
  },
  methods: {
    toggleThisWebsite() {
      this.displayThisSite = !this.displayThisSite;
      this.display2 = false;
    },
    toggleProjectTwo() {
      this.display2 = !this.display2;
      this.displayThisSite = false;
    }
  }
};
</script>

<style scoped>
.projecto {
  text-align: center;
  margin-top: 20px;
  position: relative;
  left: 12px;
}
</style>
