<template>
  <div class="home">
    <div
      class="container"
      style="padding-top: 50px; padding-bottom: 100px"
      align="center"
    >
      <h1 style="padding-top: 30px">Hi, i'm <font color="#8c00ff"><strong>David Lee</strong></font></h1>
      <h4 style="padding: 10px">and this is my Portfolio.</h4>
    </div>
    <div class="container-dark">
      <div class="flex-container">
        <div class="hov">
          <router-link :to="{ name: 'about-me' }"
            ><img class="image-container" v-bind:src="sea"
          /></router-link>
          <router-link :to="{ name: 'about-me' }" class="overlay"
            >Me</router-link
          >
        </div>
        <div class="hov">
          <router-link :to="{ name: 'projects' }"
            ><img class="image-container-dark" v-bind:src="coding"
          /></router-link>
          <router-link :to="{ name: 'projects' }" class="overlay"
            >Projects</router-link
          >
        </div>
        <div class="hov">
          <router-link :to="{ name: 'blog' }"
            ><img class="image-container" v-bind:src="blog"
          /></router-link>
          <router-link :to="{ name: 'blog' }" class="overlay">Blog</router-link>
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
    getImages() {
      this.coding = "/static/img/code.jpg";
      this.blog = "/static/img/blog.jpg";
      this.sea = "/static/img/city.jpg";
    }
  },
  created() {
    this.getImages();
    document.title = "David's Portfolio";
  }
};
</script>

<style scoped>
.hov {
  position: relative;
  text-align: center;
  margin: 30px 10px 30px 10px;
}

.hov:hover .image-container,
.hov:hover .image-container-dark {
  filter: brightness(40%);
}

.overlay {
  font-size: 50px;
  color: #d3d3d3;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-decoration: none;
  text-shadow: 0 0 5px black;
}

.flex-container {
  display: flex;
  flex-wrap: wrap;
}

.image-container {
  width: 300px;
  height: 280px;
  filter: brightness(70%);
  border-radius: 60%;
  -webkit-transition: all 1s ease;
  -moz-transition: all 1s ease;
  -o-transition: all 1s ease;
  -ms-transition: all 1s ease;
  transition: all 0.6s ease;
}

.image-container-dark {
  width: 300px;
  height: 280px;
  filter: brightness(90%);
  border-radius: 60%;
  -webkit-transition: all 1s ease;
  -moz-transition: all 1s ease;
  -o-transition: all 1s ease;
  -ms-transition: all 1s ease;
  transition: all 0.6s ease;
}

.container-dark {
  background-color: #E0E0E0;
  height: 100%;
}
</style>
