<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import NavbarComponent from "@/components/Navbar.vue";

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
    this.setUserInfo();
  }
};
</script>

<style>
html,
body {
  font-family: "Raleway", sans-serif;
  color: black;
  background-color: #FFFFFF;
}

.btn:focus {
  box-shadow: none !important;
}

a:hover {
 cursor:pointer;
}

a > h3 {
  text-decoration: none;
}
</style>
