<template>
  <div class="home">
    <div class="container" style="padding: 40px" align="center">
      <h1 style="font-weight: bold">Hi, i'm David</h1>
      <h4 style="padding: 10px">And this is my Portfolio.</h4>
      
      <div class="flex-container">
        <div class="hov">
            <router-link :to="{ name: 'projects' }"><img class="image-container" v-bind:src="coding" /></router-link>
            <router-link :to="{ name: 'projects' }" class="overlay">Projects</router-link>
            <br>
            <router-link :to="{ name: 'projects' }" class="overlay-desc">My projects, including how this site was built.</router-link>
        </div>
        <div class="divider"></div>
        <div class="hov">
            <router-link :to="{ name: 'blog' }"><img class="image-container" v-bind:src="blog" /></router-link>
            <router-link :to="{ name: 'blog' }" class="overlay">Blog</router-link>
            <br>
            <router-link :to="{ name: 'blog' }" class="overlay-desc">Fully functioning blog, built with a backend API</router-link>
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
      blog: null
    };
  },
  methods: {
    myFunction: function() {
      this.coding = "https://i.imgur.com/DQnTrwM.jpg";
      this.blog = "https://i.imgur.com/hyENYMG.jpg";
    }
  },
  created() {
    this.myFunction();
    document.title = "David's Portfolio";
  }
};
</script>

<style scoped>

.hov:hover .image-container {
    filter: brightness(20%);
}

.overlay {
    font-size: 40px;
    color: white;
    position: relative; 
    bottom: 250px;
    text-decoration: none;
}

.overlay-desc{
    font-size: 20px;
    color: white;
    position: relative; 
    bottom: 250px;
    text-decoration: none;
    padding: 5px;
}

.flex-container {
  display: flex;
}

.image-container {
    width: 600px;
    height: 400px;
    padding: 10px;
    filter: brightness(55%);
    -webkit-transition: all 1s ease;
    -moz-transition: all 1s ease;
    -o-transition: all 1s ease;
    -ms-transition: all 1s ease;
    transition: all 0.6s ease;
}

.divider {
  width: 10px;
  background-color: white;
}
</style>
