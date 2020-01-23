<template>
  <div class="home">
    <div class="container" style="padding-top: 50px; padding-bottom: 100px" align="center">
      <h1 style="font-weight: bold; padding-top: 30px">Hi, i'm David</h1>
      <h4 style="padding: 10px">and this is my Portfolio.</h4>
    </div>
    <div class="container-dark">
      <div class="flex-container">
        <div class="hov">
          <router-link :to="{ name: 'projects' }"><img class="image-container" style="" v-bind:src="coding" /></router-link>
          <router-link :to="{ name: 'projects' }" class="overlay">Projects</router-link>
          <router-link :to="{ name: 'projects' }" class="overlay-desc">My projects, including how this site was built.</router-link>
        </div>
        <div class="hov">
          <router-link :to="{ name: 'blog' }"><img class="image-container" style="height: 95.2%" v-bind:src="blog" /></router-link>
          <router-link :to="{ name: 'blog' }" class="overlay">Blog</router-link>
          <router-link :to="{ name: 'blog' }" class="overlay-desc">Functional blog, built with a backend API.</router-link>
        </div>
        <div class="hov">
          <router-link :to="{ name: 'about-me' }"><img class="image-container" v-bind:src="sea" /></router-link>
          <router-link :to="{ name: 'about-me' }" class="overlay">About Me</router-link> 
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      coding: null,
      blog: null,
      sea: null
    };
  },
  methods: {
    myFunction: function() {
      this.coding = "/static/img/code.jpg";
      this.blog = "/static/img/blog.jpg";
      this.sea = "/static/img/sea.jpg";
    }
  },
  created() {
    this.myFunction();
    document.title = "David's Portfolio";
  }
};
</script>

<style scoped>

.hov {
  position: relative;
  text-align: center;
  width: 400px;
}

.hov:hover .image-container {
	filter: brightness(15%);
}

.overlay {
    font-size: 40px;
    color: white;
    position: absolute; 
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-decoration: none;
}

.overlay-desc {
    font-size: 18px;
    color: white;
    position: absolute; 
    top: 60%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-decoration: none;
}

.flex-container {
  display: flex;
  flex-wrap: wrap;
}

.image-container {
    width: 100%;
    padding: 0 2px 2px 2px;
    filter: brightness(45%);
    border-radius: 50%;
    -webkit-transition: all 1s ease;
    -moz-transition: all 1s ease;
    -o-transition: all 1s ease;
    -ms-transition: all 1s ease;
    transition: all 0.6s ease;
}

.overlay-long {
    font-size: 40px;
    color: white;
    position: absolute; 
    left: 310px;
    bottom: 75px;
    text-decoration: none;
}

.container-dark {
  background-color: #181818;
  height: 100%;
}
</style>
