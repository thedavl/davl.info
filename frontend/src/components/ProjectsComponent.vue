<template>
    <div id="link-center">
        <div class="fade-container">
            Noteable Projects<br><br>
            <div class="flex-container">
                <div class="project-card">
                    <img class="project-card-image" src="@/assets/codebrain.png" />
                    <div class="project-card-description">
                        A website dedicated to helping you on your technical interview prep journey. <br><br>
                        Track what you've solved, and what problems to do next. Record important notes and solutions for later review. <br><br>
                        Tech used:<br> VueJs + NodeJs + ExpressJs + MongoDB Atlas<br><br>
                        <a type="button" href="https://thedavl.github.io/CodeBrain" target="_blank" class="btn btn-outline-light">Website Link</a>
                        <a type="button" href="https://github.com/thedavl/CodeBrain" target="_blank" class="btn btn-outline-light right-button">GitHub Repo</a>
                    </div>
                    <div class="project-card-title-background">
                        <p class="project-card-title">
                            CodeBrain
                        </p>
                    </div>
                </div>
                <div class="project-card">
                    <img class="project-card-image" src="@/assets/fitfriends.png" />
                    <div class="project-card-description">
                        My project for Hack'2020 24hr Hackathon <br>
                        Made with Andrea Dang and Colin Dang.<br><br>
                        FitFriends allows users to create, share, and explore workouts online.<br><br>
                        I wrote the app's NodeJs/MongoDB backend, and worked with my teammates to write the VueJs frontend.<br><br>
                        <a type="button" href="https://devpost.com/software/fitfriends" target="_blank" class="btn btn-outline-light">Hackathon Project Page</a>
                        <a type="button" href="https://github.com/thedavl/hack2020-David-Andrea-Collin" target="_blank" class="btn btn-outline-light right-button">GitHub Repo</a>
                    </div>
                    <div class="project-card-title-background">
                        <p class="project-card-title">
                            FitFriends
                        </p>
                    </div>
                </div>
                <div class="project-card">
                    <img class="project-card-image" src="@/assets/link-out.png" />
                    <div class="project-card-description">
                        LinkOut was my team's project for the 2020 Winfo (UW) Hackathon. Linkout is site made for recently released ex-cons, 
                        using the Google Maps API and browser geolocation to show job resources nearby. <br><br>
                        
                        We were one of four teams nominated for “Best Overall”, 
                        out of 80 total teams.<br><br>
                        The website was created using a VueJs frontend, and a Django REST Framework Backend (Python).

                    </div>
                    <div class="project-card-title-background">
                        <p class="project-card-title">
                            LinkOut
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ProjectsComponent"
}
</script>

<style scoped>
.right-button {
    margin-left: 10px;
}
.project-card {
    position: relative;
    background-color: black;
    width: 400px;
    height: 400px;
    margin: 10px 10px 0 10px;
    border-radius: 5px;
}
.project-card img {
    transition: 0.5s ease;
}
.project-card:hover img {
    opacity: 0.2
}
.project-card:hover .project-card-title-background {
    opacity: 0;
}
.project-card:hover .project-card-description {
    opacity: 1;
}
.project-card-description {
    color: white;
    font-size: 18px;
    width: 360px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: 0.5s ease;
    opacity: 0;
    font-weight: normal;
    z-index: 10;
    text-align: left;
}
.project-card-title {
    position: absolute;
    top: 50%;
    left: 50%;
    font-size: 40px;
    transform: translate(-50%, -50%);
    transition: 0.3s ease;
}
.project-card-title-background {
    height: 80px;
    width: 400px;
    border-radius: 0 0 5px 5px;
    background-color: white;
    position: absolute;
    top: 90.1%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: 0.3s ease;
}
.project-card-image {
    border-radius: 5px;
    object-fit: cover;
    height: 400px;
    width: 100%;
}
</style>