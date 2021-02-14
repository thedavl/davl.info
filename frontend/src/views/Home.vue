<template>
    <div style="height: 3000px">
        <div>
            <div class="page">
                <div class="fade-container">
                  <p class="scroll-txt">More about me</p>
                </div>
                <div class="fade-container" id="title">
                  <p class="container-title">Hi, I'm David</p>
                  <p class="container-sub-title">I’m a university student and aspiring software engineer from Seattle.</p>
                </div>
                <div class="scroll-dn">
                  <svg xmlns='http://www.w3.org/2000/svg' class='ionicon' 
                  viewBox='0 0 512 512'><title>Arrow Down</title>
                  <path fill='none' stroke='currentColor' 
                  stroke-linecap='round' stroke-linejoin='round' 
                  stroke-width='48' d='M112 268l144 144 144-144M256 392V100'/></svg>
                </div>
            </div>
            <div class="page background-purp">
                <ProjectsComponent v-show="SP1" />
            </div>
            <div class="page">
                <AcademicsComponent v-show="SP2" />
            </div>
            <div class="page background-purp">
              <br><br>
              <SkillsComponent  v-show="SP3" />
            </div>
            <div class="page" id="link-page">
              <SocialMediaComponent v-show="SP4" />
            </div>
        </div>
        <div class="fade-container" v-show="showScrollUp">
          <a v-on:click="scrollToTop">
              <div class="scroll-up">
                <div class="scroll-up-icon">
                  <svg xmlns='http://www.w3.org/2000/svg' class='ionicon' 
                    viewBox='0 0 512 512'><title>Arrow Up</title>
                  <path fill='none' stroke='currentColor' 
                  stroke-linecap='round' stroke-linejoin='round' 
                  stroke-width='48' d='M112 268l144 144 144-144M256 392V100'/></svg>
                </div>
                <p class="scroll-up-txt">Back to top</p>
              </div>
          </a>
        </div>
    </div>
</template>

<script>
import AcademicsComponent from "@/components/AcademicsComponent.vue"
import SkillsComponent from "@/components/SkillsComponent.vue"
import SocialMediaComponent from "@/components/SocialMediaComponent.vue"
import ProjectsComponent from "@/components/ProjectsComponent.vue"

export default {
    name: "Home",
    components: {
      AcademicsComponent,
      SkillsComponent,
      SocialMediaComponent,
      ProjectsComponent
    },
    data() {
        return {
            SP1: false,
            SP2: false,
            SP3: false,
            SP4: false,
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
            if (window.scrollY > 2600) {
                this.SP4 = true;
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

<style>
.detail-subtitle {
  font-size: 17px;
  margin-bottom: 5px;
}
.smaller-mini-logo {
  width: 50px;
  padding: 0 12px 0 12px;
  margin-bottom: 4.5px;
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
  /* background-color: #ece8fc; */
  width: 90vw;
  margin: 0 auto;
  border-top: 1px solid rgb(182, 182, 182);
  border-bottom: 1px solid rgb(182, 182, 182);
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
  padding-bottom: 15px;
  border-bottom: 1.5px solid rgb(182, 182, 182);
  margin-top: 6px;
}

.sub-desc-container {
  font-size: 20px;
  max-width: 400px;
}

.detail-container {
  text-align: left;
  font-size: 20px;
  max-width: 360px;
  margin: 0px 0 5px 0;
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
  width: 400px;
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

.container-title {
    text-align: center;
    color: #632494;
    font-size: 75px;
}

.container-sub-title {
    text-align: center;
    font-size: 23px;
    max-width: 380px;
    margin: 0 auto;
}

.flex-container {
    display: flex;
    justify-content: center;
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

.scroll-dn {
  width: 25px;
  position: absolute;
  left: 50%;
  bottom: 10%;
  transform: translateX(-50%)
}

.scroll-txt {
  font-size: 20px;
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
  width: 25px;
  transform: scaleY(-1);
  margin-left: 28px;
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