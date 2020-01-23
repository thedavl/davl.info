<template>
    <div>
        <div class="flex-container">
            <div class="project-container">
                <h2>How was this website made?</h2>
                <br>
                <p>
                    This website is powered by a <strong>Full REST API</strong>, written in <strong>Python
                    </strong> using <strong>Django-REST-Framework</strong></p>
                <p> The frontend is written with <strong>Vue JS</strong>, paired with the backend API to create a 
                    <strong>Single Page Application</strong></p>
                <p> 
                    I began learning vanilla Django the summer of 2019, creating multiple simple blog-like websites utilising 
                    basic features such as posts, custom user models, and bootstrap classes</p>

                <p> The idea for this portfolio was conceived when i learned of Single Page Applications, and how 
                    quickly and smoothly they operated. I learned of the common pairing of Single Page Applications and 
                    backend REST APIs, and since i was already familiar with Django basics, Django's REST framework was a 
                    natural choice, paired with the popular Vue JS. </p>

                <p>I've learned API building and Vue JS and built this website alongside various youtube tutorials, 
                    online courses, and written guides.</p>
            </div>
            <div class="project-container">
                <h2>This Website's Features</h2>
                <ul>
                    <li>REST API + Vue JS Single Page Application Frontend</li>
                    <li>User Session Authentication</li>
                    <li>User Registration/Login &#38; Permissions</li>
                    <li>User can Post, Comment on Posts, and Like Comments</li>
                    <li>Anonymous users can view all posts, comments, and likes</li>
                </ul>
                <img class="image-container" v-bind:src="vueLogo">
                <img class="image-container" v-bind:src="drfLogo">
                <img class="image-container" v-bind:src="heroku">
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "thisWebsite",
    data() {
        return {
            vueLogo: null,
            drfLogo: null,
            heroku: null,
        }
    },
    //https://dwglogo.com/wp-content/uploads/2017/09/Vue-logo-001.svg
    methods: {
        myFunction: function () {	
            this.vueLogo = "https://dwglogo.com/wp-content/uploads/2017/09/Vue-logo-001.svg";
            this.drfLogo = "https://www.django-rest-framework.org/img/logo.png"
            this.heroku = "https://i.imgur.com/dGIjsuX.png"
        }
    },
    created() {
        this.myFunction()
    }
}
</script>
<style scoped>
.flex-container {
  display: flex;
  flex-wrap: wrap;
}
.project-container {
    padding: 15px;
    width: 480px;
    margin: 10px;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.2), 0 0px 20px 0 rgba(0, 0, 0, 0.19);
    background-color: #E8E8E8;
}
.image-container {
    width: 320px;

}
</style>