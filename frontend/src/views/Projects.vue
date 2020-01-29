<template>
  <div class="projects">
    <ProjectsNavbarComponent />
  </div>
</template>

<script>
import ProjectsNavbarComponent from "@/components/ProjectsNavbar.vue";

export default {
  name: "Projects",
  components: {
    ProjectsNavbarComponent
  },
  created() {
    document.title = "Projects";
  }
};
</script>

<style scoped></style>
