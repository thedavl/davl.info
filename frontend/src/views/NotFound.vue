<template>
  <div class="not-found">
    <h1 id="notfound">{{ message }}</h1>
  </div>
</template>

<script>
export default {
  name: "NotFound",
  data() {
    return {
      message: "404 - Page Not Found"
    };
  }
};
</script>

<style scoped>
#notfound {
  color: red;
  text-align: center;
}
</style>
