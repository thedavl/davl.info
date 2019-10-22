<template>
  <div class="home" style="margin-bottom: 30px">
    <div class="container" style="padding: 15px" align="center">
      <h1 style="font-weight: bold">Hi, i'm David</h1>
      <h4 style="padding: 10px">and this is my Portfolio.</h4>
    </div>
    <div class="flex-container">
      <div class="hov">
        <router-link :to="{ name: 'projects' }"><img class="image-container" v-bind:src="coding" /></router-link>
        <router-link :to="{ name: 'projects' }" class="overlay">Projects</router-link>
        <router-link :to="{ name: 'projects' }" class="overlay-desc">My projects, including how this site was built.</router-link>
      </div>
      <div class="hov">
        <router-link :to="{ name: 'blog' }"><img class="image-container" v-bind:src="blog" /></router-link>
        <router-link :to="{ name: 'blog' }" class="overlay">Blog</router-link>
        <router-link :to="{ name: 'blog' }" class="overlay-desc">Fully functioning blog, built with a backend API</router-link>
      </div>
    </div>
    <div class="hov-long">
      <div class="flex-container">
          <router-link :to="{ name: 'about-me' }"><img class="image-long-container" v-bind:src="sea" /></router-link>
        <router-link :to="{ name: 'about-me' }" class="overlay-long">About Me</router-link> 
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
      this.coding = "https://i.imgur.com/tEVwLnR.jpg";
      this.blog = "https://i.imgur.com/GdbwzkU.jpg";
      this.sea = "https://i.imgur.com/bJBoY3u.jpg"
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
}

.hov-long {
  border-style: dashed;
  border-color: aqua;
  position: relative;
  text-align: center;
  margin: 0 155px 0 155px;
}

.hov:hover .image-container {
	filter: brightness(15%);
}

.hov-long:hover .image-long-container {
	filter: brightness(40%);
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
    font-size: 20px;
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
    -webkit-transition: all 1s ease;
    -moz-transition: all 1s ease;
    -o-transition: all 1s ease;
    -ms-transition: all 1s ease;
    transition: all 0.6s ease;
}

.image-long-container {
    padding-top: 2px;
    filter: brightness(70%);
    -webkit-transition: all 1s ease;
    -moz-transition: all 1s ease;
    -o-transition: all 1s ease;
    -ms-transition: all 1s ease;
    transition: all 0.6s ease;
    float: none;
    display: block;
	  margin: 0 auto;
    width: 1040px;
    padding: 2px 18px 0 18px;
}

.overlay-long{
    font-size: 40px;
    color: white;
    position: absolute; 
    bottom: 95px;
    text-decoration: none;
}
</style>
