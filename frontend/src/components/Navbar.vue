<template>
  <nav
    class="navbar navbar-expand-lg navbar-light"
    style="background-color: black, height: 200px"
  >
    <div
      class="container"
      style="padding-top: 12px"
    >
      <button
        class="navbar-toggler"
        type="button btn-light"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
      <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li v-on:click="setPageTitle" class="nav-item slide-center-out">
            <router-link :to="{ name: 'home' }" class="nav-text"
              >Home
            </router-link>
          </li>
          <li class="nav-item slide-center-out">
            <router-link :to="{ name: 'blog' }" class="nav-text"
              >Blog
            </router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li v-if="isLoggedIn" class="nav-item slide-center-out">
            <a class="nav-text" href="/accounts/logout/">Logout</a>
          </li>
          <li v-else class="nav-item slide-center-out">
            <a class="nav-text" href="/accounts/login/">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "NavBarComponent",
  data() {
    return {
      currentUser: null
    };
  },
  computed: {
    isLoggedIn() {
      return this.currentUser !== "";
    }
  },
  methods: {
    setPageTitle() {
      document.title = "David's Portfolio";
    },
    setCurrentUser() {
      let endpoint = `api/user/`;
      apiService(endpoint).then(data => {
        if (data) {
          this.currentUser = data.username;
        } else {
          this.setPageTitle("username error");
        }
      });
    }
  },
  created() {
    this.setCurrentUser();
  }
};
</script>

<style>

.nav-item {
  padding-bottom: 6px;
}

.nav-text {
  margin-left: 25px;
  margin-right: 25px;
  font-size: 18px;
  color: black;
}

.nav-text:hover {
  text-decoration: none;
  color: black;
}

.slide-center-out {
  text-decoration: none;
  display: inline-block;
  color: black;
}

/* add a empty string after the elment with class .slide-center-out  */
.slide-center-out:after {
  content: "";
  display: block;
  height: 1.5px;
  width: 0;
  background: transparent;
  transition: width 0.5s ease, background-color 0.5s ease;
  -webkit-transition: width 0.5s ease, background-color 0.5s ease;
  -moz-transition: width 0.5s ease, background-color 0.5s ease;

  margin: auto; /* center the cotent so it will sliding from the midddle to the left and right */
}

/* Change the width and background on hover, aka sliding from the middle to the left and right */
.slide-center-out:hover:after {
  width: 100%;
  background: black;
}
</style>
