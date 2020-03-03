<template>
  <div style="height: 1200px">
    <ProjectsNavbarComponent />
    <img v-if="showScroll" class="scroll" :src="'../static/img/scroll.png'"/>
    <a v-on:click="scrollToTop">
      <img v-if="!showScroll" class="scroll-up" :src="'../static/img/scroll-up.png'"/>
    </a>
    <div align="center">
      <div class="fade-container">
        <div class="infade">
          <div class="head">
            <h2><strong>This Portfolio</strong></h2>
          </div>
          <div class="flex-container">
            <div class="stuff-container">
              <img class="image-container-project" v-bind:src="vueLogo" />
              <img class="image-container-project" v-bind:src="drfLogo" />
            </div>
            <div class="stuff-container">
              <p>
                This website is powered by a <strong>Full REST API</strong>, written
                in <strong>Python's Django-REST-Framework</strong>, and a <strong>Single Page </strong>
                frontend written with <strong>VueJS</strong>.
              </p>
              <h2>Features</h2>
              <ul>
                <li>REST API + Vue JS Single Page Application Frontend</li>
                <li>User Session Authentication</li>
                <li>User Registration/Login &#38; Permissions</li>
                <li>User Posting, Commenting, and Liking Comments</li>
                <li>Anonymous users can view all posts, comments, and like counters</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div id="linkout" v-if="SP1" class="fade-container" style="background-color: #E0E0E0; padding-top: 80px">
        <div class="infade">
          <div class="head">
            <h2><strong>LinkOut</strong></h2>
          </div>
          <div class="flex-container">
            <div class="stuff-container" style="width: 550px">
              <img class="image-container-project" v-bind:src="linkoutLogo" style="width: 540px; height: 320px;"/>
            </div>
            <div class="stuff-container" style="padding-left: 30px">
              <p>
                LinkOut, a website designed to provide resources to recently released ex-cons, 
                using Google Maps' API and geolocation to provide job resources available nearby.
              </p>
              <p>
                Build within a team of 3 others.
              <p>
              <h2>Features</h2>
              <ul>
                <li>Django Backend + VueJS handling all data storage and geolocation</li>
                <li>Integration with Google Maps' API</li>
                <li>Job finding and Community resources</li>
              </ul>
              <h4>
                One of four projects nominated for 
                <font color="#4B2E83"><strong>"Best Overall"</strong></font> at the 
                <font color="#4B2E83"><strong>WINFO 2020 Hackathon</strong></font>
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProjectsNavbarComponent from "@/components/ProjectsNavbar.vue";
import ThisWebsiteComponent from "@/components/ThisWebsite.vue";
import ProjectTwoComponent from "@/components/ProjectTwo.vue";
import DefaultProjectComponent from "@/components/DefaultProject.vue";

export default {
  name: "Projects",
  components: {
    ProjectsNavbarComponent
  },
  data() {
    return {
      SP1: false,
      SP2: false,
      showScroll: true,
      showBackToTop: false,
      vueLogo: null,
      drfLogo: null,
      linkoutLogo: null
    };
  },
  methods: {
    handleScroll() {
      if(window.scrollY > 180) {
        this.showScroll = false;
        this.SP1 = true;
      } else {
        this.showScroll = true;
      }
      if (window.scrollY > 800) {
        this.SP2 = true;
      }
    },
    loadImages() {
      this.vueLogo =
        "https://dwglogo.com/wp-content/uploads/2017/09/Vue-logo-001.svg";
      this.drfLogo = "https://www.django-rest-framework.org/img/logo.png";
      this.heroku = "https://i.imgur.com/dGIjsuX.png";
      this.linkoutLogo = "/static/img/linkout.png";
    },
    scrollToTop() {
      window.scrollBy(0, -1000)
    },
  },
  created() {
    document.title = "Projects";
    window.addEventListener("scroll", this.handleScroll);
    this.loadImages();
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  }
};
</script>

<style scoped>
.image-container-project {
  width: 300px;
  height: 150px;
}
</style>
