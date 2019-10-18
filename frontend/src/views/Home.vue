<template>
  <div class="home">
    <div class="container" style="padding: 40px" align="center">
      <h1 style="font-weight: bold">Hi, i'm David</h1>
      <h4 style="padding: 10px">And this is my Portfolio.</h4>
      
      <div class="flex-container">
        <div>
            <img class="image-container" style="filter: brightness(50%)" v-bind:src="coding" />
            <router-link :to="{ name: 'projects' }" class="overlayL">Projects</router-link>
            <p class="overlayL-desc">My projects, including how this site was built.</p>
        </div>
        <div class="divider"></div>
        <div>
            <img class="image-container" style="filter: brightness(40%)" v-bind:src="blog" />
            <router-link :to="{ name: 'blog' }" class="overlayR">Blog</router-link>
            <p class="overlayR-desc">Fully functioning blog, showing off the backend API</p>
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

.overlayL {
    font-size: 40px;
    color: white;
    position: relative; 
    bottom: 250px;
    text-decoration: none;
}

.overlayR {
    font-size: 40px;
    color: white;
    position: relative; 
    bottom: 250px;
    text-decoration: none;
}

.overlayL-desc{
    font-size: 20px;
    color: white;
    position: relative; 
    bottom: 250px;
    text-decoration: none;
}

.overlayR-desc{
    font-size: 20px;
    color: white;
    position: relative; 
    bottom: 250px;
    text-decoration: none;
}

.overlayR:hover {
    -webkit-transform: scale(1.2);
    -ms-transform: scale(1.2);
    transform: scale(1.3);
    transition: 0.5s ease;
}

.overlayL:hover {
    -webkit-transform: scale(1.2);
    -ms-transform: scale(1.2);
    transform: scale(1.3);
    transition: 0.5s ease;
}

.flex-container {
  display: flex;
}

.image-container {
    width: 600px;
    height: 400px;
    padding: 10px;
}

.divider {
  width: 10px;
  background-color: white;
}
</style>
