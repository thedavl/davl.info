<template>
    <div style="height: 3000px">
        <div>
            <div class="page">
                <div class="fade-container">
                  <p class="scroll-txt">Learn more about me</p>
                  <img class="scroll-down" :src="'../static/img/downarrow.png'"/>
                </div>
                <div class="fade-container" id="title">
                  <p class="container-title">Hi, I'm David</p>
                  <p class="container-sub-title">I’m a university student and aspiring software engineer from Seattle.</p>
                </div>
            </div>
            <div class="page background-purp">
                <div class="fade-container" v-if="SP1">
                    <br>
                      <div class="flex-container">
                          <div>
                              <img 
                                  id="uw" 
                                  v-bind:src="'../static/img/uw.png'"/>
                          </div>
                          <div class="text-box">
                              <p class="desc-container align-left" id="student">
                                  Student at the University of Washington, Seattle
                              </p>
                              <p class="sub-desc-container" id="coursework">
                                Coursework focusing on programming, including: <br>
                                <ul>
                                <li>Data Structures/Algorithms</li>
                                <li>Data Programming in Python, R</li>
                                <li>Web Programming</li>
                                </ul>
                              </p>
                          </div>
                      </div>
                      <div class="flex-container">
                          <div class="text-box">
                              <p class="desc-container align-right" id="research">
                                  Undergraduate Researcher Ubiquitous Computing Lab</p>
                              <p class="sub-desc-container align-right"> 
                                <strong>Built two web apps for the lab, used to record and label cough recordings.</strong> <br><br>
                                Websites are used to gather/label cough data for the lab’s cough verification machine learning models.
                                Both are designed to be highly scaleable, utilizing AWS services.
                              </p>
                          </div>
                          <div>
                              <img
                                  class="image-container"
                                  id="ubicomp"
                                  v-bind:src="'../static/img/ubicomplab.png'"/>
                          </div>
                      </div>
                </div>
            </div>
            <div class="page">
              <div class="fade-container" v-if="SP2">
                  <div class="center">
                      <div class="flex-container">
                          <div class="skills-container">
                              <img
                                  class="image-container"
                                  id="code"
                                  v-bind:src="'../static/img/code.png'"
                              />
                              <p class="desc-container">
                                Languages
                              </p>
                              <p class="detail-container">
                                <img
                                  class="smaller-mini-logo"
                                  v-bind:src="'../static/img/java.png'">
                                <strong>Java</strong><br>
                              </p>
                              <div class="list">
                                The focus of my cs fundamental coursework, 
                                including data structures/algorithms<br><br>
                              </div>
                              <p class="detail-container">
                                <img
                                  class="smaller-mini-logo"
                                  v-bind:src="'../static/img/js.png'">
                                <strong>Javascript</strong><br>
                              </p>
                              <div class="list">
                                Including VueJs, React frameworks<br>
                                Web programming coursework &#38; undergraduate research<br><br>
                              </div>
                              <p class="detail-container">
                                <img
                                  class="smaller-mini-logo"
                                  v-bind:src="'../static/img/python.png'">
                                <strong>Python</strong><br>
                              </p>
                              <div class="list">
                                Django REST Framework, building backend APIs, and
                                Data programming coursework
                              </div>
                          </div>
                          <div class="skills-container">
                              <img
                                  class="image-container"
                                  id="frameworks"
                                  v-bind:src="'../static/img/framework.png'"
                              />
                              <p class="desc-container">
                                Frameworks
                              </p>
                              <p class="detail-container">
                                <img
                                  class="mini-logo"
                                  v-bind:src="'../static/img/Vue_js.png'">
                                  <strong>VueJS (Javascript)</strong><br>
                              </p>
                              <div class="list">
                                I've built multiple frontends with VueJS, 
                                for personal project and my undergraduate research. 
                                My experience includes building blog UIs, survey forms, 
                                audio collection forms, and informational webpages.<br><br>
                              </div>
                              <p class="detail-container">
                                <img
                                  class="smaller-mini-logo"
                                  v-bind:src="'../static/img/django.png'">
                                <strong>Django (Python)</strong><br>
                              </p>
                              <div class="list">
                                My work includes secured blog APIs, Survey Data handling APIs, as well as interaction with AWS S3 Storage and PostgreSQL storage, all
                                with user signup/authentication features.<br><br>
                              </div>
                              <p class="detail-container">
                                <img
                                  class="mini-logo"
                                  v-bind:src="'../static/img/node.png'">
                                <strong>NodeJS (Javascript)</strong><br>
                              </p>
                              <div class="list">
                                I've started teaching myself NodeJS most recently, and have created a basic CRUD API supporting secure user signup and authentication.
                              </div>
                          </div>
                          <div class="skills-container">
                              <img
                                  class="image-container"
                                  id="bubble"
                                  v-bind:src="'../static/img/bubble.png'"
                              />
                              <p class="desc-container">
                                Experience
                              </p>
                              <div class="detail-container">
                                <strong>Development QA Intern</strong><br>
                                Heated Details Inc, Seattle<br>
                                <div class="list">
                                  <ul>
                                  <li>Assisting in the testing, development, and integration of key web applications.</li>
                                  <li>Worked closely with the dev team to improve UI/UX, functionality, and debugging.</li>
                                  </ul>
                                </div>
                                <strong>2020 Winfo (UW) Hackathon</strong><br>
                                <div class="list">
                                  <ul>
                                    <li>Worked in a team of four to build a website designed to provide resources to recently released ex-cons</li>
                                    <li>One of four teams nominated for “Best Overall”, out of 80 total competing teams.</li>
                                  </ul>
                                </div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
            </div>
            <div class="page background-purp" id="link-page">
              <div class="fade-container" v-if="SP3" id="link-center">
                  Connect with me
                  <div class="center">
                      <div class="flex-container">
                          <div class="link-image">
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
                          <div class="link-image">
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
                          <div class="link-image">
                              <img
                                  class="image-container"
                                  v-bind:src="'../static/img/email.png'"
                                  style="width: 170px"
                              />
                              <h3 style="color: black">thedavl@uw.edu</h3>
                          </div>
                      </div>
                  </div>
              </div>
            </div>
        </div>
        <div class="fade-container" v-if="showScrollUp">
          <a v-on:click="scrollToTop">
              <div class="scroll-up">
                <img class="scroll-up-icon" :src="'../static/img/upload.png'"/>
                <p class="scroll-up-txt">Back to top</p>
              </div>
          </a>
        </div>
    </div>
