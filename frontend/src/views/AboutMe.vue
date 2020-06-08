<template>
  <div style="height: 2300px">
    <img v-if="showScroll" class="scroll" :src="'../static/img/scroll.png'"/>
    <a v-on:click="scrollToTop">
      <img v-if="!showScroll" class="scroll-up" :src="'../static/img/scroll-up.png'"/>
    </a> 
    <div align="center">
      <div class="fade-container" style="padding-top: 80px">
        <div class="infade">
          <div class="head">
            <h2><strong>About Me</strong></h2>
          </div>
          <div class="flex-container">
            <div class="stuff-container">
              <img 
                class="image-container" 
                v-bind:src="'../static/img/uw.png'" 
                style="margin-bottom: 20px"/>
              <h3>
                Student at the <br>
                <font color="#4B2E83"><strong>University of Washington</strong></font>  <br>
                Seattle
              </h3>
            </div>
            <div class="stuff-container">
              <img
                class="image-container"
                v-bind:src="'../static/img/code2.png'"
                style="margin-bottom: 20px"
              />
              <h3>
                Coursework focused on <br />
                coding fundamentals &#38; <br />
                data programming.
              </h3>
            </div>
          </div>
        </div>
      </div>
      <div class="fade-container" v-if="SP1" style="background-color: #E0E0E0; padding-top: 80px">
        <div class="infade">
          <div class="head">
            <h2><strong>Skills and Courses</strong></h2>
          </div>
          <div class="flex-container">
            <div class="stuff-container">
              <img
                class="image-container"
                v-bind:src="'../static/img/code3.png'"
                style="width: 170px"
              />
              <h3>Languages</h3>
              <hr />
              <h5><strong>Java</strong></h5> 
              <h6>The focus of my coursework</h6>
              <h5><strong>Python</strong></h5>
              <h6>Intermediate data/general programming</h6>
              <h5><strong>R</strong></h5>
              <h6>Limited Data Programming</h6>
            </div>
            <div class="stuff-container">
              <img
                class="image-container"
                v-bind:src="'../static/img/course.png'"
                style="width: 180px"
              />
              <h3>Coursework</h3>
              <hr />
              <h5><strong>CSE142 &#38; CSE143</strong></h5>
              <h6>Basic &#38; Advanced control/data structures in Java</h6>
              <h5><strong>CSE163</strong></h5>
              <h6>
                Intermediate data programming in Python, python data libraries,
                program efficiency/style
              </h6>
              <h5><strong>INFO 201</strong></h5>
              <h6>
                R data programming, Version control, Data wrangling, Databases
              </h6>
            </div>
            <div class="stuff-container">
              <img
                class="image-container"
                v-bind:src="'../static/img/other.png'"
                style="width: 180px"
              />
              <h3>Other</h3>
              <hr />
              <h5><strong>WINFO 2020 Hackathon</strong></h5>
              <h6>One of four teams nominated for "Best Overall", out of 80 total teams</h6>
              <h5><strong>Microsoft Office Certifications</strong></h5>
              <h6>Officially certified in Excel, Word, Powerpoint</h6>
            </div>
          </div>
        </div>
      </div>
      <div class="fade-container" v-if="SP2" style="padding-top: 80px">
        <div class="infade">
          <h2 class="head"><strong>Links</strong></h2>
          <div class="flex-container">
            <div class="stuff-container">
              <a class="link" href="https://www.linkedin.com/in/thedavl/">
                <img
                  class="image-container"
                  v-bind:src="'../static/img/linkedin.png'"
                  style="width: 170px"
                />
                <h3 href="https://www.linkedin.com/in/thedavl/">
                  My LinkedIn
                </h3>
              </a>
            </div>
            <div class="stuff-container">
              <a class="link" href="https://github.com/thedavl">
                <img
                  class="image-container"
                  v-bind:src="'../static/img/github.png'"
                  style="width: 170px"
                />
                <h3 href="https://github.com/thedavl">
                  My Github
                </h3>
              </a>
            </div>
            <div class="stuff-container">
              <img
                class="image-container"
                v-bind:src="'../static/img/email.png'"
                style="width: 170px"
              />
              <h3>thedavl@uw.edu</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutMe",
  data() {
    return {
      SP1: false,
      SP2: false,
      showScroll: true
    };
  },
  methods: {
    handleScroll() {
      if(window.scrollY > 200) {
        this.showScroll = false;
        this.SP1 = true;
      } else {
        this.showScroll = true;
      }
      if (window.scrollY > 800) {
        this.SP2 = true;
      }
    },
    scrollToTop() {
      window.scrollBy(0, -1500)
    }
  },
  created() {
    document.title = "About Me";
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  }
};
</script>

<style>

.scroll {
  position: fixed;
  width: 30px;
  left: 48.5%;
  bottom: 3%;
}

.scroll-up {
  position: fixed;
  width: 30px;
  left: 95%;
  bottom: 5%;
}

.head {
  height: 40px;
  width: 280px;
  margin-bottom: 50px;
  border-bottom: 1.5px solid #4B2E83
}

.flex-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.fade-container > .infade {
  padding-top: 25px;
  padding-bottom: 25px;
  -webkit-animation: fadein 2s; /* Safari, Chrome and Opera > 12.1 */
  -moz-animation: fadein 2s; /* Firefox < 16 */
  -ms-animation: fadein 2s; /* Internet Explorer */
  -o-animation: fadein 2s; /* Opera < 12.1 */
  animation: fadein 2s;
}

.stuff-container {
  width: 380px;
  padding-left: 10px;
  padding-right: 10px;
}
.logo {
  height: 15px;
  width: 15px;
  margin-right: 5px;
}

.texto {
  font: 51px;
}

.image-container {
  width: 260px;
  height: 180px;
  padding-bottom: 15px;
  margin:10px;
}

.link {
  text-decoration: none;
  color: black;
}

@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Firefox < 16 */
@-moz-keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Safari, Chrome and Opera > 12.1 */
@-webkit-keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Internet Explorer */
@-ms-keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Opera < 12.1 */
@-o-keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
