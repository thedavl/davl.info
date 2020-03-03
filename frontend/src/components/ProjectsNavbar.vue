<template>
  <div align="center">
    <nav
    class="navbar navbar-expand-lg navbar-light"
    style="background-color: #D3D3D3, height: 200px"
    >
      <button
          class="navbar-toggler"
          type="button btn-light"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
          style="color: BLACK"
        >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav w-100 justify-content-center">
          <li class="nav-item slide-center-out">
            <a
            v-on:click="scrollTo1"
            class="nav-text-small"
            >
              This Website
            </a>
          </li>
          <li class="nav-item slide-center-out">
            <a
            v-on:click="scrollTo2"
            class="nav-text-small"
            >
            LinkOut
            </a>
          </li>
        </ul>
      </div>
    </nav>
    <div style="width: 30%; border-bottom: 1.5px solid #E0E0E0"></div>
  </div>
</template>

<script>
export default {
  name: "ProjectsNavbarComponent",
  methods: {
    scrollTo1() {
      window.scrollBy(0, 100)
    },
    scrollTo2() {
      window.scrollBy(0, 600)
    }
  }
};
</script>

<style scoped>
.projecto {
  text-align: center;
  margin-top: 20px;
  position: relative;
  left: 12px;
}

.nav-text-small {
  margin-left: 25px;
  margin-right: 25px;
  font-size: 16px;
  color: BLACK;
}
</style>