</template>

<script>
export default {
    name: "Home",
    data() {
        return {
            SP1: false,
            SP2: false,
            SP3: false,
            showScrollUp: false,
            showScrollText: true
        };
    },
    methods: {
        handleScroll() {
            if(window.scrollY > 300) {
                this.SP1 = true;
            } else {
                this.showScrollUp = false;
            }
            if (window.scrollY > 1200) {
                this.SP2 = true;
                this.showScrollUp = true
            }
            if (window.scrollY > 2000) {
                this.SP3 = true;
            }
        },
        scrollToTop() {
            window.scrollBy(0, -5000)
        }
    },
    created() {
        window.addEventListener("scroll", this.handleScroll);
    },
    destroyed() {
        window.removeEventListener("scroll", this.handleScroll);
    }
}
</script>

<style scoped>
.smaller-mini-logo {
  width: 50px;
  padding: 0 12px 0 12px;
}
.mini-logo {
  width: 50px;
}
.link-image {
  width: 300px;
}

.page {
  min-height: 94vh;
  margin: 0 auto;
  position: relative;
  text-align: center;
}

.background-purp {
  background-color: #ece8fc;
}

.center {
    text-align: center;
}

.skills-container {
  width: 450px;
  padding-left: 10px;
  padding-right: 10px;
}

.align-left {
    text-align: left;
}

.align-right {
    text-align: right;
}

.desc-container {
  max-width: 360px;
  font-size: 23px;
  font-weight: bold;
  padding-bottom: 15px;
  border-bottom: 1.5px solid black;
}

.sub-desc-container {
  font-size: 20px;
  max-width: 360px;
}

.detail-container {
  text-align: left;
  font-size: 20px;
  max-width: 360px;
}

.list {
  font-size: 17px;
  text-align: left;
}

#link-page {
  min-height: 70vh;
}

#link-center {
  color: #632494;
  font-size: 60px;
  font-weight: bold;
  width: 100%;
  margin: 0 auto;
  padding-top: 80px;
}

#title {
  position: absolute;
  top: 26%;
  width: 100%;
  margin: 0 auto;
}

#bubble {
  margin-top: 20px;
  margin-right: 40px;
  height: 240px;
  width: 230px;
}

#code {
  margin-right: 40px;
  width: 260px;
  height: 260px;
}

#frameworks {
  margin-right: 40px;
  margin-bottom: 20px;
  width: 240px;
  height: 240px;
}

#ubicomp {
  background-color: black;
  width: 380px;
  height: 100px;
  margin: 20px 0 0 30px;
}

#uw {
  max-height: 250px;
  max-width: 360px;
  margin-top: 20px;
}

#student {
  margin-left: 40px;
}

#coursework {
  margin-left: 40px;
  text-align: left;
}

.container-title {
    text-align: center;
    color: #632494;
    font-size: 75px;
    font-weight: bold;
}

.container-sub-title {
    text-align: center;
    font-size: 23px;
    font-weight: bold;
    max-width: 380px;
    margin: 0 auto;
}

.flex-container {
    display: flex;
    justify-content: center;
    padding-top: 50px;
    flex-wrap: wrap;
}

.text-box {
    padding: 15px;
}

.fade-container {
    -webkit-animation: fadein 2s; /* Safari, Chrome and Opera > 12.1 */
    -moz-animation: fadein 2s; /* Firefox < 16 */
    -ms-animation: fadein 2s; /* Internet Explorer */
    -o-animation: fadein 2s; /* Opera < 12.1 */
    animation: fadein 2s;
}

.scroll-down {
  width: 45px;
  position: absolute;
  bottom: 5%;
  margin-left: -23px;
}

.scroll-txt {
  font-size: 20px;
  font-weight: bold;
  width: 100%;
  position: absolute;
  bottom: 12%;
}

.scroll-up {
  position: fixed;
  left: 82.5%;
  bottom: 4%;
}

.scroll-up-icon {
  width: 35px;
  margin-left: 22px;
}
.scroll-up-txt {
  width: 80px;
  text-align: center;
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