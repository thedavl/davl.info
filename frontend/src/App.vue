<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import NavbarComponent from "@/components/Navbar.vue"

export default {
  name: "App",
  components: {
    NavbarComponent
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
    
    }
  },
  created() {
    this.setUserInfo()
  }
};
</script>

<style>
    html, body {
      height: 100%;
      /* font-family: "Playfair Display", serif; */
      /* font-family: 'IBM Plex Sans', sans-serif; */
      font-family: 'Raleway', sans-serif;
      background-color: #D3D3D3
    }

    .btn:focus {
      box-shadow: none !important;
    }
</style>
