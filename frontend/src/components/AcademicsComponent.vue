<template>
    <div>
        <div class="fade-container">
            <br>
                <div class="flex-container">
                    <div>
                        <img 
                            id="uw" 
                            src="@/assets/uw.png"/>
                    </div>
                    <div class="text-box">
                        <p class="desc-container align-left" id="student">
                            Student at the University of Washington, Seattle
                        </p>
                        <p class="sub-desc-container" id="coursework">
                            Intended Informatics and Math Major<br><br>
                            GPA: <strong>3.91/4.0</strong> <br> Graduating: <strong>June 2023</strong>
                        </p>
                        <p class="sub-desc-container" id="coursework">
                        Coursework includings: <br>
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
                        <p class="desc-container align-right">
                            Undergraduate Researcher UbiComp Lab, UW</p>
                        <p class="sub-desc-container align-right"> 
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
    </div>
</template>

<script>
export default {
    name: "AcademicsComponent"
}
</script>

<style scoped>

</style>