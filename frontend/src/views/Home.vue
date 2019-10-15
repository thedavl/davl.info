<template>
  <div class="home">
    <div class="container" style="padding: 40px" align="center">
      <h1 style="font-weight: bold">Hi, i'm David</h1>
      <br>
      <h3>This is a website i made to showcase some of my projects and skills!</h3>
      <br>
      <div class="flex-container">
        <div class="div-flex">
          <br>
          <h3 style="font-size: 25px">Please visit the projects tab to see a bit of what i've done, and how this site was made <br></h3>
        </div>
        <div class="divider"></div>
        <div class="div-flex">
          <br>
          <h3 style="font-size: 25px">The blog section of this site showcases features of the REST API i've built, and some functionalities i've implemented!</h3>
        </div>
      </div>
      <div class="flex-container">
        <div class="button-container">
          <router-link
            :to="{ name: 'projects' }"
            class="btn btn-sm btn-primary"
            >Projects
          </router-link>
        </div>
        <div class="divider"></div>
        <div class="button-container">
          <router-link
            :to="{ name: 'blog' }"
            class="btn btn-sm btn-info"
            >Blog
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    document.title = "David's Portfolio";
  }
}
</script>

<style scoped>
.flex-container {
  display: flex;
  align-items:stretch;
  justify-content: center;
}

.div-flex {
  border-top-right-radius:15px;
  border-top-left-radius:15px;
  width: 500px;
  height: 150px;
  background-color: lightgrey;
  padding: 10px 25px;
}

.button-container {
  border-bottom-right-radius:15px;
  border-bottom-left-radius:15px;
  width: 500px;
  height: 60px;
  background-color: lightgrey;
}

.divider {
  width: 10px;
  background-color: white;
}

.div-right {
  border-left: 10px;
  border-color: black
}

</style>
