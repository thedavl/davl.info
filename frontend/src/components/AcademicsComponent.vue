<template>
    <div>
        <div class="fade-container">
            <br><br><br>
                <div class="flex-container">
                    <div>
                        <img 
                            id="uw" 
                            src="@/assets/uw.png"/>
                    </div>
                    <div class="text-box">
                        <p class="desc-container" id="student">
                            Student at the University of Washington, Seattle
                        </p>
                        <p class="sub-desc-container" id="coursework">
                            Intended Informatics and Math Major<br><br>
                            GPA: <strong>3.91/4.0</strong> <br> Graduating: <strong>June 2023</strong>
                        </p>
                        <p class="sub-desc-container" id="coursework">
                            Coursework includes: <br>
                            <div class="bullets">
                                <ul>
                                    <li>Data Structures and Algorithms</li>
                                    <li>Data Programming in Python</li>
                                    <li>Calculus, Physics</li>
                                </ul>
                            </div>
                        </p>
                    </div>
                </div>
                <div class="flex-container">
                    <div class="text-box">
                        <p class="desc-container">
                            Undergraduate Researcher UbiComp Lab, UW</p>
                        <p class="sub-desc-container"> 
                        <strong>I've built a user-facing survey website and internal annotation site for my research lab.</strong> <br><br>
                        I work on the lab's COVID/Respiratory illness project. We're developing tools for physicians to monitor their patient's respiratory condition, 
                        through analysis of their coughs.
                        </p>
                    </div>
                    <div>
                        <img
                            class="image-container"
                            id="ubicomp"
                            src="@/assets/lablogo.png"/>
                    </div>
                </div>
        </div>
        <br><br>
    </div>
</template>

<script>
export default {
    name: "AcademicsComponent"
}
</script>

<style scoped>
#coursework {
  margin-left: 40px;
}
.bullets {
    text-align: left;
    width: 320px;
    margin: 0 auto;
    font-size: 20px;
}
</style>