<template>
    <div>
        <div class="container" style="padding: 15px" align="center">
        <h1 style="font-weight: bold">About Me</h1>
        </div>
        <div class="flex-container" align="center"> 
            <div class="stuff-container">
                <h2><strong>Me</strong></h2>
                <br>
                <p>Hi, thanks for visiting my site!</p>
                <p>My name's David Lee, and i'm a prospective informatics Freshman 
                    at the University of Washington here in Seattle.</p>

                <p>When i'm not coding, studying, or attending classes, you can find 
                    me longboarding, playing badminton, 3D printing/building things, or 
                    playing video games (Counter Strike or Warframe, anyone?)</p>

                <p>I love keeping up with the latest tech, whether it be the latest   
                    computer hardware, or splurging too much on peripherals.</p>
                <br>
                <h2><strong>This whole site is a work in progress, currently working
                            on spicing up all pages</strong></h2>
            </div>
            <div class="stuff-container">
                <h2><strong>Skills</strong></h2>
                <br>
                <h4>Languages</h4>
                <ul>
                    <li>Object Oriented Programming in Java</li>
                    <li>Python - Django Web Framework, basic Python</li>
                    <li>Basic Vue JS, Single Page Applications w/ an API</li>
                    <li>Raspberry Pi python coding</li>
                    <li>Basic Selenium Java Web App Testing</li>
                </ul>
                <h4>Other</h4>
                <ul>
                    <li>Certified in Word, Excel, Powerpoint 2016</li>
                    <li>Website &#38; Application Quality Assurance</li>
                    <li>Fusion 360 &#38; Cura, 3D Printing</li>
                    <li>Raspberry pi hardware electronics</li>
                    <li>Soldering, breadboards, basic circuitry</li>
                </ul>
                <h2>Links</h2>
                <img class="logo" v-bind:src="linkedIn">
                <a target="_blank" href="https://www.linkedin.com/in/thedavl/">LinkedIn</a>
            </div>
        </div>
        
    </div>
</template>

<script>
export default {
    name: "AboutMe",
    data() {
        return {
            linkedIn: null
        }
    },
    methods: {
        myFunction: function () {	
            this.linkedIn = "https://i.imgur.com/QKDCBRy.png";
        }
    },
    created() {
        document.title = "About Me";
        this.myFunction();
    }
}
</script>

<style scoped>
.flex-container {
  display: flex;
  justify-content: center;
  align-items: center, stretch;
}

.stuff-container {
    width: 500px;
    margin-left: 20px;
    margin-right: 20px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    padding: 10px;
}

.logo {
    height: 15px;
    width: 15px;
    margin-right: 5px;
}

.texto {
    font: 51px;
}
</style>