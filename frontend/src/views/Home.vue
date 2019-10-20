<template>
  <div class="home">
    <div class="container" style="padding: 15px" align="center">
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
	  <div class="hov">
		<div class="flex-container">
			<router-link :to="{ name: 'about-me' }"><img class="image-long-container" v-bind:src="sea" /></router-link>
		</div>
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
      this.coding = "https://i.imgur.com/DQnTrwM.jpg";
      this.blog = "https://i.imgur.com/hyENYMG.jpg";
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
	height: 350px;
}

.hov:hover .image-container {
	filter: brightness(15%);
}

.hov:hover .image-long-container {
	filter: brightness(40%);
}

.overlay {
    font-size: 40px;
    color: white;
    position: relative; 
    bottom: 220px;
    text-decoration: none;
}

.overlay-desc{
    font-size: 20px;
    color: white;
    position: relative; 
    bottom: 220px;
    text-decoration: none;
    padding: 5px;
}

.flex-container {
  display: flex;
}

.image-container {
    width: 600px;
    height: 350px;
    padding: 3px;
    filter: brightness(45%);
    -webkit-transition: all 1s ease;
    -moz-transition: all 1s ease;
    -o-transition: all 1s ease;
    -ms-transition: all 1s ease;
    transition: all 0.6s ease;
}

.image-long-container {
	width: 1194px;
	height: 320px;
	padding-top: 2px;
	filter: brightness(70%);
	-webkit-transition: all 1s ease;
    -moz-transition: all 1s ease;
    -o-transition: all 1s ease;
    -ms-transition: all 1s ease;
    transition: all 0.6s ease;
}

.overlay-long{
    font-size: 40px;
    color: white;
    position: relative; 
    bottom: 190px;
    text-decoration: none;
}
</style>
